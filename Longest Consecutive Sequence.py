# Longest Consecutive Sequence.py

# Question: Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

#For example,
#Given [100, 4, 200, 1, 3, 2],
#The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

#Your algorithm should run in O(n) complexity.
# Question from: https://oj.leetcode.com/problems/longest-consecutive-sequence/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/14
# Time complexity:  O(n)
# space complexity:  O(n)  
# Tag: # Hash Map # integer
# Comment:

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        maps = {}
        result = 0 
        for i in range(len(num)):
            
            t = num[i]
            if maps.has_key(t):
                continue
            if maps.has_key(t+1):
                rightlen = maps.get(t+1)
            else:
                rightlen = 0
            if maps.has_key(t-1):
                leftlen = maps.get(t-1)
            else:
                leftlen = 0
            totallen = rightlen + leftlen + 1
            
            if result < totallen:
                result = totallen
            start = t - leftlen
            end = t + rightlen
            
            maps.update({start:totallen})
            maps.update({end: totallen})
            maps.update({t:totallen})
        return result
    

num = [1,2,0,1]
a = Solution()            
print a.longestConsecutive(num)
            
