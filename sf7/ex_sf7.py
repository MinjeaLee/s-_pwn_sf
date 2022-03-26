from pwn import *

p = process('./sf7')

def create(size, content):
    p.recvuntil("> ")
    p.sendline("1")
    p.recvuntil('size : ')
    p.send(size)
    p.recvuntil("memo : ")
    p.send(content)

p.recvuntil('name : ')
p.send('leeminjea')

input()



p.interactive()

