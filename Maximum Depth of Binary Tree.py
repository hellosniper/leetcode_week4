# Maximum Depth of Binary Tree.py

# Question: Given a binary tree, find its maximum depth.
#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Question from: https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/27
# Time complexity:  O(n) 
# space complexity:  O(lon(n))  
# Tag: # Binary Tree  # recursive # link list
# Comment:


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        list1 = [root]
        result = 0
        while list1:
            result += 1
            nextlevel = self.dfs(list1)            
            list1 = nextlevel
        return result
        
        
        
        
    def dfs(self,level):
        nextlevel = []
        for node in level:
            if node.left:
                nextlevel.append(node.left)
            if node.right:
                nextlevel.append(node.right)
            
        return nextlevel
            
            
