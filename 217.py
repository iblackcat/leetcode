#! D:/Program_Files/Python
#_*_ coding: utf8

import math
import sys

def partition(A, start, end):
    x = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j]<=x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[end] = A[end],A[i+1]
    return i+1

def quick_sort(A, start, end):
    if start < end:
        q = partition(A, start, end)
        quick_sort(A, start, q-1)
        quick_sort(A, q+1, end)

def containsDuplicate(nums):
#    quick_sort(nums, 0, len(nums) - 1)
#    for i in range(1, len(nums) - 1):
#        if nums[i]==nums[i-1]:
#            return True
#    return False
    d = dict()
    le = len(nums)
    i = 0
    while i<le:
        if nums[i] in d:
            return True
        else:
            d[nums[i]] = 1
            i += 1
    return False

nums = [1,0,2,-2,0,5]
print containsDuplicate(nums)
    
