#include <cstdio>
#include <algorithm>
#include <iostream>
#include <map>
using namespace std;

map<char, int> m;

int lengthOfLongestSubstring(string s) {
    int start = 0, end = 0, ans = 1, location = 0;
    m.clear();
    m.insert(pair <char, int> (s[0], 0));
    for (int i = 1; i < s.size(); i ++) {
        if (m.find(s[i]) == m.end()) {
            m.insert(pair <char, int> (s[i], i));
            end = i;
        }
        else {
            location = m[s[i]];
            for (int j = start; j <= location; j++) {
                m.erase(s[j]);
            }
            m.insert(pair <char, int> (s[i], i));
            start = location + 1;
            end = i;
        }
        if (end - start + 1 > ans) ans = end - start + 1;
    }
    return ans;
}

int main() {
    string s;
    cin >> s;
    printf("%d\n", lengthOfLongestSubstring(s));
}
