class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseKGroup(head, k):
    if (k<2):
        return head

    x = head
    pre = None
    while (x != None):
        y = x
        for i in range(1,k):
            y = y.next
            if (y == None):
                return head
        r = x
        if (pre == None):
            head = y
        else :
            pre.next = y
        p = x.next
        q = p.next
        x.next = y.next
        for i in range(2,k):
            p.next = r
            r = p
            p = q
            q = q.next
        y.next = r
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
e.next = f

a = reverseKGroup(a,7)
while (a!=None):
    print(a.val)
    a = a.next
