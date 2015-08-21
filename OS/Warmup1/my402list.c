// CS402 - Warmup Assignment I

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "my402list.h"
#include "cs402.h"

My402List *list;

typedef struct node {
        char type;
        long int date;
        float amnt;
        char desc[1024];
} node;

//Traverse the list and display its records in a tabulated format.
void traverse() {
	if (!list -> num_members) { printf("This list is empty!"); return; }
	
	float balance = 0;
	My402ListElem *elem = (list -> anchor).next;
	
	printf("\n\t+-----------------+--------------------------+----------------+----------------+");
	printf("\n\t|       Date      | Description              |         Amount |        Balance |");
	printf("\n\t+-----------------+--------------------------+----------------+----------------+");
		
	while ( elem != &(list -> anchor)) {
		char date[25], date1[11], date2[5], desc[26], amnt[15], famnt[13], baln[15], fbaln[13];
		strncpy(date, ctime(&(((node *)(elem->obj))->date)), 24);
		strncpy(date1, date, 10);
		strncpy(date2, &date[20], 4);
		if ( ((node *)(elem->obj))->type == '+' ) balance += ((node *)(elem->obj))->amnt; 
		else balance -= ((node *)(elem->obj))->amnt;
		
		strncpy(desc, ((node *)(elem->obj))->desc, 25);
		for (int i=0; i<=24; i++) {
			if (desc[i] == '\0') {
				for (int j=i; j<=24; j++) 
					desc[j] = ' ';
				desc[25] = '\0';
				break;
			}
		}
		
		// Format Amount field.
		char buffer1[15]=" ?,???,???.?? ", buffer2[15]="(?,???,???.??)";
		if ( ((node *)(elem->obj))->amnt >= 10000000 ) strcpy(amnt,buffer1);
		else if ( ((node *)(elem->obj))->amnt <= -10000000 ) strcpy(amnt,buffer2);
		else {
			sprintf(famnt, "%.2f", ((node *)(elem->obj))->amnt);
			int l_famnt = strlen(famnt);
			if ( ((node *)(elem->obj))->type == '+' ) { amnt[0] = ' '; amnt[13] = ' '; }
			else { amnt[0] = '('; amnt[13] = ')'; }
			amnt[14] = '\0';
			
			int i=12;
			for ( int j=l_famnt-1; j>=0; j--) {
				amnt[i] = famnt[j];
				i -= 1;
			}
			for ( int j=1; j<= i; j++)
				amnt[j] = ' ';
		}

		// Format Balance field.
		if (balance >= 10000000) strcpy(baln,buffer1);
		else if (balance <= -10000000) strcpy(baln,buffer2);
		else {
			sprintf(fbaln, "%.2f", balance);
			int l_fbaln = strlen(fbaln);
			if ( balance >= 0 ) { baln[0] = ' '; baln[13] = ' '; }
			else { baln[0] = '('; baln[13] = ')'; }
			baln[14] = '\0';
			
			int i=12;
			for ( int j=l_fbaln-1; j>=0; j--) {
				baln[i] = fbaln[j];
				i -= 1;
			}
			for ( int j=1; j<= i; j++)
				baln[j] = ' ';
		}

		printf("\n\t| %s %s | %s| %s | %s |", date1, date2, desc, amnt, baln );
		
		elem = elem->next;
	}
	printf("\n\t+-----------------+--------------------------+----------------+----------------+\n");
}

//Returns the number of elements in the list. 
int Length() { return list->num_members; }

//Returns TRUE if the list is empty. Returns FALSE otherwise. 
int Empty() { return list->num_members <= 0; }

//If list is empty, just add obj to the list. Otherwise, add obj after Last(). This function returns TRUE if the operation is performed successfully and returns FALSE otherwise. 
int Append(void *obj) {

	My402ListElem *new_link = (My402ListElem *) malloc (sizeof(My402ListElem));
	new_link -> obj = (node *)obj;
	
	My402ListElem *last = (list -> anchor).prev;

	new_link -> next = &(list -> anchor);
	new_link -> prev = last;

	last -> next = new_link;
	(list -> anchor).prev = new_link;
	
	list -> num_members += 1;
	return 1;
}

//If list is empty, just add obj to the list. Otherwise, add obj before First(). This function returns TRUE if the operation is performed successfully and returns FALSE otherwise. 
int Prepend(void *obj) {
	My402ListElem *new_link = (My402ListElem *) malloc (sizeof(My402ListElem));
	new_link -> obj = (node *)obj;
	
	My402ListElem *first = (list -> anchor).next;

	new_link -> prev = &(list -> anchor);
	new_link -> next = first;

	first -> prev = new_link;
	(list -> anchor).next = new_link;
	
	list -> num_members += 1;
	return 1;
}

//Unlink and delete elem from the list. Please do not delete the object pointed to by elem and do not check if elem is on the list.
void Unlink(My402ListElem *elem) {
	
	My402ListElem *pPrev = elem -> prev;
	My402ListElem *pNext = elem -> next;
	pPrev -> next = pNext;
	pNext -> prev = pPrev;
	free(elem);
}

//Unlink and delete all elements from the list and make the list empty. Please do not delete the objects pointed to be the list elements. 
void UnlinkAll() {
	if (!list -> num_members) { printf("This list is empty!"); return; }

        My402ListElem *elem = (list -> anchor).next;
	while ( elem != &(list -> anchor)) {
                elem = elem->next;
		free(elem->prev);
	}

	(list -> anchor).next = &(list -> anchor);
        (list -> anchor).prev = &(list -> anchor);
}

//Insert obj between elem and elem->prev. If elem is NULL, then this is the same as Prepend(). This function returns TRUE if the operation is performed successfully and returns FALSE otherwise. Please do not check if elem is on the list. 
int InsertBefore(void *obj, My402ListElem *elem) {
	if ( elem == NULL) { 
		if (Prepend(obj)) return TRUE; else return FALSE; 
	}
	else {
		My402ListElem *new_link = (My402ListElem *) malloc (sizeof(My402ListElem));
		new_link -> obj = obj;
		new_link -> next = elem;
		new_link -> prev = elem -> prev;

		(elem -> prev) -> next = new_link;
		elem -> prev = new_link;
		return TRUE;
	}
}

//Insert obj between elem and elem->next. If elem is NULL, then this is the same as Append(). This function returns TRUE if the operation is performed successfully and returns FALSE otherwise. Please do not check if elem is on the list.
int InsertAfter(void *obj, My402ListElem *elem) {
	if ( elem == NULL) { 
		if (Append(obj)) return TRUE; else return FALSE;
	}
        else {
                My402ListElem *new_link = (My402ListElem *) malloc (sizeof(My402ListElem));
                new_link -> obj = obj;
                new_link -> next = elem -> next;
                new_link -> prev = elem;

                (elem -> next) -> prev = new_link;
                elem -> next = new_link;
                return TRUE;
        }
}

//Returns the first list element or NULL if the list is empty. 
My402ListElem *First() {
	if ( Empty() ) return NULL;
	else return (list->anchor).next;
}

//Returns the last list element or NULL if the list is empty. 
My402ListElem *Last() {
	if ( Empty() ) return NULL;
        else return (list->anchor).prev;
}

//Returns elem->next or NULL if elem is the last item on the list. Please do not check if elem is on the list. 
My402ListElem *Next(My402ListElem *elem) {
	if ( elem->next == &(list->anchor)) return NULL;
	else return elem->next;
}

//Returns elem->prev or NULL if elem is the first item on the list. Please do not check if elem is on the list.
My402ListElem *Prev(My402ListElem *elem) {
	if ( elem->prev == &(list->anchor)) return NULL;
        else return elem->prev;
}

//Returns the list element elem such that elem->obj == obj. Returns NULL if no such element can be found. 
My402ListElem *Find(void *obj) {
	My402ListElem *elem = (list->anchor).next;
	while (elem != &(list->anchor)) {
		if (elem->obj == (node *)obj) return elem;
		elem = elem -> next;
	}
	return NULL;
}

//    Initialize the list into an empty list. Returns TRUE if all is well and returns FALSE if there is an error initializing the list. 
int Init() {
	
	list = (My402List *) malloc (sizeof(My402List));
        if (!list) return FALSE;
	list -> num_members = 0;
        (list -> anchor).next = &(list -> anchor);
        (list -> anchor).prev = &(list -> anchor);
        (list -> anchor).obj = NULL;
	return TRUE;
}

void insert(node *new_node) {

	if ( Empty() ) {
		if (!Append(new_node)) printf("Record could not be appended.\n");
	}
	else {
		//if (!Append(new_node)) printf("Record could not be appended.\n");
		
		My402ListElem *elem = (list -> anchor).next;
		while ( elem != &(list -> anchor)) {
			if ( new_node->date < ((node *)(elem->obj))->date ) {
				if(InsertBefore(new_node, elem)) return;
				else { printf("Record could not be inserted into the list."); exit(0); }
			}
			if ( new_node->date == ((node *)(elem->obj))->date ) { printf("Two or more records have the same time stamp."); exit(0); }
			elem = elem->next;
		}
		Append(new_node);
	}
}

void read_file() {
	FILE *pFile;
	char *file_name = "test.tfile";

	pFile = fopen(file_name,"r");
	if (!pFile) {
		printf("File could not be opened.\n");
	}
	else {
		char buffer[1024];

		// Read file one line at a time
		while( fgets(buffer,1024,pFile) != NULL ) {

			// New node creation
			node *new_node = (node *) malloc (sizeof(node));
			char word[1024];
			int len=0, word_count=0;

			for (int i=0; i<sizeof(buffer); i++) {
				if (buffer[i] == '\t' || buffer[i] == '\n') {
					if (word_count == 0) new_node->type = word[0];
					else if (word_count == 1) new_node->date = (long int)atof(word);
					else if (word_count == 2) new_node->amnt = (float)atof(word);
					else if (word_count == 3) strcpy(new_node->desc,word);
					word[0] = '\0';
					len = 0;
					word_count++;
				}
				else {
					word[len] = buffer[i];
					word[++len] = '\0';
				}
			}

			// Insert node in list
			insert(new_node);	
		}
		traverse();
	}
	fclose(pFile);
}

int main() {

	Init();
	read_file();
	return 0;
}
