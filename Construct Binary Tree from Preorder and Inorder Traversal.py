# Construct Binary Tree from Preorder and Inorder Traversal.py

# Question: 
#Given preorder and inorder traversal of a tree, construct the binary tree.

#Note:
#You may assume that duplicates do not exist in the tree.

# Question from: https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/29
# Time complexity:  O(n) 
# space complexity:  O(1)  
# Tag: # Binary Tree  # recursive 
# Comment:


#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if inorder == None or len(inorder) == 0:
            return None

        self.inorder = inorder
        self.preorder = preorder
        n = len(self.inorder)
        return self.digui(0,n-1,0,n-1)
        
    def digui(self,inleft,inright,preleft,preright):
        if preleft > preright:
            return None
        if preleft == preright:
            return TreeNode(self.preorder[preleft])
        root = TreeNode(self.preorder[preleft])
        for i in range(inleft,inright+1):
            if self.preorder[preleft] == self.inorder[i]:
                index = i
                break
        
        root.left = self.digui(inleft, index -1 , preleft +1, preleft+1+index-1-inleft)
        root.right = self.digui(index + 1 , inright,  preleft+1+index-1-inleft+1, preright)
        return root        


preorder = [1,2]
inorder = [1,2]
a = Solution()
a.buildTree(preorder, inorder)
