# Longest Valid Parentheses.py
#Question: Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

#For "(()", the longest valid parentheses substring is "()", which has length = 2.

#Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

# Question from: https://oj.leetcode.com/problems/longest-valid-parentheses/
# Sulotion:
# Author: DongDing 
# Date: 2014/08/03
# Time complexity:  O(n)
# space complexity:  O(n)  
# Tag:  # Stack # String
# Comment: 
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        end = True
        stack = []  # statck store the index of every "("
        ans = 0
        for i in range(len(s)):
            element = s[i]
            
            if element == '(':
                stack.append(i)
                if end:
                    init = i  # start index of a valid Praentheses sub string
                    end = False # False indicates  it is not within the valid Praentheses sub string
                    
            elif element == ')':
                if stack:
                    stack.pop()
                    if not stack and not end:
                        ans = max([ans, i - init+1])
                    else:
                        ans = max([ans, i- stack[-1]])
                else:
                    if end == False: # unmatched ')'
                        end = True
                        ans = max([ans, i - init])
                        

            else:
                pass
        return ans
        
       
    
s = "(()()()"
a = Solution()
print a.longestValidParentheses(s)
