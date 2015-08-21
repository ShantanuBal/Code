#include <stdio.h>

int main() {
	char *word;
	word = "Hello world!";
	while(*word) {
		printf("%c\n",*word++);
	}
	return 0;
}
