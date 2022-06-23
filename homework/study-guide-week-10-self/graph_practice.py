# ------ #
# Graphs #
# ------ #
from collections import deque

#####################################################################
#Is there a path/ Node and Friends Graph Class 
#####################################################################

class PersonNode:
    """Node is a graph representation of a person """

    def __init__(self, name, adjacent=None):
        """Create a person node with friends adjacent"""

        if adjacent is None:
            adjacent = set()
        assert isinstance(adjacent, set), "adjacent must be a set"
        self.name = name
        self.adjacent = adjacent

    def __repr__(self):
        """Debugging-friendly representation"""

        return f"<PersonNode: {self.name}>"


class FriendGraph:
    """Graph holding people and their friends"""

    def __init__(self):
        """Create an empty graph"""
        self.nodes = set()

    def __repr__(self):
        return f"<FriendGraph: {[n.name for n in self.nodes]}>"  

    def add_person(self, person):
        """Adds a person"""
        self.nodes.add(person)
    
    def set_friends(self, person1, person2):
        """Sets two people as friends"""
        person1.adjacent.add(person2)
        person2.adjacent.add(person1)



#Option 1
def are_connected(person1, target_person):
    """Breadth-first search using Class *Node"""
    possible_nodes = deque()
    seen = set()
    possible_nodes.append(person1)
    seen.add(person1)

    while possible_nodes:
        person_to_check = possible_nodes.popleft()
        print("checking", person_to_check)
        if person_to_check == target_person:
            return True
        else:
            for a_node in person_to_check.adjacent - seen: #sets can be substracted from each other
                possible_nodes.append(a_node)
                seen.add(a_node)
                print("added to queue:", a_node)
    return False 


#Option 2
def are_connected_recursive(person1, target_person, seen=None):
    """Recursive depth-first search using Class *Node"""
    if not seen:
        seen = set()
    
    if person1 == target_person:
        return True

    seen.add(person1)
    print("adding", person1)

    for person_to_check in person1.adjacent:
        if person_to_check not in seen:
            if are_connected_recursive(person_to_check, target_person, seen):
                return True
    return False

def are_connected_dfs(person1, target_person):
    """Iterative Depth-first search using Class *Node"""

    stack = [] # creating a set via Queue
    seen = set()
    stack.append(person1) # adding really first node to a queue
    seen.add(person1)

    while stack:
        node_to_check = stack.pop()
        if node_to_check == target_person:
            return True
        else:
            for item in node_to_check.adjacent:
                if item not in seen:
                    stack.append(item)
                    seen.add(item)
                    print("added to queue:", item)

    return False

n1 = PersonNode(2)
n2 = PersonNode(5)
n3 = PersonNode(4)
n4 = PersonNode(3)
n5 = PersonNode(4)
n6 = PersonNode(7)
n7 = PersonNode(1)
n8 = PersonNode(6)   
n9 = PersonNode(9)
n10 = PersonNode(6)

n1.adjacent.add(n2)
n1.adjacent.add(n3)

n2.adjacent.add(n4)
n2.adjacent.add(n5)

n3.adjacent.add(n6)

n4.adjacent.add(n7)
n5.adjacent.add(n8)

n6.adjacent.add(n9)
n6.adjacent.add(n10)

# print(are_connected_recursive(n2, n9)) -> False
# print(are_connected_recursive(n2, n7)) -> True

# print(are_connected(n2, n9)) -> False
# print(are_connected(n2, n7)) -> True

# print(are_connected_dfs(n2, n9))
# print(are_connected_dfs(n2, n7))

#####################################################################
# Is there a path // Graph without Class 
#####################################################################

def are_connected_via_gr(graph, node1, target_node):
    """Iterative Breadth-first search"""
    
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


