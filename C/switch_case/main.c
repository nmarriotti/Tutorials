#include <stdio.h>

int main() {

	int option;

	printf("Select an option 1-3: ");
	scanf("%i", &option);

	switch(option) {
		case 1: 
			puts("option is 1");
			break;
		case 2:
			puts("option is 2");
			break;
		case 3:
			puts("option is 3");
			break;
		default:
			puts("Invalid option!");
	}
}
