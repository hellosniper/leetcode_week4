# Convert Sorted Array to Binary Search Tree.py

# Question:Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# Question from: https://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/25
# Time complexity:  O(n) 
# space complexity:  O(log n)  
# Tag: # Binary Tree  # recursive # Array
# Comment:



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if num == None or len(num) == 0:
            return None
        n = len(num)
        self.num = num
        return self.creatTree(0,n-1)
        
    def creatTree(self, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(self.num[start])
        
        m = (end + start)/2  # median
        
        head = TreeNode(self.num[m])
        head.left = self.creatTree(start, m-1)
        head.right = self.creatTree(m+1, end)
        
        return head
