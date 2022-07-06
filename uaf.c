// Name: uaf.c
// Compile: gcc -o uaf uaf.c -no-pie
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct NameTag
{
    char team_name[16];
    char name[32];
    void (*func)();
};
struct Secret
{
    char secret_name[16];
    char secret_info[32];
    long code;
};
int main()
{
    int idx;
    struct NameTag *nametag;
    struct Secret *secret;

    secret = malloc(sizeof(struct Secret));

    strcpy(secret->secret_name, "ADMIN PASSWORD");
    strcpy(secret->secret_info, "P@ssw0rd!@#");
    secret->code = 0x1337;

    free(secret);
    secret = NULL;

    nametag = malloc(sizeof(struct NameTag));

    strcpy(nametag->team_name, "security team");
    memcpy(nametag->name, "S", 1);

    printf("Team Name: %s\n", nametag->team_name);
    printf("Name: %s\n", nametag->name);
    
    if (nametag->func)
    {
        printf("Nametag function: %p\n", nametag->func);
        nametag->func();
    }
}