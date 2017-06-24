#include <stdio.h>

void PrintNumber(int *x) {
	printf("x is stored at: %p\n", x);
	printf("x points to value of %i\n", *x);
}

int main() {

	int var = 100;
	int *i = NULL;

	i = &var;

	printf("var is stored at: %p\n", &var);
	printf("i points to memory address of %p\n", i);
	printf("i points to value of %i\n", *i);

	PrintNumber(i);

	return 0;
}
