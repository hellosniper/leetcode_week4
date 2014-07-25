# Valid Palindrome.py

# Question: Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#For example,
#"A man, a plan, a canal: Panama" is a palindrome.
#"race a car" is not a palindrome.
# Question from: https://oj.leetcode.com/problems/valid-palindrome/
# Sulotion:
# Author: DongDing 
# Date: 2014/07/25
# Time complexity:  O(n)  , n the lenth of string
# Tag: # integer 
# Comment: 

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s) ==0:
            return True
        s = s.lower()
        s = [x for x in s if x in "abcdefghijklmnopqrstuvwxyz1234567890"]
        
        #s1 = s.reverse()
        if s[::-1] == s:
            return True
        else:
            return False
        
        
        
