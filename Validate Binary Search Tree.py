#Validate Binary Search Tree.py
# Question:#Given a binary tree, determine if it is a valid binary search tree (BST).

#Assume a BST is defined as follows:

#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.

# Question from: https://oj.leetcode.com/problems/validate-binary-search-tree/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/21
# Time complexity:  O(n) 
# space complexity:  O(n)  
# Tag: # Binary Search Tree  # DFS 
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
    def isValidBST(self, root):
        if root == None:
            return True
        self.finished = False
        self.result = True
        self.dfs(root, None)
        #stack1 = []
        #stack1.append(root)
        #while stack1:
        return self.result
            
    #def check(self,node):
        #if node.left:
            #if node.val > 
    
    # @param root, a tree node
    # @return a node that is the last node of the binary search tree            
    def dfs(self,node,pre):
        if node == None:
            return None
        if self.finished:
            return None
        left = self.dfs(node.left,pre)
        if left:
            pre = left
        else:
            pass
        if pre != None:
            if pre.val >= node.val:
                self.result = False
                self.finished = True
            else:
                pass
        if self.finished:
            return None
        right = self.dfs(node.right, node)
        return right if right != None else node
        
        
