#Implement strStr().py
#Question: #Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack..

# Question from: https://oj.leetcode.com/problems/implement-strstr/
# Sulotion:
# Author: DongDing 
# Date: 2014/08/04
# Time complexity:  O(len_h*len_n)
# space complexity:  O(1)  
# Tag:  # Stack # String
# Comment: 

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        len_h = len(haystack)
        len_n = len(needle)
        if len_n == 0:
            return haystack
        if haystack == None or len_h<len_n:
            return None
        
        for i in range(0,len_h-len_n+1):
            if haystack[i:i+len_n] == needle:
                return haystack[i:len_h]
