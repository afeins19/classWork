# generates edge objects

import random

class Edge:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost

    def get_verticies(self):
        return (self.start, self.end)

    def __str__(self):
        return f"{ self.start } -- { self.cost } -- { self.end }"

class Vertex:
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return self.val

    def __eq__(self, other):
        # making sure that we can compare vertex objects
        return self.val == other.val if isinstance(other, Vertex) else False

    def __hash__(self):
        # Provides a hash based on the 'val' attribute
        return hash(self.val)



class GraphGenerator:
    """Supports up to 10 Verticies"""
    def __init__(self, count):
        node_names = list("abcdefghijklmnopqrstuvwxyz")
        self.count = count

        # making  vertex objects
        self.graph = [Vertex(node_names[i]) for i in range(self.count)]

    def generate_sparse_graph(self):

        # generating the edges (random weights)
        print("\nGenerating Sparse Graph:")
        sparse_edges = [Edge(self.graph[random.randint(1, len(self.graph) - 1)],
                             self.graph[random.randint(1, len(self.graph) - 1)],
                             random.randint(1, 100)) for v in self.graph]

        for edge in sparse_edges:
            print(f"\t{edge}")

        return sparse_edges

    def generate_dense_graph(self):
        dense_edges = []

        # making a dense graph
        print("\nGenerating Dense Graph: ")
        existing = []

        # generating a non-directed dense graph
        for node in self.graph:
            for neighbor in self.graph:
                if neighbor not in existing:
                    edge = Edge(node, neighbor, cost=random.randint(1, 100))
                    dense_edges.append(edge)
                    print(f"\t{edge}")
            existing.append(node)

        return dense_edges






