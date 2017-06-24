#include <stdio.h>

int main() {
	char filename[80];
	printf("Enter a filename: ");
	scanf("%79s", filename);

	printf("You entered: %s\n", filename);

	return 0;
}
