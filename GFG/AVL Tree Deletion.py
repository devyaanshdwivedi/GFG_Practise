def height(root):
    if not root:
        return 0
    return root.height
    
def update_height(root):
    root.height= 1+max(height(root.left),height(root.right))
    
def balance_factor(root):
    if not root:
        return 0
    return height(root.left)-height(root.right)
    
def rotate_right(root):
    x=root.left
    t2=x.right
    x.right=root
    root.left=t2
    update_height(root)
    update_height(x)
    return x
    
def rotate_left(root):
    x=root.right
    t2=x.left
    x.left=root
    root.right=t2
    update_height(root)
    update_height(x)
    return x
    
def rebalance(root):
    update_height(root)
    balance=balance_factor(root)
    if balance>1:
        if balance_factor(root.left)<0:
            root.left=rotate_left(root.left)
        return rotate_right(root)
    elif balance<-1:
        if balance_factor(root.right)>0:
            root.right=rotate_right(root.right)
        return rotate_left(root)
    return root

def inorder_successor(root):
    while root.left:
        root=root.left
    return root.data

def deleteNode(root, key):
    if not root:
        return root
    if root.data<key:
        root.right=deleteNode(root.right,key)
    elif root.data>key:
        root.left=deleteNode(root.left,key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            root.data=inorder_successor(root.right)
            root.right=deleteNode(root.right,root.data)
    root=rebalance(root)
    return root
