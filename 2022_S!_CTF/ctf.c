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

    // signal(SIGALRM, alarm_handler);
    // alarm(100);
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
    puts("        ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ ");
    puts("       ▐░░░░░░░░░░░▌ ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌");
    puts("        ▀▀▀▀▀▀▀▀▀█░▌▐░█░█▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌");
    puts("                 ▐░▌▐░▌▐░▌    ▐░▌          ▐░▌          ▐░▌");
    puts("                 ▐░▌▐░▌ ▐░▌   ▐░▌          ▐░▌          ▐░▌");
    puts("        ▄▄▄▄▄▄▄▄▄█░▌▐░▌  ▐░▌  ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌");
    puts("       ▐░░░░░░░░░░░▌▐░▌   ▐░▌ ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌");
    puts("       ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌    ▐░▌▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ");
    puts("       ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄█░█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ");
    puts("       ▐░░░░░░░░░░░▌ ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌");
    puts("        ▀▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ ");
}

void gift(){
    system("/bin/sh");
}

void profile(){
    char buf[32] = {};

    printf("What kind of bird do you like? >> ");
    read(0, buf, 512);
    printf("Oh you like this bird!! >> %s", &buf);
    printf("What's your bucket list for 2022? >> ");
    read(0, buf, 512);
    printf(buf);
    printf("Additional comments >> ");
    read(0, buf, 0x200);
}

int main(int argc, char *argv[]) {
    initialize();
    happy();
    Two_Thousand_Twenty_Two();

    profile();
    
    return 0;
}
