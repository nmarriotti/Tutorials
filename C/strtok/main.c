#include <stdio.h>
#include <string.h>

int main() {
    char myString[] = "This,is,a,comma,delimited,string";
    char delim[2] = ",";
    char *token;

    token = strtok(myString, delim);
    printf("%s", token);

    while(token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, delim);
    }

    return 0;
}