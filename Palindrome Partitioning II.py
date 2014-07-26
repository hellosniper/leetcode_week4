# Palindrome Partitioning II.py

class Solution:
    # @param s, a string
    # @return an integer
    

    def minCut(self, s):
        if len(s) == 0:
            return 0
        #if self.isPalindrome(s):
            #return 0        
        # initialize tabulation
        # partition[i] = [3,4] means cut after 3 and 4,   s[0:3], s[3+1,4], s[4:i]  
        partition = [[] for i in range(len(s))]
        # pali[i][j] == Ture if s[i:j+1] isPalindrome
        pali = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            mincut = i # initialize num of cut to the max
            #print mincut
            if i == 0:
                continue
            for j in range(i+1):

                if s[i] == s[j] and (i -j <= 2 or pali[i-1][j+1] == True ):
                    pali[i][j] = True
                    temp = []
                    if j-1>=0:
                        temp.extend(partition[j-1])
                        if len(temp) <= mincut:
                            mincut = len(temp)
                            temp.append(j-1)
                            partition[i] = []
                            partition[i].extend(temp)   
                    else:
                        partition[i] = []
                        break
        return len(partition[-1])   


    ## o(n^3) , TLE
    # def minCut(self, s):
    #     if len(s) == 0:
    #         return 0
    #     if self.isPalindrome(s):
    #         return 0
    #     # initialize tabulation
    #     # partition[i] = [3,4] means cut after 3 and 4,   s[0:3], s[3+1,4], s[4:i]  
    #     partition = [[] for i in range(len(s))]
        
    #     for i in range(len(s)):
    #         mincut = i # initialize num of cut to the max
            
    #         if i == 0:
    #             continue
    #         for j in range(i+1):
    #             if self.isPalindrome(s[j:i+1]):
    #                 temp = []
    #                 if j-1>=0:
    #                     temp.extend(partition[j-1])
    #                     if len(temp) <= mincut:
    #                         mincut = len(temp)
    #                         temp.append(j-1)
    #                         partition[i] = []
    #                         partition[i].extend(temp)   
    #                 else:
    #                     partition[i] = []
    #                     break
    #     return len(partition[len(s)-1])
    
    # def isPalindrome(self, s):
    #     if len(s) ==0:
    #         return True
    #     #s = s.lower()
    #     #s = [x for x in s if x in "abcdefghijklmnopqrstuvwxyz1234567890"]
        
    #     #s1 = s.reverse()
    #     if s[::-1] == s:
    #         return True
    #     else:
    #         return False
        
