# Palindrome Partitioning.py

# Question: 
#Given a string s, partition s such that every substring of the partition is a palindrome.
#Return all possible palindrome partitioning of s.
#For example, given s = "aab",
#Return [
    #["aa","b"],
    #["a","a","b"]
  #]
# Question from: https://oj.leetcode.com/problems/palindrome-partitioning/
# Sulotion:
# Author: DongDing 
# Date: 2014/07/26
# Time complexity:  O(n^3)  , n is the length of the string
# space complexity:  O(n^2)
# Tag: # string # Dynamic Programming
# Comment: 


class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if len(s) == 0:
            return []
        # initiallize the tabulation, partition[i]:  result for s[0:i]
        partition = [[] for i in range(len(s))]
        
        for i in range(len(s)):
            for j in range(i+1):
                if self.isPalindrome(s[j:i+1]):
                    if j-1 < 0:  # deal with the first letter
                        partition[i].append([s[j:i+1]])
                        continue
                    for temp in partition[j-1]: 
                        a = []
                        a.extend(temp)
                        a. append(s[j:i+1]) 
                        partition[i].append(a)
        return partition[len(s)-1]        
                
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

s = "aaaa"
a = Solution()
print a.partition(s)
