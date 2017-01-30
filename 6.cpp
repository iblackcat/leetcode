#include <iostream>
#include <cstring>
using namespace std;

string convert(string s, int numRows) {
    string ans = s;

    if (numRows == 1) return ans;

    int before = (numRows << 1) - 2, after = 0;
    int ans_num = 0, s_num;
    for (int i = 0; i < numRows; i ++) {
        s_num = i;
        while (s_num < s.length() && ans_num < s.length()) {
            ans[ans_num++] = s[s_num];
            s_num += before;
            if (before && after && s_num < s.length() && ans_num < s.length()) ans[ans_num++] = s[s_num];
            s_num += after;
        }
        before -= 2;
        after += 2;
    }
    return ans;
}

int main() {
    string s;
    int numRows;
    cin >> s >> numRows;
    cout << convert(s, numRows);
    return 0;
}
