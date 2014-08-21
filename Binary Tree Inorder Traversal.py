# Binary Tree Inorder Traversal.py
# Question: Given a binary tree, return the inorder traversal of its nodes' values.
#For example:
#Given binary tree {1,#,2,3},
   #1
    #\
     #2
    #/
   #3
#return [1,3,2].
# Question from: https://oj.leetcode.com/problems/binary-tree-inorder-traversal/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/21
# Time complexity:  O(n) 
# space complexity:  O(n)  
# Tag: # Binary Tree  # DFS 
# Comment:

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root == None:
            return []
        result = []
        queue = []
        queue.append(root)
        visited1 = {}
        while queue:
            node1 = queue[-1]
            if node1.left != None and visited1.get(node1.left) != True:
                queue.append(node1.left)
                continue
            else:
                visited1.update({node1:True})
                queue.pop()
                result.append(node1.val)
                if node1.right != None:
                    queue.append(node1.right)
                    
        return result
            
            
        
        
