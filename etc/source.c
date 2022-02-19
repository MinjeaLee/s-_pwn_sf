#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <fcntl.h>

void menu(void);
int read_int(void);
void show_flag(void);

int main(void)
{
    int choice = 0;
    char buffer[256] = { 0, };
    char enter;

    setbuf(stdin, 0);
    setbuf(stdout, 0);

    puts("=======================================");
    puts("|                                     |");
    puts("|        ☆  Merry Christmas ☆         |");
    puts("|         I am a Dream Santa          |");
    puts("|    I'll give you some present :)    |");
    puts("|         What do you want ?          |");
    puts("|                                     |");
    puts("=======================================");

    while (1) {
        menu();
        choice = read_int();
        switch (choice) {
            case 1:
                gets(buffer);
                break;

            case 2:
                show_flag();
                break;

            case 3:
                system("/bin/sh");
                break;

            case 4:
                return 0;

            default:
                puts("no..");
        }
    }
}

void menu(void)
{
    printf("\n");
    puts("1. I want buffer overflow");
    puts("2. I want flag");
    puts("3. I want shell");
    puts("4. I want nothing");
    printf(">> ");
}

int read_int(void)
{
    char buf[10];

    read(0, buf, sizeof(buf));
    return atoi(buf);
}

void show_flag(void)
{
    int fd = 0, idx = 0;
    char flag[256] = { 0, };

    puts("Input index");
    printf(">> ");
    idx = read_int();

    if (idx < 0 || idx > 2) {
        puts("I'll let you know next year :p");
        return;
    }

    fd = open("/home/ctf/flag", O_RDONLY);

    read(fd, flag, sizeof(flag));
    printf("flag[%d] is %c\n", idx, flag[idx]);
    memset(flag, 0, sizeof(flag));

    return;
}