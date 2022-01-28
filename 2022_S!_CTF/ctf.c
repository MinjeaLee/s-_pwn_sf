#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>


void alarm_handler() {
    puts("TIME OUT");
    exit(-1);
}


void initialize() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    signal(SIGALRM, alarm_handler);
    alarm(30);
}

void happy(){
    puts(" ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄   ");
    puts("▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌  ");
    puts("▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌  ");
    puts("▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌  ");
    puts("▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌  ");
    puts("▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌  ");
    puts("▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀   ");
    puts("▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌               ▐░▌       ");
    puts("▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌               ▐░▌       ");
    puts("▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌               ▐░▌       ");
    puts(" ▀         ▀  ▀         ▀  ▀            ▀                 ▀        ");
}

void Two_Thousand_Twenty_Two(){
    puts("         ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄ ");
    puts("        ▐░░░░░░░░░░░▌ ▐░░░░░░░░░▌  ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌");
    puts("         ▀▀▀▀▀▀▀▀▀█░▌▐░█░█▀▀▀▀▀█░▌▐░█░█▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌");
    puts("                  ▐░▌▐░▌▐░▌    ▐░▌▐░▌▐░▌    ▐░▌          ▐░▌");
    puts("                  ▐░▌▐░▌ ▐░▌   ▐░▌▐░▌ ▐░▌   ▐░▌          ▐░▌");
    puts("         ▄▄▄▄▄▄▄▄▄█░▌▐░▌  ▐░▌  ▐░▌▐░▌  ▐░▌  ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌");
    puts("        ▐░░░░░░░░░░░▌▐░▌   ▐░▌ ▐░▌▐░▌   ▐░▌ ▐░▌▐░░░░░░░░░░░▌");
    puts("        ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌    ▐░▌▐░▌▐░▌    ▐░▌▐░▌▐░█▀▀▀▀▀▀▀▀▀ ");
    puts("        ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄█░█░▌▐░█▄▄▄▄▄█░█░▌▐░█▄▄▄▄▄▄▄▄▄ ");
    puts("        ▐░░░░░░░░░░░▌ ▐░░░░░░░░░▌  ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌");
    puts("         ▀▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀    ▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀ ");
}

void gift(){
    system("/bin/sh");
}

int main(int argc, char *argv[]) {
    char buf[0x80] = {};
    initialize();
    happy();
    Two_Thousand_Twenty_Two();
    printf("What kind of bird do you like? >> ");
    read(0, &buf, 0x84);
    printf("Oh you like this bird!! >> %s", &buf);
    read(0, &buf, 0x100);
    return 0;
}
