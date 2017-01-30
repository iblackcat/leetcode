#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int searchInsert(vector<int>& nums, int target) {
    int start = 0, end = nums.size() - 1, mid;
    while (start <= end) {
        mid = start + end >> 1;
        if (nums[mid] == target) return mid;
        else if (nums[mid] > target) end = mid - 1;
        else start = mid + 1;
    }
    return start;
}

int main() {
    freopen("35.txt", "r", stdin);
    vector<int> nums;
    nums.clear();
    int n, a, k;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i ++) {
        scanf("%d", &a);
        nums.push_back(a);
    }
    printf("%d\n", searchInsert(nums, k));
    return 0;
}
