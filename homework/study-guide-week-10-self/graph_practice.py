# ------ #
# Graphs #
# ------ #
from collections import deque

#####################################################################
# Is there a path // Graph without creation of a Class  via Hashmap 
#####################################################################

def are_connected_via_gr(graph, node1, target_node):
    """Iterative Breadth-first search has path"""
    
    possible_nodes = deque() # creating a set via Queue
    seen = set()
    possible_nodes.append(node1) # adding really first node to a queue
    seen.add(node1) # adding a node to a set

    while possible_nodes: # while queue exists
        node_to_check = possible_nodes.popleft() # removing first element from queue and storing it in a varieble
        print("checking", node_to_check)
        if node_to_check == target_node:
            return True
        else:
            for item in graph[node_to_check]: #iterating through neighbours
                if item not in seen: #substracting neighbours that we have seen
                    possible_nodes.append(item) # adding neighbouring nodes to a queue
                    seen.add(item) # marking neighbouring nodes as seen
                    print("added to queue:", item)
    return False 


# graph = {0:[1,2,3], 1:[0,2],2:[0,1],3:[0],4:[2]}
# print(are_connected_via_gr(graph, 0, 4))

def breadth_first_search(graph, source, destination):
    """Breadth-first search simple solution has path"""
    q = deque([source])
   
    while len(q)>0:
        cur = q.popleft()
        if cur == destination:
            return True
        for v in graph[cur]:
            q.append(v)
    return False

# graph = {'a':['c','b'],
#          'b':['d'],
#          'c':['e'],
#          'd':['f'],
#          'e':[],
#          'f':[]}

# breadth_first_search(graph, 'a', 'b')



def has_path_dfs_rec(graph, source, destination):
    """Depth-first search Recurcive has path"""

    if source==destination:
        return True
    for v in graph[source]:
        if has_path_dfs_rec(graph, v, destination):
            return True
    return False

# graph_new = {'a':['c','b'],
#          'b':['d'],
#          'c':['e'],
#          'd':['f'],
#          'e':[],
#          'f':[]}

# print(has_path_dfs_rec(graph_new, 'a', 'g'))


#####################################################################
# Depth First Print (Search) via Hashmap 
#####################################################################

def depth_first_search_print(graph, source):
    """Recursive solution"""
    print(source)
    for neighbour in graph[source]:
        depth_first_search_print(graph, neighbour)


# graph = {'a':['b','c'],
#          'b':['d'],
#          'c':['e'],
#          'd':['f'],
#          'e':[],
#          'f':[]}

# depth_first_search_print(graph,'a')

#Option II
def depth_first_search_print_iter(graph, source):
    """Iterative Solution"""
    stack = [source]
   
    while stack:
        current = stack.pop()
        stack += graph[current] # add neighbours into stack by using key = 'a'(source), so value will be neighbours of 'a' ['c','b']
        print(current)
   

# graph = {'a':['c','b'],
#          'b':['d'],
#          'c':['e'],
#          'd':['f'],
#          'e':[],
#          'f':[]}

# depth_first_search_print_iter(graph,'a')



# #####################################################################
# #
# #####################################################################

# edges = [['i','j'],['k','i'],['m','k'],['k','l'],['o','n']]

# def undirectedPath(edges, nodeA, nodeB):
#     graph = buildGraph(edges)
   
#     visited = set()
#     stack = [nodeA]
   
#     while len(stack)>0:
#         cur =stack.pop()
#         visited.add(cur)
       
#         if cur==nodeB:
#             return True
       
#         for v in graph[cur]:
#             if v not in visited:
#                 stack.append(v)
#     return False

# #####################################################################
# #
# #####################################################################

# def buildGraph(edges):
#     graph = {}
#     for e in edges:
#         a, b = e
#         if a not in graph:
#             graph[a] = []
#         graph[a].append(b)
#         if b not in graph:
#             graph[b] = []
#         graph[b].append(a)
   
#     return graph
       
# undirectedPath(edges, 'm', 'o')       


