# Balanced Binary Tree.py

# Question: #Given a binary tree, determine if it is height-balanced.
#For this problem, a height-balanced binary tree is defined as a binary tree 
#in which the depth of the two subtrees of every node never differ by more than 1.
# Question from: https://oj.leetcode.com/problems/balanced-binary-tree/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/25
# Time complexity:  O(n) 
# space complexity:  O(log n)  
# Tag: # Binary Tree  # recursive
# Comment:
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        #if root == None:
            #return True
        if self.checkBalanced(root) == -1:
            return False
        else:
            return True
        
    def checkBalanced(self, root):
        if root == None:
            return 0
        left_height = self.checkBalanced(root.left)
        
        right_height = self.checkBalanced(root.right)
        
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        
        height = max([left_height,right_height]) + 1 
        
        return height
