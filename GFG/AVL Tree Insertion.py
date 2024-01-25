#User function Template for python3

''' structure of tree node:

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''

class Solution:
    def height(self,node):
        return node.height if node else 0
        
    def right_rotation(self,node):
        x=node
        y=node.left
        y_r=y.right
        y.right=x
        x.left=y_r
        x.height=1+max(self.height(x.left),self.height(x.right))
        y.height=1+max(self.height(y.left),self.height(y.right))
        return y
        
    def left_rotation(self,node):
        x=node
        y=node.right
        y_l=y.left
        y.left=x
        x.right=y_l
        x.height=self.height(x)
        x.height=1+max(self.height(x.left),self.height(x.right))
        y.height=1+max(self.height(y.left),self.height(y.right))
        return y
        

    def insertToAVL(self, node, key):
        if node is None:
            return Node(key)
        if node.data>key:
            node.left=self.insertToAVL(node.left,key)
        else:
            node.right=self.insertToAVL(node.right,key)
            
        node.height=1+max(self.height(node.left),self.height(node.right))
        
        diff=self.height(node.left)-self.height(node.right)
        
        if diff>1:
            if key>node.left.data:
                node.left=self.left_rotation(node.left)
            return self.right_rotation(node)
        elif diff<-1:
            if key<node.right.data:
                node.right=self.right_rotation(node.right)
            return self.left_rotation(node)
        return node
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

def isBST(n, lower, upper):
    if not n:
        return True
    
    if n.data <= lower or n.data >= upper:
        return False
    
    return isBST(n.left, lower, n.data) and isBST(n.right, n.data, upper)

def isBalanced(n):
    if not n:
        return (0,True)
    
    lHeight, l = isBalanced(n.left)
    rHeight, r = isBalanced(n.right)
    
    if abs( lHeight - rHeight ) > 1:
        return (0, False)
    
    return ( 1 + max( lHeight,rHeight  ) , l and r )

def isBalancedBST(root):
    if not isBST(root, -1000000000, 1000000000):
        print("BST voilated, inorder traversal :", end=' ')
    
    elif not isBalanced(root)[1]:
        print("Unbalanced BST, inorder traversal :", end=' ')
    
    else:
        return True
    
    return False

def printInorder(n):
    if not n:
        return
    printInorder(n.left)
    print(n.data, end=' ')
    printInorder(n.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        ip = [ int(x) for x in input().strip().split() ]
        
        root = None
        
        for i in range(n):
            root = Solution().insertToAVL( root, ip[i] )
            
            if not isBalancedBST( root ):
                break
        
        printInorder(root)
        print()

# } Driver Code Ends