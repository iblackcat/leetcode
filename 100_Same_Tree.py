class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def isSameTree(p,q):
    if p==None and q==None:
        return True
    elif p==None or q==None:
        return False
    elif ((isSameTree(p.left,q.left) and isSameTree(p.right,q.right)) or (isSameTree(p.left,q.right) and isSameTree(p.right,q.left))) and p.val==q.val:
        return True
    else :
        return False


