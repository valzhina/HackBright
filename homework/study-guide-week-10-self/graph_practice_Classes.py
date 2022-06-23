# ------ #
# Graphs Solutions via creating Class#
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



def has_path_iter(node1, target_node): #Beginning of the solution using Class Node
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



# #####################################################################
# #Avarage of level 
# #####################################################################

class AvrNode():
    """initial Node"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def cruise(data,node, level = 0):
    """Creating a collection"""
    if not node:
        return None
    print(node.value)
    if level not in data:
        data[level] = []
       
    data[level].append(node.value)

    cruise(data, node.left, level + 1)
    cruise(data, node.right, level + 1)
   
def average(node):
    """Calculating Avr"""
   
    data = {}
    cruise(data, node, 0)
    print(data)
    result = []
   
    i = 0
    while i in data:
        avg = sum(data[i]) / len(data[i])
        result.append(avg)
        i+=1
    return result

#       2 (Node1)
#      /\
#     3  5 
#    /  /\
#   6  9  10 
#    \
#     7   

n2 = AvrNode(2)
n3 = AvrNode(3)
n5 = AvrNode(5)
n6 = AvrNode(6)
n7 = AvrNode(7)
n9 = AvrNode(9)
n10 = AvrNode(10)

n2.left = n3
n3.left = n6
n5.left = n9

n2.right = n5
n6.right = n7
n5.right = n10

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

