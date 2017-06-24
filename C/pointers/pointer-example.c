#include <stdio.h>

int main(int argc, int argv[]) {

    int num = 500;
    int *p = &num;

    printf("Pointer is at: %p\n", p);
    printf("Value is: %i\n", *p);
    return 0;
}