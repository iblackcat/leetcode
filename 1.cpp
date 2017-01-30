#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

typedef struct MY_NODE {
    int num;
    int index;
}my_node;

bool cmp(my_node a, my_node b) {
    return a.num < b.num;
}

int find(int start, int end, int target, my_node array[]) {
    if (end < start) return 0;
    int mid = ((start + end) >> 1);
    if (array[mid].num == target) {
        return array[mid].index + 1;
    }
    else if (array[mid].num < target) {
        return find(mid + 1, end, target, array);
    }
    else return find(start, mid - 1, target, array);
}

vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> ans;
    my_node array[nums.size()];
    ans.clear();
    int index1 = 0, index2 = 0, n = nums.size();
    for (int i = 0; i < n; i ++) {
        array[i].num = nums[i];
        array[i].index = i;
    }
    sort(array, array + n, cmp);
    for (int i = 0; i < n; i ++) {
        index2 = find(i + 1, n, target - array[i].num, array);
        if (index2 != 0) {
            index1 = array[i].index + 1;
            break;
        }
    }
    if (index1 > index2) {
        int t = index2;
        index2 = index1;
        index1 = t;
    }
    ans.push_back(index1);
    ans.push_back(index2);
    return ans;
}

int main() {
    vector<int> nums;
    nums.clear();
    int n, num[1024], target;
    scanf("%d %d", &n, &target);
    for (int i = 0; i < n; i++) {
        scanf("%d", &num[i]);
        nums.push_back(num[i]);
    }
    vector<int> ans =
    twoSum(nums, target);
    cout << ans[0] << " " << ans[1] << endl;
    return 0;
}
