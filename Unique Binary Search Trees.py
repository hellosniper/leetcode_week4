# Unique Binary Search Trees.py

# Question: Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

#For example,
#Given n = 3, there are a total of 5 unique BST's.    
# Question from: https://oj.leetcode.com/problems/unique-binary-search-trees/
# Sulotion:  f(n)=C(2n,n)/(n+1) (n=0,1,2,...)   
# Author: DongDing 
# Date: 2014/08/10
# Time complexity:  O(n)
# space complexity:  O(1)  
# Tag: # Binary Search Tree
# Comment: 
class Solution:
    # @return an integer
    def numTrees(self, n):
        result = 1
        for i in range(n+1, 2*n+1):
            result *= i
        for i in range(1,n+1):
            result /= i
        return result/(n+1)
    
a = Solution()

print a.numTrees(2) 
