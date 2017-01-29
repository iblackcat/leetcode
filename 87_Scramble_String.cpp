#include <stdio.h>
#include <string.h>
#include <malloc.h>

int len;

bool judge(int st1, int en1, int st2, int en2, char* s1, char* s2, short* dp) {
    if (dp[st1*(len*len*len)+en1*(len*len)+st2*len+en2] != -1) {
        //printf(" - f(%d,%d,%d,%d) = %d\n", st1, en1, st2, en2, dp[st1*(len*len*len)+en1*(len*len)+st2*len+en2] > 0);
        return dp[st1*(len*len*len)+en1*(len*len)+st2*len+en2] > 0;
    }
    if (st1 == en1) {
        dp[st1*(len*len*len)+en1*(len*len)+st2*len+en2] = short(s1[st1] == s2[st2]);
        //printf(" ! f(%d,%d,%d,%d) = %d\n", st1, en1, st2, en2, dp[st1*(len*len*len)+en1*(len*len)+st2*len+en2] > 0);
        return s1[st1] == s2[st2];
    }
    for (int i=0; i<en1-st1; i++) {
        if (judge(st1, st1+i, st2, st2+i, s1, s2, dp) && judge(st1+i+1, en1, st2+i+1, en2, s1, s2, dp)) {
            dp[st1*(len*len*len)+en1*(len*len)+st2*len+en2] = 1;
            //printf("f(%d,%d,%d,%d) = %d\n", st1, en1, st2, en2, dp[st1*(len*len*len)+en1*(len*len)+st2*len+en2] > 0);
            return true;
        }
        if (judge(st1, st1+i, en2-i, en2, s1, s2, dp) && judge(st1+i+1, en1, st2, en2-i-1, s1, s2, dp)) {
            dp[st1*(len*len*len)+en1*(len*len)+st2*len+en2] = 1;
            //printf("f(%d,%d,%d,%d) = %d\n", st1, en1, st2, en2, dp[st1*(len*len*len)+en1*(len*len)+st2*len+en2] > 0);
            return true;
        }
    }
    //printf("f(%d,%d,%d,%d) = %d\n", st1, en1, st2, en2, dp[st1*(len*len*len)+en1*(len*len)+st2*len+en2] > 0);
    return false;
}

bool isScramble(char* s1, char* s2) {
    len = strlen(s1);
    short *dp = (short*)malloc(sizeof(short)*len*len*len*len);

    memset(dp, -1, sizeof(short)*len*len*len*len);
    return judge(0,len-1,0,len-1,s1,s2,dp);
}

int main() {
    char s1[1024] = "greateat";
    char s2[1024] = "ategrate";
    printf("%d\n",isScramble(s1,s2));
    return 0;
}
