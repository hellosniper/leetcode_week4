# Palindrome Number.py

# Question: Determine whether an integer is a palindrome. Do this without extra space.
# Question from: https://oj.leetcode.com/problems/palindrome-number/
# Sulotion:
# Author: DongDing 
# Date: 2014/07/25
# Time complexity:  O(n)  , n the digit of decimal integer
# space complexity:  O(1)  
# Tag: # integer 
# Comment: 


class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        Pali = 0
        if x < 0:
            return False
        temp = x
        while temp != 0:
            Pali = Pali*10 +  temp%10
            temp = temp/10
        
        return x == Pali 
