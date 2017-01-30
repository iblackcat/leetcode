class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.maxval = x
        self.fail = None
        self.letter = [0 for i in range(0,26)]

def insert(head, word, success):
    x = head
    for i in word:
        if (x.letter[ord(i)-ord('a')] == 0):
            p = ListNode(0)
            x.letter[ord(i)-ord('a')] = p
        x = x.letter[ord(i)-ord('a')]
    x.val += 1
    x.maxval += 1
    success += x

def reset(success):
    for x in success:
        x.val = x.maxval

def set_fail(head):
    head.fail = head
    queue = [head]
    while (queue != []):
        x = queue[0]
        for i in range(0,26):
            if (x.letter[i] != 0):
                queue += x.letter[i]
                if (x.fail.letter[i] != 0):
                    x.letter[i].fail = x.fail.letter[i]
                else :
                    x.letter[i].fail = head
        if (len(queue) <= 1):
            break
        else:
            x = queue[1:]

def findSubstring(s, words):
    head = ListNode(0)
    success = []
    for i in words:
        insert(head, i, success)
    set_fail(head)

    x = head
    i = 0
    l = len(s)
    while (i < l):
        if (x.letter[ord(s[i])] != 0):
            i += 1
            x = x.letter[ord(s[i])]
            if ()
        else:
            
    return 0

a = ListNode(0)
b = ListNode(2)
a.letter[21] = b
print(a.letter[21].val)
print(ord('z')-ord('a'))
