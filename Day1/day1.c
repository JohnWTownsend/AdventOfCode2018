#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp = fopen("day1Input.txt", "r");
    int val;
    int sum = 0;

    while (!feof(fp))
    {
        fscanf(fp, "%d", &val);
        sum += val;
    }
    printf("%d\n", sum);
    return 0;
}