from graph_generator import GraphGenerator
from kruskals import kruskals
from prims import prims

# generating the graphs
graph = GraphGenerator(10) # up to 10 verticies
sparse_edges = graph.generate_sparse_graph()
dense_edges = graph.generate_dense_graph()


# Running the Algorithm
print("\n\t\t--- Kruskal's ---")
print("\nMST of Sparse Graph:")
kruskals(sparse_edges)

print("\nMST of Dense Graph:")
kruskals(dense_edges)

# Running the Algorithm
print("\n\t\t--- Prim's ---")
print("\nMST of Sparse Graph:")
prims(sparse_edges)

print("\nMST of Dense Graph:")
prims(dense_edges)
