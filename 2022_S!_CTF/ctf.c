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

void sys(){
    system("/bin/sh");
}

int main(int argc, char *argv[]) {
    char buf[0x80];
    initialize();
    

    gets(buf);
    printf("Your data : %s", &buf);
    gets(buf);

    return 0;
}
