#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_WORDS 10000
#define MAX_WORD_LENGTH 100

void printWords(char words[MAX_WORDS][MAX_WORD_LENGTH])
{
    int i;
    for (i = 0; i < MAX_WORD_LENGTH; i++)
    {
        printf("%s\n", words[i]);
    }
}

void clearNewlines(char words[MAX_WORDS][MAX_WORD_LENGTH])
{
    int i;
    int end;
    for (i = 0; i < MAX_WORD_LENGTH; i++)
    {
        end = strlen(words[i]) - 1;
        words[i][end] = '\0';
    }
}

char getAlphabetNumberFromLetter(char c)
{
    return c - 'a';
}

int getBoxIdChecksum(char words[MAX_WORDS][MAX_WORD_LENGTH], int numWords)
{
    int i, j, k;
    int totalDoubles = 0;
    int totalTriples = 0;
    int letterCount[26] = {0};
    int currentLetterIndex;
    int doubles, triples = 0;

    for (i = 0; i < numWords; i++)
    {
        for(k = 0; k < 26; k++){
            letterCount[k] = 0;
        }
        doubles = 0;
        triples = 0;


        for (j = 0; j < strlen(words[i]); j++)
        {
            currentLetterIndex = getAlphabetNumberFromLetter(words[i][j]);
            letterCount[currentLetterIndex]++;
        }

        for (k = 0; k < 26; k++)
        {
            if (doubles == 0 && letterCount[k] == 2)
            {
                doubles = 1;
            }
            else if (triples == 0 && letterCount[k] == 3)
            {
                triples = 1;
            }
        }

        totalDoubles += doubles;
        totalTriples += triples;
    }

    return totalDoubles * totalTriples;
}

int main()
{
    FILE *fp = fopen("day2Input.txt", "r");
    int numWords = 0;
    int checksum;
    char words[MAX_WORDS][MAX_WORD_LENGTH];

    while (!feof(fp))
    {
        fgets(words[numWords], MAX_WORD_LENGTH, fp);
        numWords++;
    }

    checksum = getBoxIdChecksum(words, numWords);

    printf("Checksum : %d\n", checksum);

    return 0;
}