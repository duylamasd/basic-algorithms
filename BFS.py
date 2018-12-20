class Queue:
    """
    This class represents a queue
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Graph:
    """
    This class represents a directed graph using adjacency list representation
    """

    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.adjecency = []
        for _ in range(num_of_vertices):
            self.adjecency.append([])

    def add_edge(self, v, w):
        self.adjecency[v].append(w)

    def bfs(self, s):
        visited = [False] * self.num_of_vertices
        queue = Queue()
        visited[s] = True
        queue.enqueue(s)

        while not queue.is_empty():
            s = queue.dequeue()
            print s

            for node in self.adjecency[s]:
                if not visited[node]:
                    visited[node] = True
                    queue.enqueue(node)

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.bfs(2)