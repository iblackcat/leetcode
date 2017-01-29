#include <stdio.h>
#include <string.h>
#include <malloc.h>
#include <stdlib.h>

bool isInterleave(char* s1, char* s2, char* s3) {
    int len1 = strlen(s1);
    int len2 = strlen(s2);
    int len3 = strlen(s3);
    if (len3 != len1+len2) return false;
    bool *dp = (bool*)malloc(sizeof(bool)*(len1+1)*(len2+1));
    memset(dp, 0, sizeof(bool)*(len1+1)*(len2+1));
    dp[0] = true;
    for (int i=1; i<=len1; i++) {
        if (s1[i-1] == s3[i-1]) dp[i*(len2+1)] = true;
        else break;
    }
    for (int i=1; i<=len2; i++) {
        if (s2[i-1] == s3[i-1]) dp[i] = true;
        else break;
    }
    for (int i=1; i<=len1; i++) {
        for (int j=1; j<=len2; j++) {
            dp[i*(len2+1)+j] = (dp[(i-1)*(len2+1)+j] && s1[i-1]==s3[i+j-1]) || (dp[i*(len2+1)+j-1] && s2[j-1]==s3[i+j-1]);
        }
    }
    return dp[len1*(len2+1)+len2];
}

int main() {
    char s1[1024] = "z";
    char s2[1024] = "dbbca";
    char s3[1024] = "zdbbca";
    char s4[1024] = "aadbbbaccc";
    printf("%d\n%d\n",isInterleave(s1,s2,s3), isInterleave(s1,s2,s4));
    return 0;
}
