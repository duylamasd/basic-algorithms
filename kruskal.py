class Stack:
    """
    This class represents a stack
    """

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return not self.stack


class Edge:
    """
    This class represents an edge of graph
    """

    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


class Subset:
    """
    This represents a subset for union-find
    """

    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


def find(subsets, i):
    stack = Stack()
    stack.push(i)

    while not stack.empty():
        i = stack.pop()
        parent = subsets[i].parent
        if parent != i:
            stack.push(parent)

    return subsets[i].parent


def union(subsets, x, y):
    xroot = find(subsets, x)
    yroot = find(subsets, y)

    if subsets[xroot].rank < subsets[yroot].rank:
        subsets[xroot].parent = yroot
    elif subsets[xroot].rank > subsets[yroot].rank:
        subsets[yroot].parent = xroot
    else:
        subsets[yroot].parent = xroot
        subsets[xroot].rank += 1


def compare(a, b):
    return a.weight - b.weight


class Graph:
    """
    This class represents a graph
    """

    def __init__(self, num_of_vertices, num_of_edges):
        self.num_of_vertices = num_of_vertices
        self.num_of_edges = num_of_edges
        self.edges = []

    def add_edge(self, src, dest, weight):
        self.edges.append(Edge(src, dest, weight))

    def kruskal_mst(self):
        result = [None] * self.num_of_vertices
        e = 0
        i = 0

        # Sort all the edges
        self.edges.sort(compare, None, False)

        subsets = []
        for v in range(self.num_of_vertices):
            subsets.append(Subset(v, 0))

        while e < self.num_of_vertices - 1:
            next_edge = self.edges[i]
            i += 1

            x = find(subsets, next_edge.src)
            y = find(subsets, next_edge.dest)

            if x != y:
                result[e] = next_edge
                e += 1
                union(subsets, x, y)

        print "The edges in the constructed MST"
        for i in range(0, e):
            print result[i].src, result[i].dest, result[i].weight


g = Graph(4, 5)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
g.kruskal_mst()
