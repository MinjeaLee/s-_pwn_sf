#include <stdio.h>

int win(){
    system("/bin/sh");  // 
}

int main(){
    char buf[10];

    read(0, buf, 100);

    return 0;
}