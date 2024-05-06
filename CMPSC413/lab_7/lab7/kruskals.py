# Kruslkals Algorithm for Graphs
import random

from graph_generator import GraphGenerator

def kruskals(edges):
    vertices = set()

    for e in edges:
        vertices.add(e.start)
        vertices.add(e.end)

    # sorting edges in order by increasing path cost
    sorted_edges = sorted(edges, key=lambda edge: edge.cost)

    mst = []
    total_cost = 0

    # keep track of the connections of each vertex
    components = {v: v for v in vertices}

    for edge in sorted_edges:
        start = components[edge.start]
        end = components[edge.end]

        # if start and end vertices are in different graphs -> no cycle
        if start != end:
            mst.append(edge)
            total_cost += edge.cost

            # updating the vertex tracker
            for vertex in vertices:
                if components[vertex] == end:
                    components[vertex] = start

    print("\n\t\tMST")
    for edge in mst:
        print(f"\t{edge}")
    print(f"\n\tTotal Path Cost of MST: {total_cost}")

