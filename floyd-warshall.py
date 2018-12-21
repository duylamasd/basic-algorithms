import sys

MAX_INT = sys.maxsize


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

    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.adjacency_matrix = []

    def add_dist(self, distances):
        self.adjacency_matrix.append(distances)

    def floyd_warshall(self):
        def print_solution(dist):
            print "The shortest distances between every pair of vertices"
            for i in range(self.num_of_vertices):
                for j in range(self.num_of_vertices):
                    if dist[i][j] == MAX_INT:
                        print "INF",
                    else:
                        print dist[i][j],
                print ''

        def shortest_path(src, dest, path):
            result = []
            stack = Stack()
            stack.push(dest)

            while path[src][dest] != src:
                stack.push(path[src][dest])
                dest = path[src][dest]

            result.append(src)
            while not stack.empty():
                result.append(stack.pop())

            return result

        dist = map(lambda i: map(lambda j: j, i), self.adjacency_matrix)
        path = map(lambda i: map(lambda j: j, i), self.adjacency_matrix)
        for i in range(self.num_of_vertices):
            for j in range(self.num_of_vertices):
                if path[i][j] != MAX_INT:
                    path[i][j] = i

        for k in range(self.num_of_vertices):
            for i in range(self.num_of_vertices):
                for j in range(self.num_of_vertices):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        path[i][j] = path[k][j]

        print_solution(dist)
        print shortest_path(0, 3, path)


# Test
g = Graph(4)
g.add_dist([0, 5, MAX_INT, 10])
g.add_dist([MAX_INT, 0, 3, MAX_INT])
g.add_dist([MAX_INT, MAX_INT, 0, 1])
g.add_dist([MAX_INT, MAX_INT, MAX_INT, 0])
g.floyd_warshall()
