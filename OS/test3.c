#include <stdio.h>
#include <stdlib.h>

int main() {
	char *name;
	printf("Enter your name: ");
	gets(name);

	printf("\nYour name is: %s\n",name);
	return 0;
}
