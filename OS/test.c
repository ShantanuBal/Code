#include <stdio.h>
#include <stdlib.h>

struct node{
	int key;
	struct node * next;
	struct ndoe * prev;
};

typedef struct node node;

int main() {
	int a[5] = {1,2,3,4,5};
	
	node *head = (node *)malloc(sizeof(node));
	head->key = a[0];
	node *root = head;

	printf("%d\n", head->key);
	
	for (int i=1; i < sizeof(a)/sizeof(a[0]); i++) {
		node *new_node = (node *)malloc(sizeof(node));
		head->next = new_node;
		new_node->key = a[i];
		new_node->next = NULL;
		head = new_node;
	}

	node *list = root;
	while (list != NULL){
		printf("%d",list->key);
		list = list->next;
	}
	return 0;
}