def has_path_dfs_rec(graph, source, destination):
    """Depth-first search Recurcive"""

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
# High-Scoring Path
#####################################################################
#       2 (Node1)
#      /\
#     5 4 (Node2 and 3)
#    /\ /\
#   3  4  7 (Node4, 5 and 6)
#  /\ /\ /\
# 1  6  9  6 (Node7, 8, 9 and 10)


class Node:
    """Creation of Node Class"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def best_path_recursive(node):
    """Resursive Solution"""
    if not node:
        return 0

    left_child = best_path_recursive(node.left)
    right_child = best_path_recursive(node.right)

    bigest_child = max(left_child, right_child)

    return bigest_child + node.value



def has_path_iter(node1, target_node): #Beginniong of the solution using Class Node
    """Iterative Solution  Depth-first search"""
        
    stack = [] # creating a set via Queue
    stack.append(node1) # adding really first node to a queue

    while stack:
        node_to_check = stack.pop()
        if node_to_check == target_node:
            return True
        elif  node_to_check:
            stack.append(node_to_check.left)
            stack.append(node_to_check.right)
            
    return False

#Building a Graph
n1 = Node(2)
n2 = Node(5)
n3 = Node(4)
n4 = Node(3)
n5 = Node(4)
n6 = Node(7)
n7 = Node(1)
n8 = Node(6)   
n9 = Node(9)
n10 = Node(6)

n1.left = n2
n1.right = n3

n2.left = n4
n2.right = n5

n3.left = n5
n3.right = n6

n4.left = n7
n4.right = n8

n5.left = n8
n5.right = n9

n6.left = n9
n6.right = n10

# print(best_path_recursive(n1))

# print(has_path_iter(n4, n9))

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

#####################################################################
#Breadth First Search
#####################################################################
from collections import deque

def breadth_first_search(graph, source):
   
    q = deque([source])
   
    while q:
        cur = q.popleft()
        print(cur)
        for v in graph[cur]:
            q.append(v)


# graph = {'a':['c','b'],
#          'b':['d'],
#          'c':['e'],
#          'd':['f'],
#          'e':[],
#          'f':[]}

# breadth_first_search(graph, 'a')

#####################################################################
#
#####################################################################


# #####################################################################
# #Avarage of level 
# #####################################################################
# def hasPathBFS(graph, src, dst):
#     q = deque([src])
   
#     while len(q)>0:
#         cur = q.popleft()
#         if cur==dst:
#             return True
#         for v in graph[cur]:
#             q.append(v)
#     return False
   

                         
# graph = {'a':['c','b'],
#          'b':['d'],
#          'c':['e'],
#          'd':['f'],
#          'e':[],
#          'f':[]}

# hasPathBFS(graph, 'a', 'f')





# edges = [['i','j'],['k','i'],['m','k'],['k','l'],['o','n']]

# #####################################################################
# #Avarage of level 
# #####################################################################

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
# #Avarage of level 
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
# '''
# Given an undirected graph, the task is to print the number of connected components in the graph.
# '''

# ccc_graph = {0:[8,1,5],
#             1:[0],
#             2:[3,4],
#             3:[2,4],
#             4:[3,2],
#             5:[0,8],
#             8:[0,5]}

# In this task we must visit each node so the best complexity is O(N)
# I will write a code that traverses each node and their connected node. If it is an unknown node for us, I will add to count
# def ccc(graph):
    
    count = 0
    # as we need to keep track of visited nodes, I create hash set
    visited = set()
    
    for key in graph:
        if key not in visited:
            explore(graph, key, visited)
            count+=1
    return count

def explore(graph, key, visited):
    if key in visited:
        return
    visited.add(key)
    for item in graph[key]:
        explore(graph, item, visited)


# print (ccc(ccc_graph))       
# def ccc(ccc_graph):
#     visited = set()
#     res = 0
#     for k in ccc_graph:
#         if xplore(ccc_graph, k, visited):
#             res+=1
#     return res

# def xplore(ccc_graph, node, visited):
#     if node in visited:
#         return False
#     visited.add(node)
#     for n in ccc_graph[node]:
#         xplore(ccc_graph, n, visited)
#     return True
# ccc(ccc_graph)    

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

# #####################################################################
# #Avarage of level 
# #####################################################################

# class AvrNode():
#     """initial Node"""
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def cruise(data,node, level = 0):
#     """Creating a collection"""
#     if not node:
#         return None
#     print(node.value)
#     if level not in data:
#         data[level] = []
       
#     data[level].append(node.value)

#     cruise(data, node.left, level + 1)
#     cruise(data, node.right, level + 1)
   
# def average(node):
#     """Calculating Avr"""
   
#     data = {}
#     cruise(data, node, 0)
#     print(data)
#     result = []
   
#     i = 0
#     while i in data:
#         avg = sum(data[i]) / len(data[i])
#         result.append(avg)
#         i+=1
#     return result

#       2 (Node1)
#      /\
#     3  5 
#    /  /\
#   6  9  10 
#    \
#     7   

# n2 = AvrNode(2)
# n3 = AvrNode(3)
# n5 = AvrNode(5)
# n6 = AvrNode(6)
# n7 = AvrNode(7)
# n9 = AvrNode(9)
# n10 = AvrNode(10)

# n2.left = n3
# n3.left = n6
# n5.left = n9

# n2.right = n5
# n6.right = n7
# n5.right = n10

# print(average(n2))
# print(n2.value)
#####################################################################
# Marine Food Chain
#####################################################################

class MarineAnimalNode:
    """Node in a graph representing a marine animal."""

    def __init__(self, name, prey=None):
        """Create a marine animal node with prey"""

        if prey:
            assert isinstance(prey, set), "prey must be a set!"
        self.name = name
        self.prey = prey or set()

    def __repr__(self):
        """Debugging-friendly representation"""

        return f"<MarineAnimalNode: {self.name}>"


class MarineFoodChainGraph:
    """Graph holding marine animals and their predator/prey relationships."""

    def __init__(self):
        """Create an empty graph"""

        self.nodes = set()

    def __repr__(self):
        return f"<MarineFoodChainGraph: {[n.name for n in self.nodes]}>"

    def add_animal(self, animal):
        """Add an animal to our graph"""

        self.nodes.add(animal)

    def add_animals(self, animals):
        """Add animals to our graph"""

        for animal in animals:
            self.nodes.add(animal)

    def is_prey(self, animal1, animal2):
        """Determine whether animal1 is prey of animal2

        >>> krill = MarineAnimalNode('krill')
        >>> squid = MarineAnimalNode('squid', set([krill]))
        >>> seal = MarineAnimalNode('seal', set(['squid']))
        >>> baleen_whale = MarineAnimalNode ('baleen whale', set([krill]))
        >>> orca = MarineAnimalNode('orca', set([seal, baleen_whale]))
        >>> aquarium = MarineFoodChainGraph()
        >>> aquarium.add_animals([krill, squid, seal, baleen_whale, orca])
        >>> aquarium.is_prey(krill, baleen_whale)
        True
        >>> aquarium.is_prey(squid, krill)
        False
        >>> aquarium.is_prey(krill, orca)
        False

        """

        return animal1 in animal2.prey


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
    visited = set()
    mn_size = len(grid)*len(grid[0])
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='L' and (i,j) not in visited:
                temp = explore_island(grid, i, j, visited)
                mn_size = min(mn_size, temp)
    return mn_size

def explore_island(grid, i, j, visited):
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

#####################################################################
# Connected components count
#####################################################################

'''
Given an undirected graph, the task is to print the number of connected components in the graph.
'''

ccc_graph = {0:[8,1,5],
            1:[0],
            2:[3,4],
            3:[2,4],
            4:[3,2],
            5:[0,8],
            8:[0,5]}

# In this task we must visit each node so the best complexity is O(N)
# I will write a code that traverses each node and their connected node. If it is an unknown node for us, I will add to count





# if __name__ == "__main__":
