# Binary Tree Level Order Traversal.py

# Question:Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

#For example:
#Given binary tree {3,9,20,#,#,15,7},
    #3
   #/ \
  #9  20
    #/  \
   #15   7
#return its level order traversal as:
#[
  #[3],
  #[9,20],
  #[15,7]
#]

# Question from: https://oj.leetcode.com/problems/binary-tree-level-order-traversal/
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
    def levelOrder(self, root):
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
        self.result.append(list1)        
        return nextlevel
            
            
        
