# Recover Binary Search Tree.py
# Question:Two elements of a binary search tree (BST) are swapped by mistake.
#Recover the tree without changing its structure.
#Note:
#A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

# Question from: https://oj.leetcode.com/problems/recover-binary-search-tree/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/21
# Time complexity:  O(n) 
# space complexity:  O(1)  
# Tag: # Binary Search Tree  # DFS 
# Comment:
#Definition for a  binary tree node
class TreeNode:
    def __init__(self,x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        if root == None:
            return None
        self.first = None # store the first that are reversed
        self.second = None # store the second that are reversed
        #self.isOver = False        
        #self.list1 = []
        self.reverse(root,None)
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp
        return root
        
    def reverse(self,root, pre):
        if root == None:
            return None
        left = self.reverse(root.left, pre)
        pre = left if left != None else pre
        if pre != None and root.val < pre.val:
            if self.first == None:
                self.first = pre
                self.second = root  
            else:
                self.second = root         
        right = self.reverse(root.right, root)
        return right if right != None else root
a = Solution()
root = TreeNode(2,TreeNode(3),TreeNode(1))
a.recoverTree(root)
