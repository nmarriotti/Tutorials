#include <stdio.h>

int main() {

	struct recipe {
		const char *name;
	        char *description;
		int prepTime;
		int servings;
	};

	struct recipe spaghetti = {"Spaghetti","Some delicious spaghetti",20,4};

        printf("Recipe: %s\nDescription: %s\nPrep Time: %d\nServings: %d\n",
               spaghetti.name, spaghetti.description, spaghetti.prepTime, spaghetti.servings);

	return 0;
}
