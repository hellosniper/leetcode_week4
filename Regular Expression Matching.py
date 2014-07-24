# Regular Expression Matching.py

# Question: #Implement regular expression matching with support for '.' and '*'.
#'.' Matches any single character.
#'*' Matches zero or more of the preceding element.
#The matching should cover the entire input string (not partial).
#The function prototype should be:
#bool isMatch(const char *s, const char *p)

#Some examples:
#isMatch("aa","a") → false
#isMatch("aa","aa") → true
#isMatch("aaa","aa") → false
#isMatch("aa", "a*") → true
#isMatch("aa", ".*") → true
#isMatch("ab", ".*") → true
#isMatch("aab", "c*a*b") → true
# Question from: https://oj.leetcode.com/problems/regular-expression-matching/
# Sulotion:  
# Author: DongDing 
# Date: 2014/07/23
# Time complexity:  O(mn),  m = len(s), n = len(P)
# space complexity:  O(mn)  
# Tag:  # Dynamic Programming  # String Compare
# Comment: 
class Solution:
    # @return a boolean
    def isMatch (self,s, p):
        if len(s) <= 0 and len(p) <=0:
            return True
        elif len(s) == 1 and len(p) == 1:
            if p[0] == ".":
                return True
            else:
                return s == p
        #elif len(s) == 1 and len(p) != 1:
            #return False
        elif len(s) != 1 and len(p) == 1:
            return False        
        # Initialize the tabulation
        # M[i][j] : s[0:i] matches p[0:j]
        M = [[False for j in range(len(s)+1)] for i in range(len(p)+1)]
        M[0][0] = True
        #M[0][1] = False
        #M[1][0] = False
        
        for i in range(1,len(p)+1):
            if p[i-1] =="*":
                M[i][0] = M[i-2][0]
                
        #pi = 0
        #si = 0    
        for j in range(1,len(s)+1):
            for i in range(1,len(p)+1):
                if p[i-1] == ".":
                    M[i][j] = M[i-1][j-1]
                elif p[i-1] == "*":
                    M[i][j] = M[i-2][j] or ((p[i-1-1] == s[j-1] or p[i-1-1] == ".") and M[i][j-1])
                elif p[i-1] == s[j-1]:
                    M[i][j] = M[i-1][j-1]
                elif  p[i-1] != s[j-1]:
                    M[i][j] = False
        return M[len(p)][len(s)]            


s = "a"
p = "ab*a"
a = Solution()
print a.isMatch(s, p)        
    #def isMatch(self, s, p):
        #if len(s) <= 0 and len(p) <=0:
            #return True

        #return self.compare(s,p,len(s)-1,len(p)-1)
        
    #def compare(self,s,p,si,pi):
        #if si < 0 and pi <0:
            #return True
        ##elif si < 0 and pi>=0:
            ##return False
        #elif si >=0 and pi < 0:
            #return False
        
        #if p[pi] == ".":
            #return self.compare(s,p,si-1,pi-1)
        #elif p[pi] == "*":
            
            #i = 0
            #while i <= si+1:
                #if (i == 0 or p[pi-1] == '.' or p[pi-1] == s[si-i+1]) and self.compare(s,p, si-i,pi-2):
                    #return True
                #if i != 0 and p[pi-1] != '.' and p[pi-1] != s[si-i+1]:
                    #break
                #i+=1
            
            ##temp1 = self.compare(s,p,si,pi-1)
            ##temp2 = self.compare(s,p,si-1,pi)
            ##return temp1 or (temp2 and p[pi-1] == s[si] )
        #elif p[pi] != s[si]:
            #return False
        #elif p[pi] == s[si]:
            #return self.compare(s,p,si-1,pi-1)
        #return False
    #def isMatch(self, s, p):        
        #if len(s) == 0:
            #return True
        ## Initialize the tabulation
        ## M[i][j] : s[0:i] matches p[0:j]
        ##M = [[False for j in range(len(p))] for i in range(len(s))]
        #M = [0 for i in range(len(p))]
        #j = 0
        #i = 0
        ##for i in range(len(p)):
        #while i < len(p):
            #if i != len(p)-1:
                #if p[i+1] != "*" :
                    #if p[i] == "." or p[i] == s[j] : # match
                        #M[i] = j 
                        #i+=1
                        #j+=1                            
                    #elif p[i] != s[j]: # not match
                        #return False                        
                #elif  p[i+1] == "*" :
                    #if p[i] == ".":
                        #return True
                    #elif p[i] == s[j]:
                        #while(p[i] == s[j]):
                            #j+=1
                            #if j >= len(s)-1:
                                #return True
                        
                    #elif p[i] != s[j]:
                        #pass
                    #i+=2
            #else: #last character
                #if p[i] == "." or p[i] == s[j] : # match
                    #M[i] = j 
                    #i+=1
                    #j+=1                            
                #elif p[i] != s[j]: # not match
                    #return False                                   
        #return True
#s = "aa"
#p = "a*"
#a = Solution()
#print a.isMatch(s, p)
