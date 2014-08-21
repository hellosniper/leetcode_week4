# Minimum Depth of Binary Tree.py
# Question: Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Question from: https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/21
# Time complexity:  O(n) 
# space complexity:  O(n)  
# Tag: # Binary Tree  # BFS 
# Comment:
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x,left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0        
        self.result = 0
        self.finished = False
        level = [root]
        while level:
            nextlevel = self.bfs(level)
            if self.finished:
                break
            level = nextlevel
            
        return self.result
            
    def bfs(self,level):
        nextlevel = []
        self.result += 1
        for node in level:
            if node.left == None and node.right == None:
                self.finished = True
                return
            if node.left != None:
                nextlevel.append(node.left)
            if node.right != None:
                nextlevel.append(node.right)
                
        return nextlevel
            

root1 = TreeNode(1,TreeNode(3),TreeNode(2,TreeNode(4,None,TreeNode(5)),None))
#root1 = TreeNode(1,TreeNode(5),None)
root1 = None
a = Solution()
print a.minDepth(root1)
        
        
        
