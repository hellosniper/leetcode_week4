# Climbing Stairs.py

# Question: You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Question from: https://oj.leetcode.com/problems/climbing-stairs/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/11
# Time complexity:  O(n)
# space complexity:  O(2)  
# Tag: # Dynimic Programming #
# Comment: 
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n <=0: 
            return 0
        pre0 = 1
        pre1 = 1
        curr = 1
        if n == 1:
            return 1
        for i in range(1,n):
            curr = pre0 + pre1
            pre0 = pre1
            pre1 = curr
        return curr
    
a = Solution()
print a.climbStairs(3)
        
        
