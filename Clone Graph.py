# Clone Graph.py
# Question: Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
#OJ's undirected graph serialization:
#Nodes are labeled uniquely.
#We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
#As an example, consider the serialized graph {0,1,2#1,2#2,2}.
#The graph has a total of three nodes, and therefore contains three parts as separated by #.
#First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
#Second node is labeled as 1. Connect node 1 to node 2.
#Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
#Visually, the graph looks like the following:
# Question from: https://oj.leetcode.com/problems/clone-graph/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/13
# Time complexity:  O(n)
# space complexity:  O(n)  
# Tag: # Recursion # DFS
# Comment

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    #self.creatmap = {}
    #self.searchneighbors = []
    
    def cloneGraph(self,node):
        if node == None:
            return None
        self.marks = {}
        return self.dfs(node)
    def dfs(self,node):
        #copy node
        new_node = UndirectedGraphNode(node.label)
        #new_node.neighbors.extend(node.neighbors)
        self.marks.update({new_node.label: new_node})   ## mark
        # visit the adjacent nodes
        for item in node.neighbors:
            if self.marks.has_key(item.label):
                adjacent_node = self.marks.get(item.label)
                new_node.neighbors.append(adjacent_node)
            else:
                new_node.neighbors.append(self.dfs(item))
        return new_node
head = UndirectedGraphNode(0)
head.neighbors.append(head)
head.neighbors.append(head)


a = Solution()
new_node = a.cloneGraph(head)
print new_node == head

