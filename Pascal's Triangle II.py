# Pascal's Triangle II.py

# Question: #Given an index k, return the kth row of the Pascal's triangle.

#For example, given k = 3,
#Return [1,3,3,1].

#Note:
#Could you optimize your algorithm to use only O(k) extra space?
# Question from: https://oj.leetcode.com/problems/pascals-triangle-ii/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/15
# Time complexity:  O(n^2)
# space complexity:  O(n)  
# Tag: # integer
# Comment:
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        
        result = []
        pre = []
        for i in range(1,rowIndex+1):
            len_p = len(pre)
            result = list()
            for j in range(1,len_p):
                result.append(pre[j-1]+pre[j])
            result.append(1)
            result.insert(0, 1)
            pre = result
        return result


r = 5
a = Solution()
print a.getRow(r)
