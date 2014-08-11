# Pascal's Triangle.py
#Given numRows, generate the first numRows of Pascal's triangle.

#For example, given numRows = 5,
#Return
#[
     #[1],
    #[1,1],
   #[1,2,1],
  #[1,3,3,1],
 #[1,4,6,4,1]
#]
      
# Question from: https://oj.leetcode.com/problems/pascals-triangle/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/10
# Time complexity:  O(numRows^2)
# space complexity:  O(numRows^2)  
# Tag: # Dynamic Programming # integer
# Comment: 

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        result = list()
        for i in range(numRows):
            row = [1 for j in range(i+1)]
            for j in range(1,i):
                row[j] = result[-1][j] + result[-1][j-1]
            result.append(row)
        return result
a = Solution()
print a.generate(5)
