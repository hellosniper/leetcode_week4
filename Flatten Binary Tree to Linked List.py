# Flatten Binary Tree to Linked List.py
# Question: #Given a binary tree, flatten it to a linked list in-place.

#For example,
#Given

         #1
        #/ \
       #2   5
      #/ \   \
     #3   4   6
#The flattened tree should look like:
   #1
    #\
     #2
      #\
       #3
        #\
         #4
          #\
           #5
            #\
             #6
# Question from: https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/25
# Time complexity:  O(n) 
# space complexity:  O(1)  
# Tag: # Binary Tree  # preoder DFS 
# Comment:

             
#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x,left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root == None:
            return
        stack1 = [] #only store the unvisted right
        
        flag = 1 # 1: to child, 2: to parent
        
        #stack1.append(root)
        this = root
        new = None
        while this or stack1:
            # 
            if this == None:
                this = stack1.pop()
            if this.right:
                stack1.append(this.right)
                this.right = None
            # 
            temp = this.left
            this.left = None
            #reshape in place
            if new == None:
                new = this
            else:
                new.right = this
                new = this
            
            this = temp
            
root = TreeNode(1,TreeNode(2),None)
a= Solution()
a.flatten(root)
