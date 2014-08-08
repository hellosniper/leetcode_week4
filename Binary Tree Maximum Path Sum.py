# Binary Tree Maximum Path Sum.py


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @param root, a tree node
    # @return an integer
    # self.result = 0
    def maxPathSum(self, root):
        if root == None:
            return 0
        self.result = root.val
        self.findMax(root)
        return self.result
        
        
    def findMax(self, root):
    # return the max path sum of the current node
        if root == None:
            return 0
        lmax = self.findMax(root.left)
        rmax = self.findMax(root.right)
        cmax = root.val
        if (lmax + rmax + cmax)>self.result:
            self.result = lmax + rmax + cmax
        lmax = cmax + lmax
        rmax = cmax + rmax
        cmax = max([cmax,lmax])
        cmax = max([cmax,rmax]) 
        # cmax = lmax if lmax > cmax else cmax
        # cmax = rmax if rmax > cmax else cmax
        #cmax = root.val + max([self.flen(root.left),0]) + max([self.flen(root.right),0])
        if (cmax > self.result):
            self.result = cmax
        return cmax

root=  TreeNode(-2)
left = TreeNode(1)
root.left = left
a = Solution()
print a.maxPathSum(root)        
    
    # def flen(self, root):
    # # return the max path from root to a curtern node
        # if root == None:
            # return 0
        # lmax = self.flen(root.left)
        # rmax = self.flen(root.right)
        # if lmax <=0 and rmax <=0:
            # return root.val
        # elif lmax > 0 and lmax >= rmax:
            # return root.val +lmax
        # elif rmax > 0 and rmax >= lmax:
            # return root.val +rmax

# class Solution:
    # # @param root, a tree node
    # # @return an integer
    # self.result = 0
    # def maxPathSum(self, root):
        # if root == None:
            # return 0
        # self.result = root.val
        # self.result = self.findMax(root)
        # return self.result
        
        
    # def findMax(self, root):
    # # return the max path sum of the current node
        # if root == None:
            # return 0
        # lmax = self.findMax(root.left)
        # rmax = self.findMax(root.right)
        # cmax = root.val + max([self.flen(root.left),0]) + max([self.flen(root.right),0])
        # return max([lmax,rmax,cmax])
        
    
    # def flen(self, root):
    # # return the max path from root to a curtern node
        # if root == None:
            # return 0
        # lmax = self.flen(root.left)
        # rmax = self.flen(root.right)
        # if lmax <=0 and rmax <=0:
            # return root.val
        # elif lmax > 0 and lmax >= rmax:
            # return root.val +lmax
        # elif rmax > 0 and rmax >= lmax:
            # return root.val +rmax
