#! D:/Program_Fils/Python
#_*_ coding:utf8

import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    last = None
    p = None
    while head != None:
        p = head.next
        head.next = last
        last = head
        head = p
    return last

p = ListNode(1)
p.next = ListNode(2)
p.next.next = ListNode(3)

p = reverseList(p)
k = p.next
l = k.next
print p.val,k.val,l.val
