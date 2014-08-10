# Unique Binary Search Trees II.py

# Question: Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
#For example,
#Given n = 3, your program should return all 5 unique BST's shown below.        
# Question from: https://oj.leetcode.com/problems/candy/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/10
# Time complexity:  O(n^3)
# space complexity:  O(1)  
# Tag: # Binary Search Tree # recursive 
# Comment: 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.subTree(1,n)
    
    def subTree(self,start,end):
    # @return a list of tree node        
        if start > end:
            result = [None]
        elif start == end:
            result = [TreeNode(start)]
        
        else:
            result = []
            for i in range(start,end+1):
                left_tree = self.subTree(start, i-1)
                right_tree = self.subTree(i+1, end)
                for j in range(len(left_tree)):
                    for k in range(len(right_tree)):                
                        new_tree = TreeNode(i)
                        new_tree.left = left_tree[j]
                        new_tree.right = right_tree[k]
                        result.append(new_tree)                                        
        return result
          
