# Construct Binary Tree from Inorder and Postorder Traversal.py

# Question: Given inorder and postorder traversal of a tree, construct the binary tree.
#Note:
#You may assume that duplicates do not exist in the tree.
# Question from: https://oj.leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/29
# Time complexity:  O(n) 
# space complexity:  O(1)  
# Tag: # Binary Tree  # recursive 
# Comment:


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if inorder == None or len(inorder) == 0:
            return None

        self.inorder = inorder
        self.postorder = postorder
        n = len(self.inorder)
        return self.digui(0,n-1,0,n-1)
        
    def digui(self,inleft,inright,postleft,postright):
        if postleft > postright:
            return None
        if postleft == postright:
            return TreeNode(self.postorder[postright])
        root = TreeNode(self.postorder[postright])
        for i in range(inleft,inright+1):
            if self.postorder[postright] == self.inorder[i]:
                index = i
                break
        
        root.left = self.digui(inleft, index -1 , postleft, postleft+index-1-inleft)
        root.right = self.digui(index + 1 , inright, postleft+index-inleft, postright-1)
        return root
