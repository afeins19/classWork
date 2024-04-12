# Prim's Algorithm
"""
From Wikipedia: https://en.wikipedia.org/wiki/Prim%27s_algorithm#:~:text=In%20computer%20science%2C%20Prim's%20algorithm,in%20the%20tree%20is%20minimized.

1. Initialize a tree with a single vertex, chosen arbitrarily from the graph.
2. Grow the tree by one edge: Of the edges that connect the tree to vertices not yet in the tree, find the minimum-weight edge, and transfer it to the tree.
3. Repeat step 2 (until all vertices are in the tree)
"""
import random

from graph_generator import GraphGenerator
def prims(edges):
    # adjacency list for edges
    adjacent = {}

    # setup
    for edge in edges:
        adjacent.setdefault(edge.start, []).append((edge.end, edge.cost))
        adjacent.setdefault(edge.end, []).append((edge.start, edge.cost))

    # sorting edges by cost
    adjacent = {k: sorted(v, key=lambda x: x[1]) for k, v in adjacent.items()}

        # building the MST
    mst = {}
    total_cost = 0

    # track unvisited nodes to not include cycles
    visited = set()

    # starting with first node
    start_node = next(iter(adjacent))
    visited.add(start_node)
    mst[start_node] = []

    # until all nodes are visited...
    while len(visited) < len(adjacent):
        min_edge = None

        # find neighbor with minimum path cost
        for node in visited:
            for neighbor, cost in adjacent[node]:
                if neighbor not in visited:
                    if min_edge is None or cost < min_edge[2]:
                        min_edge = (node, neighbor, cost)

        # add edge to mst
        if min_edge:
            _, next_node, cost = min_edge
            visited.add(next_node)
            if min_edge[0] in mst.keys():
                mst[min_edge[0]].append((next_node, cost))

            else:
                mst[min_edge[0]] = [(next_node, cost)]

            total_cost += cost # update total cost


    # print the mst
    for node, neighbors in mst.items():
        for neighbor, cost in neighbors:
            print(f"\t{ node } -- { cost } -- { neighbor }")

    print(f"Total Cost: {total_cost}")








