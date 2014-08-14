# Word Ladder.py
# Question: Given two words (start and end), 
#and a dictionary, find the length of shortest transformation sequence from start to end, such that:
#Only one letter can be changed at a time
#Each intermediate word must exist in the dictionary
#For example,
#Given:
#start = "hit"
#end = "cog"
#dict = ["hot","dot","dog","lot","log"]
#As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#return its length 5.
# Question from: https://oj.leetcode.com/problems/word-ladder/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/14
# Time complexity:  O(len(start)*26*n)
# space complexity:  O(n)  
# Tag: # BFS
# Comment:
# Python code : TLE

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        if start == end:
            return 1
        self.dict1 = []
        self.dict1.extend(dict)
        self.dict1.remove(start)
        self.target = end
        self.level = 1
        list1 = [start]
        # 
        self.found = False
        while list1:
            if len(self.dict1)>100:
                list1 = self.dfs(list1)
            else:
                list1 = self.dfs1(list1)
            self.level += 1
            if self.found:
                return self.level       
        # not found
        return 0
    # @param list1, a list of string, in which the current level of BFS tree
    # @return list2, a list of string, in which the next level of BFS tree       
    def dfs(self,list1):
        list2 = list()
        for item in list1:
            #find adjacent
            n = len(item)
            for i in range(n):
                alphabeta = "abcdefghigklmnopqrstuvwxyz"
                for index in range(26):
                    x = alphabeta[index]
                    if x == item[i]:
                        continue
                    word = item[0:i] +x +item[i+1:n]
                    if word in self.dict1:
                        self.dict1.remove(word)
                        if word == self.target:
                            self.found = True
                            return list2
                        list2.append(word)
                    else:
                        pass
        return list2  
            #for word in self.dict1:
                #if not self.compare(item,word):
                    #continue
                #self.dict1.remove(word)
                #if word == self.target:
                    #self.found = True
                    #return list2
                #list2.append(word)
  
    def dfs1(self,list1):
        list2 = list()
        for item in list1:
            #find adjacent
            for word in self.dict1:
                if not self.compare(item,word):
                    continue
                self.dict1.remove(word)
                if word == self.target:
                    self.found = True
                    return list2
                list2.append(word)
        return list2
    # @param item, a string
    # @param word, a string
    # @return True if only one letter differs between item and word , False otherwise     
    def compare(self,item,word):
        n = len(item)
        diff = 0
        for i in range(n):
            if item[i] == word[i]:
                pass
            else:
                diff += 1
            if diff >= 2:
                return False
        return True

start = "hit"
end = "hab"
dict1 = ["hit",'hib','hab']

a = Solution()
print a.ladderLength(start, end, dict1)
