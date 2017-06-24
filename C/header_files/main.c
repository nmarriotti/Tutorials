#include <stdio.h>
#include "add.h"

int main() {
	
	int num1, num2, result;

	printf("Enter a number: ");
	scanf("%d", &num1);

	printf("Enter another number: ");
	scanf("%d", &num2);

	result = addNumbers(num1, num2);

	printf("Result: %d\n", result);

	return 0;
}
