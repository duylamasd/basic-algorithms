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

    def dfs(self, s):
        """
        Prints all not yet visited vertices reachable from s
        """
        visited = [False] * self.num_of_vertices
        stack = Stack()
        stack.push(s)

        while not stack.empty():
            # Pop a vertex from stack
            s = stack.pop()

            if not visited[s]:
                print s
                visited[s] = True

            print visited

            for node in self.adjecency[s]:
                if not visited[node]:
                    stack.push(node)
        print s

    def is_cyclic_util(self, v, visited, rec_stack):
        """
        Visit the graph by dfs
        """
        if not visited[v]:
            visited[v] = True
            rec_stack[v] = True

            stack = Stack()
            stack.push(v)

            while not stack.empty():
                s = stack.pop()

                if not visited[s]:
                    visited[s] = True

                for node in self.adjecency[s]:
                    if not visited[node]:
                        stack.push(node)
                    elif rec_stack[node]:
                        return True

        rec_stack[v] = False
        return False

    def is_cyclic(self):
        """
        Check whether the graph is cyclic
        """
        visited = [False] * self.num_of_vertices
        rec_stack = [False] * self.num_of_vertices
        for i in range(self.num_of_vertices):
            if self.is_cyclic_util(i, visited, rec_stack):
                return True

        return False


# Test

g = Graph(4)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print g.is_cyclic()
