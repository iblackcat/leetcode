def firstMissingPositive(nums):
    f = [0]*1000000
    l = len(nums)
    for i in range(0, l):
        if (nums[i] >= 0 and nums[i] < 1000000):
            f[nums[i]] = 1
    i = 1
    while (f[i] == 1):
        i += 1
    return i

#c code accapt
#int firstMissingPositive(int* nums, int numsSize) {
#    bool tag[100000];
#    int k = 1;
#    for (int i = 0; i < numsSize; i++) {
#        if (nums[i] > 0 && nums[i] < 100000) {
#            tag[nums[i]] = 1;
#        }
#    }
#    while (tag[k] == 1) k++;
#    return k;
#}

print firstMissingPositive([1,2,0])
print firstMissingPositive([3,4,-1,1])
