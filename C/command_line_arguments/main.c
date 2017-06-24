#include <stdio.h>

int main(int argc, char *argv[]) {

	printf("Arguments passed: %i\n", argc);

	for(int i=0; i<argc; i++) {
		printf("Argument %i: %s\n", i, argv[i]);
	}
}

