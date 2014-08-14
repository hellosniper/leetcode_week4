# Next Permutation.py

# Question:Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

#If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

#The replacement must be in-place, do not allocate extra memory.

#Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#1,2,3 → 1,3,2
#3,2,1 → 1,2,3
#1,1,5 → 1,5,1
# Question from: https://oj.leetcode.com/problems/Next Permutation/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/13
# Time complexity:  O(n^2)
# space complexity:  O(1)  
# Tag: # Recursion # Math Problem
# Comment

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        n = len(num)
        # for right to left  , find the one that num[i]>num[i+1] 
        existed = False
        for i in range(n-1,0,-1):
            if num[i] > num[i-1]:
                d = i-1
                existed = True
                break
        if not existed:
            num.reverse()
            return num
        existed = False
        for increase in range(1,1000):
            for i in range(d+1, n):
                if num[d] + increase == num[i]:
                    replace = i
                    existed = True
                    break
            if existed :
                break
        # swap d, replace
        temp = num[d]
        num[d] = num[replace]
        num[replace] = temp
        # sort d+1 to n-1
        a1 = num[0:d+1]
        a2 = num[d+1:n]
        a2.sort()
        a1.extend(a2)
        return a1
    
    
num = [1,2,3,4]
num = [4,3,1,2,5,5,4,1]
a = Solution()
print a.nextPermutation(num)
