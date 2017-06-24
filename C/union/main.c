#include <stdio.h>

int main() {

	typedef union {
		float weight;
                float volume;
		int count;
	} quantity;

	typedef struct {
		const char *item;
		quantity amount;
	} order;

	order i = {"Lemons", .amount.count=3};

	printf("You ordered %i %s\n", i.amount.count, i.item);


	return 0;
}
