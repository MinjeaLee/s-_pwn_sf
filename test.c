#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *p1 = malloc(0x30);
    char *p2 = malloc(0x30);
    char *p3 = malloc(0x30);
    free(p2);
    return 0;
}