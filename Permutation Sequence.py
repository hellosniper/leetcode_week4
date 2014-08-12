# Permutation Sequence.py
# Question: The set [1,2,3,…,n] contains a total of n! unique permutations.
#By listing and labeling all of the permutations in order,
#We get the following sequence (ie, for n = 3):
#"123"
#"132"
#"213"
#"231"
#"312"
#"321"
#Given n and k, return the kth permutation sequence.
#Note: Given n will be between 1 and 9 inclusive.
# Question from: https://oj.leetcode.com/problems/permutation-sequence/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/12
# Time complexity:  O(n)
# space complexity:  O(n)  
# Tag: # Recursion # Math Problem
# Comment

class Solution:
    # @return a string
    def getPermutation(self, n, k):        
        num = [str(i+1) for i in range(n)] # 1<=n<=9
        return ''.join(self.compute(num, k))
    
        
    # @input a list of digit and the index of the permutation
    # @return a list of digit in the curtern order    
    def compute(self,num,k):
        n = len(num)
        if n == 1:
            return num
        elif n == 2:
            if k == 1:
                return num
            elif k == 2:
                num.reverse()
                return num
        # n>=3
        divisor = self.factorial(n-1)
        index = (k-1)/divisor
        k = k % divisor
        if k == 0:
            k = divisor
        a1 = list(num.pop(index))
        a2 = self.compute(num, k)
        a1.extend(a2)
        return a1
    def factorial(self, n):
        if n == 1 or n == 0:
            return 1
        return n*self.factorial(n-1)

a = Solution()
print a.getPermutation(4, 6)
