from pwn import *

p = process('./app')

p.interactive()