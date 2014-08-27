# Convert Sorted List to Binary Search Tree.py

# Question: #Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# Question from: https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
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
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head == None:
            return None
        self.num = []
        pointer = head
        while pointer:
            self.num.append(pointer.val)
            pointer = pointer.next
            
        n = len(self.num)
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
