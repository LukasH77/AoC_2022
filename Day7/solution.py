from anytree import Node, RenderTree, search


def find_node(parent, name):
    for node in parent.children:
        if node.name == name:
            return node


data = open("aoc_day6_input.txt", "r")

line = data.readline()
line = data.readline()
line = data.readline().replace('\n', '')
root = Node("root", parent=None, size=0, dir=True)
nodes = [root]
current = root
while line:
    words = line.split(' ')
    if words[0] == "$" and words[1] == "cd":
        if words[2].replace('\n', '') == "..":
            current = current.parent
        else:
            current = find_node(current, words[2])
    elif words[0] == "dir":
        nodes.append(Node(f"{words[1]}", parent=current, size=0, dir=True))
    elif words[0].isnumeric():
        nodes.append(Node(f"{words[1]}", parent=current, size=int(words[0]), dir=False))
        current.size += int(words[0])
        tmp = current
        while tmp.parent is not None:
            tmp = tmp.parent
            tmp.size += int(words[0])
    line = data.readline().replace('\n', '')

print(RenderTree(root))

# part 1
sum = 0
sizes = []
for node in nodes:
    if node.dir:
        sizes.append(node.size)
        if node.size <= 100000:
            sum += node.size
print(sum)

# part 2
sizes.sort()
needed = 30000000 - (70000000 - root.size)
for n in sizes:
    if n >= needed:
        print(n)
        break
