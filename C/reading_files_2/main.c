#include <stdio.h>

int main() {
	FILE *file = fopen("example.txt", "r");

	char c;

	do {
		c = fgetc(file);
		printf("%c", c);
	} while (c != EOF);

	fclose(file);
	return 0;
}
