#include <cstdio>
#include <cstring>
#include <algorithm>

int candy(int* ratings, int ratingsSize) {
    int head = 0, ans = 0, tag = 0;
    for (int i=0; i<ratingsSize; i++) {
        if (i < ratingsSize-1 && ratings[i+1] < ratings[i]) {
            head++;
        } else {
            for (int j=0; j<head; j++) {
                ans += j+1;
            }
            if (i-head-1 >= 0 && ratings[i-head-1] < ratings[i-head] && tag > head) tag = tag+1;
            else tag = head+1;
            ans += tag;
            if (head) tag = 1;
            head = 0;
        }
    }
    return ans;
}
