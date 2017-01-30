class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def buildList(nums):
    if len(nums) == 0:
        return None
    l = ListNode(nums[0])
    ans = l
    for i in range(1, len(nums)):
        k = ListNode(nums[i])
        l.next = k
        l = k
    return ans

def mergeTwoLists(l1, l2):
    if l1 == None and l2 == None:
        return None
    if (l1 != None and l2 != None and l1.val < l2.val) or l2 == None:
        ans = l1
        l1 = l1.next
    else:
        ans = l2
        l2 = l2.next
    a = ans
    while l1 != None and l2 != None:
        if l1.val < l2.val:
            ans.next = l1
            ans = ans.next
            l1 = l1.next
        else :
            ans.next = l2
            ans = ans.next
            l2 = l2.next
    if l1 == None and ans != None:
        ans.next = l2
    else :
        if ans != None:
            ans.next = l1
    l1 = a
    l2 = a
    return a


nums1 = []
nums2 = []
l1 = buildList(nums1)
l2 = buildList(nums2)
l = mergeTwoLists(l1, l2)
while l != None:
    print l.val
    l = l.next
