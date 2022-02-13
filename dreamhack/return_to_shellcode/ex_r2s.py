from pwn import *

p = process("./r2s")

p.interactive()