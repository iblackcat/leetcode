#! D:/Program_Files/Python
#_*_ coding:utf8

import sys

def findMedianSortedArray(nums1, nums2):
    le1 = len(nums1)-1
    le2 = len(nums2)-1
    s1 = 0
    s2 = 0
    l = le1 + le2 + 2
    i = 0
    while l > 2:
        if s1 <= le1 and s2 <= le2 and nums1[s1] < nums2[s2] or s2 > le2:
            s1 += 1
        else :
            s2 += 1
        if s1 <= le1 and s2 <= le2 and nums1[le1] > nums2[le2] or s2 > le2:
            le1 -= 1
        else :
            le2 -= 1
        l -= 2
        i += 2
    ans = 0
    while s1 <= le1:
        ans += nums1[s1]
        s1 += 1
    while s2 <= le2:
        ans += nums2[s2]
        s2 += 1
    if l == 1 or ans & 1 == 0:
        return ans / l
    else:
        return float(ans) / l

nums1 = []
nums2 = [5,7,8,9]
print findMedianSortedArray(nums1,nums2)
