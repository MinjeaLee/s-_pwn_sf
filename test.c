#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
char secret[256];
int read_secret() {
  FILE *fp;
  if ((fp = fopen("secret.txt", "r")) == NULL) {
    fprintf(stderr, "`secret.exe` does not exist");
    return -1;
  }
  fgets(secret, sizeof(secret), fp);
  fclose(fp);
  return 0;
}
int main() {
  char *docs[] = {"COMPANY INFORMATION", "MEMBER LIST", "MEMBER SALARY",
                  "COMMUNITY"};
  char *secret_code = secret;
  int idx;
  // Read the secret file
  if (read_secret() != 0) {
    exit(-1);
  }
  // Exploit OOB to print the secret
  puts("What do you want to read?");
  for (int i = 0; i < 4; i++) {
    printf("%d. %s\n", i + 1, docs[i]);
  }
  printf("> ");
  scanf("%d", &idx);
  if (idx > 4) {
    printf("Detect out-of-bounds");
    exit(-1);
  }
  puts(docs[idx - 1]);
  return 0;
}