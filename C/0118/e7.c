#include <stdio.h>
int index_char(char *p,char c){
    int index = 0;
    while (*p != '\0')
    {
        if (*p == c)
        {
            break;
        }
        else
        {
            p++;
            index++;
        }
    }
    if(*p == '\0'){
        index = -1;
    }
    return index;
}
int main(void){
    char word[100];
    char c;
    int index=0;
    printf("input a word:\n");
    scanf("%s",word);
    printf("input a character:\n");
    scanf(" %c",&c);

    index = index_char(word,c);
    printf("index of '%c' : %d",c,index);
    return 0;
}