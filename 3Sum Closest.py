# 3Sum Closest.py
# Question: Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
# Question from: https://oj.leetcode.com/problems/3sum-closest/
# Sulotion:
# Author: DongDing 
# Date: 2014/07/25
# Time complexity:  O(n^2) 
# space complexity:  O(1)  
# Tag: # integer 
# Comment: 

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        #sum2 = [[0 for i in range(len(num))] for j in range (len(num))]
        #for i in  range(len(num)):
            #for j in  range(len(num)):
                #sum2[i][j] = num[i] + num[j]
        #result = sum2[0][1] +num[2]
        #for i in  range(len(num)):
            #for j in  range(len(num)):
                #if 
                #temp sum2[i][j] = num[i] + num[j]
        #sort
        #for i in  range(len(num)):
            #for j in  range(i+1,len(num)):
                #if num[i] > num[j]:
                    #temp = num[i]
                    #num[i] = num[j]
                    #num[j] = temp
                #else:
                    #pass
        num.sort()
        result = num[0]+ num[1] +num[2]
        #discrepancy = target - result  
        for i in range(len(num)):
            left = i+1
            right = len(num)-1
            while left< right:
                tempReslut = num[i]+ num[left] +num[right]
                if tempReslut == target:
                    return target
                elif tempReslut > target:
                    if abs(tempReslut-target)<abs(reslut-target):
                        reslut = tempReslut
                    right -= 1
                elif tempReslut < target:
                    if abs(tempReslut-target)<abs(reslut-target):
                        reslut = tempReslut                    
                    left += 1
        return result     
            
