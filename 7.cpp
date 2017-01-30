#include <iostream>
#include <cstdio>
using namespace std;

int reverse(int x) {
        bool symbol = 0;
        long long int ans = 0;
        int out;
        if (x < 0) {
            symbol = 1;
            x = -x;
        }
        while (x != 0) {
            ans = ans * 10 + x % 10;
            x /= 10;
        }
        if (symbol) ans = -ans;
        out = (int)ans;
        if ((long long int)out != ans) return 0;
        else return out;
}

int main() {
    int x;
    cin >> x;
    cout << reverse(x);
    return 0;
}
