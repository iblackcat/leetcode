def sort(nums, s, t):
    print(nums[s:t])
    if (t - s > 1):
        for i in range(s,t-1):
            j = t-1
            while (j > i):
                if (nums[j]<nums[j-1]):
                    tmp = nums[j]
                    nums[j] = nums[j-1]
                    nums[j-1] = tmp
                j -= 1
    print(nums[s:t])

def nextPermutation(nums):
    l = len(nums)
    i = l-2
    tag = 0
    mi = 0
    loc = 0
    while (i >= 0):
        tag = 0
        for j in range(i+1,l):
            if (tag == 0 and nums[j] > nums[i]):
                mi = nums[j]
                loc = j
                tag = 1
            elif (tag == 1 and nums[j] > nums[i] and nums[j] < mi):
                mi = nums[j]
                loc = j
        if (tag == 1):
            nums[loc] = nums[i]
            nums[i] = mi
            sort(nums,i+1,l)
            break
        i -= 1
    if (tag == 0):
        for i in range(0,(l>>1)):
            mi = nums[i]
            nums[i] = nums[l-i-1]
            nums[l-i-1] = mi

a = [5,4,3,2,3,4,2]
nextPermutation(a)
print(a)
