//gcc -o Notepad Notepad.c -fno-stack-protector
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

void Initalize(){
   setvbuf(stdin, (char *)NULL, _IONBF, 0);
   setvbuf(stdout, (char *)NULL, _IONBF, 0);
   setvbuf(stderr, (char *)NULL, _IONBF, 0);
}

void main()
{
    Initalize();

    puts("Welcome to Dream's Notepad!\n");

    char title[10] = {0,};
    char content[64] = {0,};

    puts("-----Enter the content-----");
    read(0, content, sizeof(content) - 1);

    for (int i = 0; content[i] != 0; i++)
    {
        if (content[i] == '\n')
        {
            content[i] = 0;
            break;
        }
    }

    if(strstr(content, ".") != NULL) {
        puts("It can't be..");
        return;
    }
    else if(strstr(content, "/") != NULL) {
        puts("It can't be..");
        return;
    }
    else if(strstr(content, ";") != NULL) {
        puts("It can't be..");
        return;
    }
    else if(strstr(content, "*") != NULL) {
        puts("It can't be..");
        return;
    }
    else if(strstr(content, "cat") != NULL) {
        puts("It can't be..");
        return;
    }
    else if(strstr(content, "echo") != NULL) {
        puts("It can't be..");
        return;
    }
    else if(strstr(content, "flag") != NULL) {
        puts("It can't be..");
        return;
    }
    else if(strstr(content, "sh") != NULL) {
        puts("It can't be..");
        return;
    }
    else if(strstr(content, "bin") != NULL) {
        puts("It can't be..");
        return;
    }

    char tmp[128] = {0,};

    sprintf(tmp, "echo %s > /home/Dnote/note", content);
    system(tmp);
    
    FILE* p = fopen("/home/Dnote/note", "r");
    unsigned int size = 0;
    if (p > 0)
    {
        fseek(p, 0, SEEK_END);
        size = ftell(p) + 1;
        fclose(p);
        remove("/home/Dnote/note");
    }

    char message[256];
    
    puts("\n-----Leave a message-----");
    read(0, message, size - 1);

    puts("\nBye Bye!!:-)");
}