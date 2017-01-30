class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printf(array):
    for i in array:
        print(i.val)

def insert(queue, i):
    print("(1)")
    printf(queue)
    if (queue == []):
        queue += [i]
    elif (queue[0].val > i.val):
        queue = [i]+queue
    elif (queue[len(queue)-1].val <= i.val):
        queue += [i]
    else :
        mid = (len(queue)>>1)
        if (queue[mid].val > i.val):
            q = insert(queue[:mid],i)
            queue = q+queue[mid:]
        else :
            q = insert(queue[mid+1:],i)
            queue = queue[:mid+1]+q
    print("(2)")
    printf(queue)
    return queue

def mergeKLists(lists):
    queue = []
    ans = ListNode(0)
    rear = ans
    for i in lists:
        if (i != None):
            queue += [i]
    queue = sorted(queue,lambda a,b:a.val-b.val)
    while (queue != []):
        if (len(queue) == 1) :
            rear.next = queue[0]
            break
        i = queue[0]
        while (i!=None and (len(queue)==1 or i.val<=queue[1].val)):
            p = i.next
            i.next = None
            rear.next = i
            rear = i
            i = p
        queue = queue[1:]
        if (i != None):
            queue = insert(queue,i)
    return ans.next

a = ListNode(-1)
b = ListNode(1)
c = ListNode(-3)
d = ListNode(1)
e = ListNode(4)
f = ListNode(-2)
g = ListNode(-2)
h = ListNode(-1)
i = ListNode(0)
j = ListNode(2)
a.next = b
c.next = d
d.next = e
f.next = h
h.next = i
qq = [a,c,g,f,j]
ans = mergeKLists(qq)
print("")
while (ans != None):
    print(ans.val)
    ans = ans.next
