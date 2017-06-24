#include <stdio.h>

int askForNumber() {
	int number;
	printf("Enter a number: ");
	scanf("%d", &number);
	return number;
}

void print(void (*f)(int)) {
	printf("You entered");
}

int main() {
	print(askForNumber());	
}
