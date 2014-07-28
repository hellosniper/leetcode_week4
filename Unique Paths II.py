# Unique Paths II.py
# Question:
#Follow up for "Unique Paths":

#Now consider if some obstacles are added to the grids. How many unique paths would there be?

#An obstacle and empty space is marked as 1 and 0 respectively in the grid.

#For example,
#There is one obstacle in the middle of a 3x3 grid as illustrated below.
# Question from: https://oj.leetcode.com/problems/unique-paths-ii/
# Sulotion:
# Author: DongDing 
# Date: 2014/07/28
# Time complexity:  O(mn) 
# Tag: # Dynamic Programming
# Comment: 
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if n==1 and m==1:
            return 1 if obstacleGrid[0][0] == 0 else 0
            
        Paths = [[1 for j in range(m)] for i in range(n)]
        for j in range(1,m):
            Paths[0][j] = Paths[0][j-1] if obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] ==0 else 0

        for i in range(1,n):
            if obstacleGrid[i][0] == 0:
                Paths[i][0] = Paths[i-1][0] if obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0]==0 else 0 
            else:
                Paths[i][0] = 0
     
        #if n == 1:
            #return Paths[-1]
        #if m == 1:
            #return Paths[-1]
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j] == 1:
                    Paths[i][j] = 0
                else:
                    if obstacleGrid[i-1][j] == 1:
                        path1 = 0
                    else:
                        path1 = Paths[i-1][j]
                    if obstacleGrid[i][j-1] == 1:
                        path2 = 0
                    else:
                        path2 = Paths[i][j-1]
                    Paths[i][j] = path1 + path2

        return Paths[-1][-1]
o = [[0,0]]
a = Solution()
print a.uniquePathsWithObstacles(o)
