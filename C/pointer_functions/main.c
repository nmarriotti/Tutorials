#include <stdio.h>

void minus10(int *x);

int main() {
	int value = 20;
	minus10(&value);
	printf("%d",value);

	return 0;
}

void minus10(int *x) {
	*x = *x - 10;
}
