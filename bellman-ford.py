import sys

MAX_INT = sys.maxsize


class Edge:
    """
    This class represents an edge of graph
    """

    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


class Graph:
    """
    This class represents a graph using adjacency matrix
    """

    def __init__(self, num_of_vertices, num_of_edges):
        self.num_of_vertices = num_of_vertices
        self.num_of_edges = num_of_edges
        self.edges = []

    def add_edge(self, source, dest, weight):
        self.edges.append(Edge(source, dest, weight))

    def has_negative_cycle(self, source, dist):
        # Initialize distances from source to all vertices as MAX_INT
        for i in range(self.num_of_vertices):
            dist[i] = MAX_INT
        dist[source] = 0

        # Relax all edges V - 1 times.
        # A simple shortest path from source to any
        # other vertex can have at most V - 1 edges
        for _ in range(1, self.num_of_vertices):
            for j in range(self.num_of_edges):
                u = self.edges[j].src
                v = self.edges[j].dest
                weight = self.edges[j].weight

                if (dist[u] != MAX_INT) and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        # Check for negative weight cycles.
        # The above step guarantees shortest distances
        # if graph doesn't contain negative weight cycle.
        # If we get a shorter path, then there is a cycle
        for i in range(self.num_of_edges):
            u = self.edges[i].src
            v = self.edges[i].dest
            weight = self.edges[i].weight

            if (dist[u] != MAX_INT) and dist[u] + weight < dist[v]:
                return True

        return False

    def is_negative_cycle_disconnected(self):
        visited = [False] * self.num_of_vertices
        # visited[0] = False
        dist = [MAX_INT] * self.num_of_vertices

        for i in range(self.num_of_vertices):
            if not visited[i]:
                if self.has_negative_cycle(i, dist):
                    return True
                
                for _ in range(self.num_of_vertices):
                    if dist[i] != MAX_INT:
                        visited[i] = True

        return False

# Test
g = Graph(5, 8)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

print g.is_negative_cycle_disconnected()