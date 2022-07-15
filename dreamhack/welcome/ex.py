from pwn import *

# p = process("./")
# nc host3.dreamhack.games 23085
p = remote("host3.dreamhack.games", 23085)

p.interactive()

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv