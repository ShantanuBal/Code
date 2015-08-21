#include <string.h>
#include <stdio.h>

int main()
{
   const char str[180] = "This is - www.tutorialspoint.com - website";
   const char s[2] = "-";
   char token[100];
   
   /* get the first token */
   token = strtok(str, s);
   
   /* walk through other tokens */
   while( token != NULL ) 
   {
      printf( " %s\n", token );
    
      token = strtok(token, s);
   }
   
   return(0);
}
