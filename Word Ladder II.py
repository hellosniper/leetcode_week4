# Word Ladder II.py
# Question: #Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:
#Only one letter can be changed at a time
#Each intermediate word must exist in the dictionary
#For example,
#Given:
#start = "hit"
#end = "cog"
#dict = ["hot","dot","dog","lot","log"]
#Return
#[
    #["hit","hot","dot","dog","cog"],
    #["hit","hot","lot","log","cog"]
  #]
#Note:
#All words have the same length.
#All words contain only lowercase alphabetic characters.

# Question from: https://oj.leetcode.com/problems/word-ladder-ii/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/15
# Time complexity:  O(n^2* len(word))
# space complexity:  O(n^2)  
# Tag: # BFS
# Comment: Python: TLE

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        level = [start]
        finished = False  # indicate whether end is found or not
        wordpaths = {start:[[start]]}
        marked = {start:True}
        self.dict1 = []
        self.dict1.extend(dict)
        if not end in self.dict1:
            self.dict1.append(end)
        while level:
            nextlevel = []
            for word in level:
                newwords = self.findword(word) 
                for new in newwords:
                    if marked.get(new) == True:
                        continue
                    if new == end: # find the target
                        finished = True
                    paths = wordpaths.get(word) # list of word path
                    newpaths = wordpaths.get(new)
                    if not newpaths:
                        newpaths = []
                    for wp in paths:
                        #wp.append(new)
                        temp = []
                        temp.extend(wp)
                        temp.extend([new])
                        newpaths.append(temp)
                    wordpaths.update({new:newpaths})
                    if not (new in nextlevel):
                        nextlevel.append(new)
                
            if finished:
                break
            # mark
            for nllword in nextlevel:
                marked.update({nllword: True})
            
            level = nextlevel
        if finished:
            return wordpaths.get(end)
        else:
            return [[]]
    # input: a string
    # output: the list of strings that are next to the input string
    def findword(self,item):    
        list2 = list()
        for word in self.dict1:
            if self.compare(item,word):
                list2.append(word)
        return list2    
    
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
end = "lot"
dict1 = ["hot","lit","lot"]    
start = "hit"
end = "cog"
dict1 = ["hot","dot","dog","lot","log"]
a = Solution()

print a.findLadders(start, end, dict1)
