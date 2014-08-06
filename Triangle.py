# Triangle.py
#Question:Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

#For example, given the following triangle
#[
     #[2],
    #[3,4],
   #[6,5,7],
  #[4,1,8,3]
#]
#The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

#Note:
#Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
# Question from: https://oj.leetcode.com/problems/triangle/
# Sulotion:
# Author: DongDing 
# Date: 2014/08/06
# Time complexity:  O(n^2) , n is the number of rows of the  triangle
# space complexity:  O(n^2)  
# Tag:  # Dynamic Programming 
# Comment: 
#[
     #[2],
    #[3,4],
   #[6,5,7],
  #[4,1,8,3]
#]
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        len_t = len(triangle)
        if len_t == 0:
            return 0
        if len_t == 1:
            return triangle[0][0]
        M = [[0 for j in range(i+1)]for i in range(len_t)]
        #print M
        M[0][0] = triangle[0][0]
        for i in range(1,len_t):
            M[i][0] = M[i-1][0] + triangle[i][0]
            M[i][-1] = M[i-1][-1] + triangle[i][-1]            
            for j in range(1,i):
                M[i][j] = triangle[i][j] + min([M[i-1][j-1],M[i-1][j]])
        return min(M[-1])
        
tr = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]        
a = Solution()

print a.minimumTotal(tr)
        
        
        
        
        
