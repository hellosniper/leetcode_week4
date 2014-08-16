# Sum Root to Leaf Numbers.py
# Question: Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

#An example is the root-to-leaf path 1->2->3 which represents the number 123.

#Find the total sum of all root-to-leaf numbers.

#For example,

    #1
   #/ \
  #2   3
#The root-to-leaf path 1->2 represents the number 12.
#The root-to-leaf path 1->3 represents the number 13.

#Return the sum = 12 + 13 = 25.
# Question from: https://oj.leetcode.com/problems/sum-root-to-leaf-numbers/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/16
# Time complexity:  O(n) n : number of tree nodes
# space complexity:  O(n)  
# Tag: # Tree # DFS # integer
# Comment:
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        
        self.result = 0
        if root == None:
            return 0
        #path = [root.val] # list of integer
        path = []
        self.dfs(root,path)
        return self.result
    # @param node, a tree node
    # @param path, a list of integer
    # @return an integer    
    def dfs(self,node,path):
        if node == None:
            return False
        path.append(node.val)
        left = self.dfs(node.left, path)
        right = self.dfs(node.right, path)
        if not left and not right: # this is the leaf
            sum1 = self.sumPath(path)
            self.result += sum1
        path.pop()
        return True
    # @param path, a list of integer
    # @return an integer
    def sumPath(self,path):
        weight = 1
        result = 0
        for i in range(len(path)-1,-1,-1):
            result += path[i] * weight
            weight *= 10            
        return result
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
path = [1,2,3,4]
a = Solution()
root = None
print a.sumPath(path)+1

print a.sumNumbers(root)
