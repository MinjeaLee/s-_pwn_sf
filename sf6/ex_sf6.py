from pwn import *

p = process("./tomato")

p.interactive()