def removeElement(nums, val):
    ans = 0
    l = len(nums)
    for i in range(0,l):
        if (nums[i] != val):
            nums[ans] = nums[i]
            ans += 1
    return ans

a = [3,2,3,4,5,3,3]
print(removeElement(a,3))
print(a)
