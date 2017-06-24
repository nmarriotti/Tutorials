#include <stdio.h>

int main(int argc, char* argv[]) {

	FILE *fp = fopen(argv[1], "r");

	char buffer[255];
	char *c;
	
	while(fp) 
	{
		fgets(buffer, 255, fp); /* Reads entire line */
		if(feof(fp)) break; /* Stop if end of file reached */
		printf("%s", buffer); /* print the buffer */

	} 

	fclose(fp);
	return 0;
}
