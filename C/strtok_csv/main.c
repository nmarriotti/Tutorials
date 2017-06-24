#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void parse(char *line) {
    char *token;
    char delim[2] = ",";

    token = strtok(line, delim);

    while(token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, delim);
    }
}

void readfile(char *filename) {
    FILE *fp = fopen(filename, "r");
    if(fp) 
    {
        char buffer[255];

	    while(fp) {
		    fgets(buffer, 255, fp);   
            buffer[strlen(buffer)-1]='\0'; 
		    if(feof(fp)) break; 
            parse(buffer); 
	    }
        fclose(fp);
    } 
    else {
        printf("File does not exist.\n");
    }

}

int main(int argc, char *argv[]) {

    if(argc > 1) {
        char *filename = argv[1];
        readfile(filename);
    }

    return 0;
}

