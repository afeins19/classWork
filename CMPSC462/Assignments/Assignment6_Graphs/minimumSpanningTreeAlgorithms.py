import copy

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = self.generate_edges()

    def generate_edges(self, nodes=None):
        graph_nodes = nodes if nodes else self.nodes
        edges = []

        for node in graph_nodes:
            for neighbor in graph_nodes[node]:
                edges.append((node, neighbor[0], neighbor[1]))  # nodes are tuples of the form (neighbor, path cost)
        return edges

    def remove_loops(self, graph=None):
        """Remove loops from the graph """
        cp_graph = graph if graph else copy.deepcopy(self.nodes) # doesnt actually modify self.nodes

        for node in cp_graph:  # Use cp_graph instead of self.nodes
            no_loops = []

            for neighbor in cp_graph[node]:
                if neighbor[0] != node:  # Check if the neighbor is not the same as the node
                    no_loops.append(neighbor)

            cp_graph[node] = no_loops

        return cp_graph

    def remove_redundant_paths(self, graph=None):
        """Remove all redundant paths"""
        cp_graph = graph if graph else copy.deepcopy(self.nodes)

        # iterate over nodes
        for node in self.nodes:
            # dict to hold the cheapest of the duplicate paths (for each node)
            cheapest_paths = {}

            for neighbor, path_cost in self.nodes[node]:
                # determine if this path cost is cheaper than the currently stored one
                if neighbor in cheapest_paths:
                    if path_cost < cheapest_paths[neighbor]:
                        cheapest_paths[neighbor] = path_cost
                else:
                    cheapest_paths[neighbor] = path_cost

            cp_graph[node] = [(n, cost) for n, cost in cheapest_paths.items()]

        return cp_graph

    def getSortedEdges(self, nodes=None):
        """sorts by ascending order"""
        if not nodes:
            nodes = self.nodes

        edges = self.generate_edges(nodes)
        return sorted(edges,key=lambda path: path[2])


    def mst_kruskal(self):
        # Removing all loops and redundant paths
        processed = self.remove_redundant_paths(self.remove_loops(self.nodes))

        # Generating edges
        processed_edges = self.generate_edges(processed)

        # sort the edges in ascending order
        processed_edges=self.getSortedEdges(processed)


        # Sorting the edges by ascending order
        processed_edges.sort(key=lambda path: path[2])  # Edges are tuples (node_1, node_2, path cost)
        #print(processed_edges)


        # Connect the nodes together, store each node in a visited list to ensure that we don't add it again
        visited = []
        mst = []

        traversal_cost = 0

        for tup in processed_edges:
            ns, ne, ps = tup

            if ns not in visited or ne not in visited:
                mst.append(tup)

                # add the past cost to counter
                traversal_cost+=tup[2]
                visited.extend([ns, ne])

            if len(visited) == len(self.nodes):  # Fix here, use self.nodes instead of processed.nodes
                break  # Stop when all nodes are visited

        print(f"\nTotal Path Cost: {traversal_cost}")
        return mst

    def getStandardFrontier(self, nodes):
        out = {}  # will hold all nodes that are in the frontier but are pulled from self.nodes
        for node in nodes:
            if node not in out:
                out[node[0]] = self.nodes[node[0]]
        return out

    def updateFrontier(self, nodes, graph):
        out = {}

        for node in nodes:
            if node not in out.keys():
                out[node] = self.nodes[node]
        return out

    def mst_prims(self):
        """Prim's algorithm:
           1. Remove all loops
           2. Find the cheapest node to travel to from the start node
           3. Treat the currently connected series of nodes as a single 'node' and continue adding
              nodes with the cheapest path
        """
        # remove self loops
        no_loops = self.remove_loops(self.nodes)

        # setup visited list and frontier (holds nodes up next to be visited)
        visited = []
        mst = []
        frontier = {}

        # find the node with the cheapest path from no_loops to start
        start_edge = self.getSortedEdges(nodes=no_loops)[0]

        # Add the starting node to visited
        visited.append(start_edge[0])
        visited.append(start_edge[1])

        # add start point to output
        mst.append(start_edge)

        #  add starting node and neighbors to the frontier
        frontier = self.updateFrontier([start_edge[0], start_edge[1]], graph=no_loops)

        while len(visited) < len(self.nodes):

            # Find  neighbor with the cheapest path cost
            min_cost = float('inf') # setting up min cost with max value

            for node in visited:
                for neighbor, cost in no_loops[node]:

                    # if we havent visited the node, add it to the frontier
                    if neighbor not in visited and cost < min_cost:
                        # update the min cost and node to the one with the lowest cost and then set it to curr
                        min_cost = cost
                        curr = (node, neighbor, cost)

            # Add the current node to visited
            visited.append(curr[1])
            mst.append(curr)

            # Update the frontier with neighbors of the current node
            frontier = self.updateFrontier([curr[1]], graph=no_loops)

        print("\nTotal Path Cost: ", sum([x[2] for x in mst]))
        return mst

    def mst_djikstras(self, start_node=None):
        """Dijkstra's algorithm without priority queue:
            1. Mark all nodes as unvisited and put them into an unvisited set.
            2. Assign every node a tentative distance value (set to infinity for unvisited nodes and 0 for the initial node).
            3. Set the initial node as the current node.
            4. For the current node, consider all unvisited neighbors and calculate their tentative distances through the current node and assign.
               - If the distance was marked previously with a longer path, change it to the shortest one that's now found.
            5. If the destination node has been found OR the unvisited set is empty, HALT.
        """

        #  first node in our graph
        start_node = list(self.nodes.keys())[0]

        #  unvisited set with tentative distances
        distances = {node: float('infinity') for node in self.nodes}
        distances[start_node] = 0

        #   empty set for visited nodes
        visited = set()

        while True:
            # Find the unvisited node with the smallest tentative distance:

            # add in nodes from distances if not visited
            unvisited_nodes = [node for node in distances if node not in visited]

            # all nodes have been vitsed...
            if not unvisited_nodes:
                break

            # find the node with the lowest path cost from our current node
            current_node = min(unvisited_nodes, key=lambda node: distances[node])

            # Mark the current node as visited
            visited.add(current_node)

            # Update tentative distances for neighbors (distance up until now plus known path cost to this node)
            for neighbor, path_cost in self.nodes[current_node]:
                distance = distances[current_node] + path_cost

                # if shorter path is found then update the distance
                if distance < distances[neighbor]: # when starting well be comparing path cost to infinity
                    distances[neighbor] = distance

        # return all distnaces from start node
        return distances

# nodes will be in the form nodes = {'a': [(neighbor, pathcost)]}
test1 = {'a': [('b', 5), ('b', 1), ('c', 14)],
        'b': [('c', 4), ('d', 2)],
        'c': [('c', 3), ('d', 45)],
        'd': [('e', 5), ('b', 4), ('a', 4)],
        'e': [('b', 7)]
        }

test2 = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 5), ('D', 10)],
    'C': [('A', 2), ('B', 5), ('D', 3)],
    'D': [('B', 10), ('C', 3), ('E', 7)],
    'E': [('D', 7)]
}



g1 = Graph(test1)
g2= Graph(test2)


# Testing Graph 1
print(g1.mst_kruskal())
print(g1.mst_prims())
print("\nDijkstra Graph 1")
print(g1.mst_djikstras())

print("\n---------------------------------")

# Testing Graph 2
print(g2.mst_kruskal())
print(g2.mst_prims())
print("\nDijkstra Graph 2")
print(g2.mst_djikstras())
