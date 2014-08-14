# Permutations II.py
# Question:Given a collection of numbers that might contain duplicates, return all possible unique permutations.

#For example,
#[1,1,2] have the following unique permutations:
#[1,1,2], [1,2,1], and [2,1,1].
# Question from: https://oj.leetcode.com/problems/Permutations II/
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
    def permuteUnique(self, num):
        num = self.bubbleSort(num)
        return self.compute(num)
    def compute(self,num):    
        n = len(num)
        if n == 1:
            return [num]
        result = []
        pre = num[0] - 1
        for i in range(n):
            if num[i] == pre:
                continue
            num1 = [digit for digit in num]
            a1 = list([num1.pop(i)])
            a2 = self.compute(num1)
            for j in a2:
                temp = []
                temp.extend(a1)
                temp.extend(j)
                result.append(temp)   
            pre = num[i]
        return result        
    def bubbleSort(self,num):

        n = len(num)
        for i in range(n-1):
            swapped = False
            for j in range(n-1,0,-1):
                if num[j]<num[j-1]:
                    temp = num[j]
                    num[j] = num[j-1]
                    num[j-1] = temp
                    swapped = True
            if not swapped:
                break        
        return num
num = [1,1,2,2]
a = Solution()
print a.permuteUnique(num)
