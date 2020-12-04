# AOC Day 6

path = '.\\aoc.txt'
file_in = open(path, 'r')
lines = file_in.readlines()

# Example: local_orbits = [['N9N', 'LNM'], ['TJ4', 'ZVD']]
local_orbits = [line.strip().split(')') for line in lines]

class Node:
    def __init__(self,val):
        self.val = val
        self.distance = 0
        self.children = [] # the pointer initially points to nothing

all_nodes = dict() # key: "N9N", value: [children]

# Populate Dictionary of All Nodes
for pair in local_orbits:
	parent_val = pair[0] # 'N9N'
	child_val = pair[1] # 'LNM'
	if parent_val in all_nodes:
		all_nodes[parent_val].append(child_val)
	else:
		all_nodes[parent_val] = [child_val]
	if child_val not in all_nodes:
		all_nodes[child_val] = []

root = Node('COM')

def PopulateTree(root, all_nodes):
	for child_val in all_nodes[root.val]:
		child_node = Node(child_val)
		root.children.append(child_node)
		PopulateTree(child_node, all_nodes)

PopulateTree(root, all_nodes)

# Traverse Tree
total = 0
def CalculateDistance(parent):
	global total
	for child in parent.children:
		child.distance = parent.distance + 1
		total = total + child.distance
		if len(child.children) != 0:
			CalculateDistance(child)

CalculateDistance(root)
print(total)

def GetPathTo(parent, val, path):
	for child in parent.children:
		if child.val == val:
			path.append(parent.val)
			return True
		if len(child.children) != 0:
			if GetPathTo(child, val, path):
				path.append(parent.val)
				return True
	return False

path_to_you = []
GetPathTo(root, 'YOU', path_to_you)
path_to_santa = []
GetPathTo(root, 'SAN', path_to_santa)

path_to_you.reverse()
path_to_santa.reverse()

print(path_to_you)
print(path_to_santa)

count = 0
for idx, val in enumerate(path_to_you):
	if val == path_to_santa[idx]:
		continue
	else:
		count = len(path_to_you[idx:]) + len(path_to_santa[idx:])
		break
print(count)