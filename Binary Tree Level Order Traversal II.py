# Binary Tree Level Order Traversal II.py
# Question: Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

#For example:
#Given binary tree {3,9,20,#,#,15,7},
    #3
   #/ \
  #9  20
    #/  \
   #15   7
#return its bottom-up level order traversal as:
#[
  #[15,7],
  #[9,20],
  #[3]
#]
# Question from: https://oj.leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/22
# Time complexity:  O(n) 
# space complexity:  O(n)  
# Tag: # Binary Tree  # BFS 
# Comment:

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root == None:
            return []
        self.result = []
        level = [root]
        
        while level:
            nextlevel = self.bfs(level)
            level = nextlevel
            
        return self.result
    
    def bfs(self,level):
        list1 = []
        nextlevel = []
        for node in level:
            list1.append(node.val)
            if node.left:
                nextlevel.append(node.left)
            if node.right:
                nextlevel.append(node.right)
        self.result.insert(0,list1)        
        return nextlevel
            
            
        
