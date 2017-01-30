#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int myAtoi(string str) {
    long long int ans = 0;
    int i = 0;
    int symbol = 1;
    while (str[i] == ' ') {
        i ++;
    }
    if (str[i] == '-') {
        symbol = -1;
        i ++;
    }
    else if (str[i] == '+') {
        i ++;
    }
    while (i < str.size()) {
        if (str[i] < '0' || str[i] > '9') break;
        str[i] = str[i] - '0';
        ans = ans * 10 + str[i];
        if (ans > 2147483648) break;
        i ++;
    }

    ans *= symbol;

    if (ans < -2147483648) return -2147483648;
    else if (ans > (long long int)2147483647) return 2147483647;
    else return ans;
}

int main() {
    string s;
    cin >> s;
    printf("%d\n", myAtoi(s));
}
