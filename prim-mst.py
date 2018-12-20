import sys

MAX_INT = sys.maxsize


class Graph:

    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.adjecency_matrix = []

    def add_dist(self, distances):
        self.adjecency_matrix.append(distances)

    def min_key(self, key, mst_set):
        """
        A utility function to find the vertex
        with minimum key value, from the set of vertices
        not yet included in MST
        """
        min = MAX_INT
        min_idx = 0

        for v in range(self.num_of_vertices):
            if (not mst_set[v]) and key[v] < min:
                min = key[v]
                min_idx = v

        return min_idx

    def print_mst(self, parent):
        """
        A utility function to print the constructed MST stored in parent
        """
        print "edge", "weight"
        for i in range(1, self.num_of_vertices):
            print parent[i], i, self.adjecency_matrix[i][parent[i]]

    def prim_mst(self):
        """
        Construct and print MST for a graph represented using adjecency matrix representation
        """

        # Key values used to pick minimum weight edge in cut
        key = [MAX_INT] * self.num_of_vertices
        # Always include first vertex in MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0

        # Array to store constructed MST
        parent = [MAX_INT] * self.num_of_vertices
        # First node is always root of MST
        parent[0] = -1

        # Represent set of vertices not yet included in MST
        mst_set = [False] * self.num_of_vertices

        for _ in range(self.num_of_vertices - 1):
            # Pick the minimum ket vertex from the
            # set of vertices not yet included in MST
            u = self.min_key(key, mst_set)

            # Add the picked vertex to the MST set
            mst_set[u] = True

            # Update key value and parent index
            # of the adjacent vertices of the picked vertex.
            # Consider only those vertices which are not
            # yet included in MST
            for v in range(self.num_of_vertices):
                # graph[u][v] is non zero only for adjecent vertices of m
                # mst_set[v] is False for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.adjecency_matrix[u][v] and (not mst_set[v]) and self.adjecency_matrix[u][v] < key[v]:
                    parent[v] = u
                    key[v] = self.adjecency_matrix[u][v]

        self.print_mst(parent)


# Test
g = Graph(5)
g.add_dist([0, 2, 0, 6, 0])
g.add_dist([2, 0, 3, 8, 5])
g.add_dist([0, 3, 0, 0, 7])
g.add_dist([6, 8, 0, 0, 9])
g.add_dist([0, 5, 7, 9, 0])

g.prim_mst()
