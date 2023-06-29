#include <time.h>
#include <stdio.h>

void for_cycle(int count)
{
    for (int o = 0; o < count; o++) 
    {
        for (int i = 0; i < count; i++)
        {
            int a = 0;
            int b = 2;
            int c = a + b;
        }
    }
}

void while_cycle(int count)
{
    int o = 0;
    while (o < count)
    {
        int i = 0;
        while (i < count)
        {
            int a = 0;
            int b = 2;
            int c = a + b;
            i++;
        }
        o++;
    }
}

int main()
{
    long count = 100000000000;
    time_t start, end;
    start = time(NULL);
    for_cycle(count);
    end = time(NULL);
    printf("%ld\n", end - start);

    start = time(NULL);
    while_cycle(count);
    end = time(NULL);
    printf("%ld\n", end - start);
}