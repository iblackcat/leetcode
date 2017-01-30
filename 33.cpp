#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int my_find(vector<int>& nums, int target, int start, int end) {
    if (start > end || (start == end && nums[start] != target)) return -1;
    int mid = ((start + end) >> 1);
    if (nums[mid] == target) return mid;
    else if (nums[mid] > nums[start] && nums[mid] > target && nums[start] <= target) return my_find(nums, target, start, mid - 1);
    else if (nums[mid] < nums[start] && ((nums[mid] > target && nums[end] > target) || nums[mid] < target && nums[end] < target))
        return my_find(nums, target, start, mid - 1);
    else return my_find(nums, target, mid + 1, end);
}

int search(vector<int>& nums, int target) {
    if (nums.size() == 0) return -1;
    return my_find(nums, target, 0, nums.size() - 1);
}

int main() {
    freopen("33.txt", "r", stdin);
    int n, number, target;
    vector<int> vec;
    vec.clear();
    scanf("%d %d", &n, &target);
    for (int i = 0; i < n; i++) {
        scanf("%d", &number);
        vec.push_back(number);
    }
    printf("%d\n", search(vec, target));
    return 0;
}
