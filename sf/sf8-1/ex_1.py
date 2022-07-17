from pwn import *

p = process("./sf8-1")

def create(name,kind,age):
        p.sendline('1')
        p.sendlineafter('> ',name)
        p.sendlineafter('> ',kind)
        p.sendlineafter('> ',age)

def edit(index,name,kind,age):
        p.sendline('2')
        p.sendlineafter('> ',index)
        p.sendlineafter('> ',name)
        p.sendlineafter('> ',kind)
        p.sendlineafter('> ',age)


create('A','A','A')



p.interactive()