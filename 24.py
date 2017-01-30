class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    x = head
    pre = None
    while (x != None):
        if (x.next == None):
            break
        if (pre == None):
            head = x.next
            x.next = head.next
            head.next = x
        else :
            pre.next = x.next
            x.next = pre.next.next
            pre.next.next = x
        pre = x
        x = x.next
    return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)

a.next = b
b.next = c
c.next = d
d.next = e
#e.next = f

a = swapPairs(a)
while (a!=None):
    print(a.val)
    a = a.next
