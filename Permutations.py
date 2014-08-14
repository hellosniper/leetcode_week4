# Permutations.py
# Question: Given a collection of numbers, return all possible permutations.

#For example,
#[1,2,3] have the following permutations:
#[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
# Question from: https://oj.leetcode.com/problems/Permutations/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/13
# Time complexity:  O(n!)
# space complexity:  O(n!)  
# Tag: # Recursion # Math Problem
# Comment
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        n = len(num)
        if n == 1:
            return [num]
        result = []
        for i in range(n):
            num1 = [digit for digit in num]
            a1 = list([num1.pop(i)])
            a2 = self.permute(num1)
            for j in a2:
                temp = []
                temp.extend(a1)
                temp.extend(j)
                result.append(temp)         
        return result
num = [1,2,3]
a = Solution()
print a.permute(num)
