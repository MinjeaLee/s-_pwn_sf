from pwn import *

p = process('./bof')

pop_rdi = 0x0000000000401343
pop_rsi_r15 = 0x0000000000401341

p.recvuntil("?\n")


# canary = b""
# canary += b"A" * 

p.interactive()