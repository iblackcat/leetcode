#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char** fullJustify(char** words, int wordsSize, int maxWidth, int* returnSize) {
    char **returnWords = (char**)malloc(sizeof(char*)*wordsSize);
    *returnSize = 10;
    return returnWords;
}

int main() {
    char w[5][10] = {"hahaha", "hehe", "ei", "oooooooo", "a"};
    int a = 0;
    char **ans = fullJustify((char**)w, 5, 10, &a);
    printf("%d\n", a);
    return 0;
}
