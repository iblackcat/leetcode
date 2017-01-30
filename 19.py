class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    l = 0
    x = head
    while (x != None):
        l += 1
        x = x.next
    if (l == 0):
        return None
    if (n < 1 or n > l):
        return head
    
    target = l - n + 1
    if (target == 1):
        x = head
        head = head.next
        del(x)
        return head
    x = head
    for i in range(1,target-1):
        x = x.next
    p = x.next
    x.next = p.next
    del(p)
    return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
#b.next = c
#a.next = b

a = removeNthFromEnd(a, 0)
while (a != None):
    print(a.val)
    a = a.next
