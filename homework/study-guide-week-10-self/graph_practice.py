# ------ #
# Graphs #
# ------ #

#####################################################################
#Is there a path/ Node and Graph Class 
#####################################################################

import collections

class PersonNode:
    """Node is a graph representation of a person """

    def __init__(self, name, adjacent=None):
        """Create a person node with friends adjacent"""

        if adjacent is None:
            adjasent = set()

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
            return f"<FriendGraph: {{n.name for n in self.nodes}}>"  

        def add_person(self, person):
            """Adds a person"""

            self.nodes.add(person)
        
        def set_friends(self, person1, person2):
            """Sets two people as friends"""

            person1.adjacent.add(person2)
            person2.adjacent.add(person1)

        def are_connected(self, person1, target_person):
            """Breadth-first search"""
            
            possible_nodes = Queue()
            seen = set()
            possible_nodes.enqueue(person1)
            seen.add(person1)

            while not possible_nodes.is_empty():
                person_to_check = possible_nodes.dequeue()
                print("checking", person_to_check)
                if person_to_check is target_person:
                    return True
                else:
                    for a_node in person_to_check.adjasent - seen: #sets can be substracted from each other
                        possible_nodes.enqueue(a_node)
                        seen.add(a_node)
                        print("added to queue:", a_node)
            return False 

        def are_connected_recursive(self, person1, target_person, seen=None):
            """Recursive depth-first search"""
            if not seen:
                seen = set()
            
            if person1 in target_person:
                return True

            seen.add(person1)
            print("adding", person1)

            for person_to_check in person1.adjacent:

                if person_to_check not in seen:

                    if self.are_connected_recursive(person_to_check, target_person, seen):
                        return True

            return False


#####################################################################
# Is there a path // Graph without Class 
#####################################################################

from collections import deque

def are_connected(graph, node1, target_node):
        """Breadth-first search"""
        
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
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def best_path(node):
    
    if not node:
        return 0

    lc = best_path(node.left)
    rc = best_path(node.right)

    best_child = max(lc, rc)

    return best_child + node.val

if __name__ == "__main__":
    graph = {0:[1,2,3], 1:[0,2],2:[0,1],3:[0],4:[2]}

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
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    # print()
    # result = doctest.testmod()
    # if not result.failed:
    #     print("ALL TESTS PASSED. GOOD WORK!")
    # print()




#####################################################################
#200. Number of Islands
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

#####################################################################
#207. Course Schedule
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

from collections import deque
def are_connected(graph, node1, target_node):
        """Breadth-first search"""
        
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

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def best_path(node):
    
    if not node:
        return 0

    lc = best_path(node.left)
    rc = best_path(node.right)

    best_child = max(lc, rc)

    return best_child + node.val

if __name__ == "__main__":
    graph = {0:[1,2,3], 1:[0,2],2:[0,1],3:[0],4:[2]}
    
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

    print(best_path(n1))
    # print(are_connected(graph, 0, 4))
    # breadth_first_search(graph,0)