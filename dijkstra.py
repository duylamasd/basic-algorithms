import sys


class Graph:
    """
    This class represents a directed graph using adjacency matrix representation
    """

    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.adjecency_matrix = []

    def add_dist(self, distances):
        self.adjecency_matrix.append(distances)

    def dijkstra(self, source):
        def min_distance(distance, spt_set):
            min = sys.maxsize
            min_idx = 0

            for v in range(self.num_of_vertices):
                if (not spt_set[v]) and distance[v] <= min:
                    min = distance[v]
                    min_idx = v

            return min_idx

        def print_solution(distance):
            for i in range(self.num_of_vertices):
                print i, distance[i]

        spt_set = [False] * self.num_of_vertices
        distance = [sys.maxsize] * self.num_of_vertices
        distance[source] = 0

        for _ in range(self.num_of_vertices):
            u = min_distance(distance, spt_set)
            spt_set[u] = True

            for v in range(self.num_of_vertices):
                if (not spt_set[v]) and self.adjecency_matrix[u][v] != 0 and distance[u] != sys.maxsize and (distance[u] + self.adjecency_matrix[u][v] < distance[v]):
                    distance[v] = distance[u] + self.adjecency_matrix[u][v]

        print_solution(distance)

# Test
g = Graph(9)
g.add_dist([0, 4, 0, 0, 0, 0, 0, 8, 0])
g.add_dist([4, 0, 8, 0, 0, 0, 0, 11, 0])
g.add_dist([0, 8, 0, 7, 0, 4, 0, 0, 2])
g.add_dist([0, 0, 7, 0, 9, 14, 0, 0, 0])
g.add_dist([0, 0, 0, 9, 0, 10, 0, 0, 0])
g.add_dist([0, 0, 4, 14, 10, 0, 2, 0, 0])
g.add_dist([0, 0, 0, 0, 0, 2, 0, 1, 6])
g.add_dist([8, 11, 0, 0, 0, 0, 1, 0, 7])
g.add_dist([0, 0, 2, 0, 0, 0, 6, 7, 0])
g.dijkstra(0)
