# Minimum Path Sum.py
# Question: Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
# Question from: https://oj.leetcode.com/problems/minimum-path-sum/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/11
# Time complexity:  O(mn)
# space complexity:  O(mn)  
# Tag: # Dynimic Programming #
# Comment

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if len(grid) == 0:
            return 0
        
        sum1 = [[0 for j in range(len(grid[0]))] for j in range(len(grid))]
        sum1[0][0] = grid[0][0]
        for j in range(1, len(grid[0])):
            sum1[0][j] = sum1[0][j-1] + grid[0][j]
        for i in range(1,len(grid)):
            sum1[i][0] = sum1[i-1][0] + grid[i][0]
            
        for i in range(1,len(grid)):
            for j in range(1, len(grid[0])):
                sum1[i][j] = min([sum1[i][j-1] + grid[i][j], sum1[i-1][j] + grid[i][j]])
        return sum1[-1][-1]     
