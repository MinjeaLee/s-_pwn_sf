// file name : execve.c
// complie : gcc -o execve execve.c -masm=intel

__asm__(
    ".global run_sh\n"
    "run_sh:\n"

    "mov rax, 0x68732f2f6e69622f\n"
    "push rax\n"
    "mov rdi, rsp # rdi = '/bin/sh'\n"
    "xor rsi, rsi # rsi = 0\n"
    "xor rdx, rdx # rdx = 0\n"
    "mov rax, 0x3b # rax = sys_execve \n"
    "syscall # execve('/bin/sh', NULL, NULL)\n"

    "xor rdi, rdi # rdi = 0\n"
    "mov rax, 0x3c # rax = sys_exit\n"
    "syscall # exit(0)\n"
);

void run_sh();

int main() {
    run_sh();
}
