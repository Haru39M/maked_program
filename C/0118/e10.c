#include <stdio.h>
#define NUM 5
#define LEN 100
void count_char(char pc[][LEN], char c, int *pi)
{
    int i = 0;
    int j = 0;
    for (j = 0; j < 5; j++)
    {
        i = 0;
        while (*(pc[0] + i) != '\0')
        {
            printf("%c\n", *(pc[0] + i));
            i++;
            *pi += 1;
        }
        pc++;
        *pi++;
    }

    // *pi += 1;
    // pi++;
}
int main(void)
{
    char c;
    char stations[NUM][LEN] = {"mikage", "kobe", "okamoto", "rokko", "ojikoen"};
    int i = 0;
    char *j;
    int count[NUM] = {0};

    printf("input a character:\n");
    scanf(" %c", &c);
    count_char(stations, c, count);

    for (i = 0; i < NUM; i++)
    {
        printf("%s : ", stations[i]);
        printf("%d\n", count[i]);
    }
    return 0;
}