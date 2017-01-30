#include <stdio.h>
#include <string.h>
#include <malloc.h>

int numDistinct(char* s, char* t) {
    int lens = strlen(s);
    int lent = strlen(t);
    if (lens == 0 || lent == 0) return 0;
    int *dp = (int*)malloc(sizeof(int)*(lens)*(lent));
    memset(dp, 0, sizeof(int)*lens*lent);
    dp[0] = (int)(s[0] == t[0]);
    for (int i=1; i<lens; i++) {
        dp[i] = dp[i-1] + (int)(s[i] == t[0]);
    }
    for (int i=1; i<lent; i++) {
        for (int j=i; j<=(lens-lent+i); j++) {
            dp[i*lens+j] = dp[(i-1)*lens+j-1]*(t[i]==s[j]) + dp[i*lens+j-1];
        }
    }
    return dp[(lent-1)*lens+lens-1];
}
/*
0123456
rabbbit
rabbit
0 0 = 1
1 1 = 1
2 2 = 1
3 2 = 2
4 2 = 3
5 2 = 3
6 2 = 3
3 3 = 1
4 3 = 3
5 3 = 3
6 3 = 3
4 4 = 0
5 4 = 3
6 4 = 3
5 5 = 0
6 5 = 3
*/

int main() {
    char s[1024] = "rabbbit";
    char t[1024] = "rabbit";
    printf("%d\n", numDistinct(s,t));
    return 0;
}
