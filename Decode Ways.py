# Decode Ways.py

# Question:  message containing letters from A-Z is being encoded to numbers using the following mapping:
#'A' -> 1
#'B' -> 2
#...
#'Z' -> 26
#Given an encoded message containing digits, determine the total number of ways to decode it.

# Question from: https://oj.leetcode.com/problems/decode-ways/
# Sulotion:
# Author: DongDing 
# Date: 2014/08/03
# Time complexity:  O(n)
# space complexity:  O(n)  
# Tag:  # Dynamic Programming # String
# Comment: 


class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        if s == "0":
            return 0
        ways = [0 for i in range(len(s))] 
        if s[0] == '0':
            return 0
        else:
            
            ways[0] = 1
            prev = 1
        for i in range(1,len(s)):
            if ((s[i-1] == '1' or  s[i-1] == '2') and s[i] == '0'):  # only s[i-1: i+1] is valid:  10, 20
                ways[i] = prev
            elif int(s[i-1:i+1]) >26 and s[i] != '0' or (s[i-1] == '0' and s[i] != '0'):   #only s[i] is valid:    01 - 09, or (>26  not (30, 40 ... )) 
                ways[i] = ways[i-1]
            elif int(s[i-1:i+1]) <=26 and int(s[i-1:i+1]) >10 and s[i] != '0': #  both are valid  11 - 26 excpt 20
                ways[i] = ways[i-1] + prev
            elif s[i-1] != '1' and  s[i-1] != '2' and s[i] == '0':  # None is valid 00, 30, 40 ...
                ways[i] = 0
            prev = ways[i-1]
        return ways[-1]
    
a = Solution()
s = "301"
print a.numDecodings(s)
