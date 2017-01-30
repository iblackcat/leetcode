#include <cstdio>
#include <cstring>

bool isPalindrome(int x) {
    if (x < 0) x = -x;
    int num = x, len = 0, a = 1;
    while (num != 0) {
        if (num != x) a *= 10;
        num /= 10;
        len ++;
    }
    num = x;
    for (int i = 0; i < (len >> 1); i ++) {
        if (x % 10 != num / a) return 0;
        x /= 10;
        num %= a;
        a /= 10;
    }
    return 1;
}

int main() {
    printf("%d\n", isPalindrome(214724712));
    return 0;
}
