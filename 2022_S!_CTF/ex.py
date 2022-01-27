from pwn import *

puts_got = 0x601018
puts_plt = 0x400620

gets_got = 0x601048
gets_plt = 0x400680


p = process("./ctf")

input()

p.interactive()