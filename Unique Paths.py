# Unique Paths.py
# Question:A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

#How many possible unique paths are there?
# Question from: https://oj.leetcode.com/problems/unique-paths/
# Sulotion:
# Author: DongDing 
# Date: 2014/07/28
# Time complexity:  O(mn) 
# Tag: # Dynamic Programming
# Comment: 
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        Paths = [[1 for j in range(m)] for i in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                Paths[i][j] = Paths[i-1][j]+Paths[i][j-1]
        return Paths[-1][-1]

a = Solution()
print a.uniquePaths(3, 3)
