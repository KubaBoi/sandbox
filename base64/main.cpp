
#include <stdio.h>
#include <iostream>
#include <bitset>

using namespace std;

void printBits(bitset<24> c) 
{
        
    printf("%d: ", c);
    std::cout << c << std::endl;
}

int main() 
{
    char table[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    char str[] = "Nazdar, světe! Příliš žluťoučký kůň úpěl ďábelské ódy.";
    int len = 0;
    while (str[len++]) {}
    len--;

    printf("111111110000000011111111\n");

    int o_str_len = (len / 3) * 4 + 3;
    printf("%d %d\n", len, o_str_len);

    char *o_str = (char *)malloc(o_str_len);
    o_str[o_str_len - 1] = 0;

    int overlap = len % 3;
    printf("%d\n", overlap);
    bitset<24> bit24;
    bitset<6> bit6;
    for (int i = 0; i < len; i += 3)
    {
        for (int o = 0; o < 3; o++) {
            int offset = o * 8;
            for (int bit = 0; bit < 8; bit++) 
            {
                bit24[23 - offset] = (str[i + o] >> (7 - bit)) & 1; 
                offset++;
            }
        }

        for (int o = 0; o < 4; o++)
        {
            int offset = o * 6;
            for (int bit = 0; bit < 6; bit++)
                bit6[bit] = bit24[offset + bit];

            int ind = (i / 3) * 4 + 3 - o;
            if (ind + overlap >= o_str_len)
            {
                printf("%d %d %d\n", ind, overlap, o_str_len);
                o_str[ind] = '=';
            }
            else
                o_str[ind] = table[bit6.to_ulong()];
        }

        /*for (int o = 0; o < overlap; o++)
        {
            o_str[(len / 3) * 4 - o + 2] = '=';
        }*/
    }
    printf("str: '%s'\n", o_str);
}