#include <stdio.h>
#include <stdlib.h>
#include "my402list.h"

typedef struct node {
        long int date;
        char *desc;
        float amnt;
        char type;
} node;

void read_file() {
	FILE *pFile;	
	char *file_name = "test.tfile";

	pFile = fopen(file_name,"r");
	if (!pFile) {
		printf("File could not be opened.\n");
	}
	else {
		char buffer[1024];
		while( fgets(buffer,1024,pFile) != NULL ) {

			node *new_node = (node *) malloc (sizeof(node));
			char word[1024];
			int len=0, word_count=0;

			for (int i=0; i<sizeof(buffer); i++) {
				if (buffer[i] == '\t' || buffer[i] == '\n') {
					if (word_count == 0) new_node->type = word[0];
					else if (word_count == 1) new_node->date = (long int)word;
					else if (word_count == 2) new_node->amnt = (float)word;
					else if (word_count == 3) new_node->desc = word;
					word[0] = '\0';
					len = 0;
				}
				else {
					word[len] = buffer[i];
					word[++len] = '\0';
				}
			}
		}
	}
	fclose(pFile);
}

int main() {
	read_file();
	return 0;
}
