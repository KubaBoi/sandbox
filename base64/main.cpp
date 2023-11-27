/*
Vezmou se vzdycky 3 bajty, ktery se spoji do 3*8=24 bitoveho retezce
ten retezec se potom rozdeli na 4 6ti bitové hodnoty
kazda z tehle hodnot je index znaku `char table[]`

pokud pocet nevychazi presne na trojice, zakoduje se posledni nebo posledni dva
bajty a pridaji se rovnitka
*/


#include <stdio.h>
#include <iostream>
#include <bitset>
#include <cstring>

using namespace std;

char table[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

char *encodeB64(char *str)
{
    int len = strlen(str);
    
    int o_str_len = (len / 3) * 4 + 3;
    char *o_str = (char *)malloc(o_str_len);
    for (int i = 0; i < o_str_len; i++)
        o_str[i] = 0;

    int overlap = 3 - len % 3;
    bitset<24> bit24;
    bitset<6> bit6;
    for (int i = 0; i < len; i += 3)
    {
        for (int o = 0; o < 3; o++) {
            int offset = o * 8;
            for (int bit = 0; bit < 8; bit++) // tady to bude nejspis sahat spatne do pameti
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
            o_str[ind] = table[bit6.to_ulong()];
        }
    }
    if (overlap < 3) 
    {
        for (int o = 0; o < overlap; o++)
            o_str[o_str_len - o] = '=';
    }
    return o_str;
}

int main() 
{
    char str[] = "Nazdar, světe! Příliš žluťoučký kůň úpěl ďábelské ódy.";
    printf("str: %s\n", str);
    char *o_str = encodeB64(str);
    printf("b64: '%s'\n", o_str);
    free(o_str);
}