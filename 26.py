def removeDuplicates(nums):
    l = len(nums)
    if (l < 2):
        return l
    ans = 1
    for i in range(1,l):
        if (nums[i] != nums[i-1]):
            ans += 1
            nums[ans-1] = nums[i]
    return ans

a = [1,1,2,3,3,4,4,4,4]
print(removeDuplicates(a))
print(a)