# ccc_graph = {0:[8,1,5],
#             1:[0],
#             2:[3,4],
#             3:[2,4],
#             4:[3,2],
#             5:[0,8],
#             8:[0,5]}

# #####################################################################
# Connected Components in the graph
# #####################################################################
'''
Given an undirected graph, the task is to print the number of connected components in the graph.

ccc_graph = {0:[8,1,5],
            1:[0],
            2:[3,4],
            3:[2,4],
            4:[3,2],
            5:[0,8],
            8:[0,5]}

In this task we must visit each node so the best complexity is O(N)
I will write a code that traverses each node and their connected node. If it is an unknown node for us, I will add to count
'''

def ccc(graph):
    """Counting components """
    count = 0
    # as we need to keep track of visited nodes, I create hash set
    visited = set()
    
    for key in graph:
        if key not in visited:
            explore(graph, key, visited)
            count+=1
    return count

def explore(graph, key, visited):
    """Exploring Graph """
    if key in visited:
        return
    visited.add(key)
    for item in graph[key]:
        explore(graph, item, visited)
    return True

# print (ccc(ccc_graph))     


# #####################################################################
# Largest Component
# #####################################################################
"""Return the number of nodesin the largest of components of a graph"""

def largest_component(ccc_graph):
    """Through hash set"""
    visited = set()
    result = 0
    for key in ccc_graph:
        value = explore_lc(ccc_graph, key, visited)
        result = max(value, result)
    return result

def explore_lc(ccc_graph, key, visited):
    """ Explore Graph """
   
    if key in visited:
        return 0

    visited.add(key)

    count = 1
   
    for item in ccc_graph[key]:
        count += explore_lc(ccc_graph, item, visited)
   
    return count

# ccc_graph = {0:[8,1,5],
#             1:[0],
#             2:[3,4],
#             3:[2,4],
#             4:[3,2],
#             5:[0,8],
#             8:[0,5]}

# print(largest_component(ccc_graph))  


# #####################################################################
# 
# #####################################################################


# shortest_path = {'w':['x','v'],
#                 'x':['w','y'],
#                 'v':['w','z'],
#                 'y':['x','z'],
#                 'z':['y','v']}

# def shortestPath(graph, src, dst):
#     visited = set(src)
#     q = deque([(src,0)])
   
#     while len(q)>0:
#         cur, level = q.popleft()
#         if cur==dst:
#             return level
       
#         for n in  graph[cur]:
#             if n not in visited:
#                 visited.add(n)
#                 q.append((n, level+1))
#     return -1

# # shortestPath(shortest_path, 'w', 'z')


#####################################################################
#200. Number of Islands
#####################################################################

"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""

grid = [['W','W','W','W','W'],
        ['W','W','W','W','W'],
        ['W','W','W','W','W'],
        ['W','W','W','W','W'],
        ['W','W','W','W','W'],
        ['W','L','W','W','W']]

def m_island(grid):
    """TBD"""
    visited = set()
    mn_size = len(grid)*len(grid[0])
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='L' and (i,j) not in visited:
                temp = explore_island(grid, i, j, visited)
                mn_size = min(mn_size, temp)
    return mn_size

def explore_island(grid, i, j, visited):
    """TBD"""
    if i<0 or i>=len(grid) or j < 0 or j>=len(grid[0]):
        return 0
    if (i, j) in visited:
        return 0
   
    visited.add((i,j))
   
    if grid[i][j]=='W':
        return 0

    size = 1
    size += explore_island(grid, i+1, j, visited)
    size += explore_island(grid, i-1, j, visited)
    size += explore_island(grid, i, j+1, visited)
    size += explore_island(grid, i, j-1, visited)
    return size

# m_island(grid)


#####################################################################
#207. Course Schedule
#####################################################################

"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

#####################################################################
#210. Course Schedule II
#####################################################################
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""

#####################################################################
#994. Rotting Oranges
#####################################################################
"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""

#####################################################################
#417. Pacific Atlantic Water Flow
#####################################################################

"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105

"""

#####################################################################
#79. Word Search
#####################################################################

"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""



# if __name__ == "__main__":
