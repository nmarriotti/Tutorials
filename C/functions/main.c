#include <stdio.h>

// Function Prototypes
void saySomething();
void doSomething(int *);

int main() {
	int number = 6;
	saySomething();
	doSomething(&number);	
	printf("Number is %d\n", number);
	return 0;
}

void saySomething() {
	printf("Hello there!\n");
}

void doSomething(int *x) {
	*x = *x * 2;
}
