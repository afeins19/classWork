"""
Write a class for graph data structure containing the following functions:

1. Function to generate the list of all edges
2. Function to calculate isolated hubs of a given graph
3. Function to find a path from a start vertex to an end vertex
4. Function to find all the paths between a start vertex to an end vertex
5. Function to check if a graph is a connected graph.
6. Function to perform BFS
7. Function to perform DFS
"""

example_graph = {
    "a": ["b", "c"],
    "b": ["a", "c", "d"],
    "c": ["a", "b", "d", "e"],
    "d": ["b", "c", "e"],
    "e": ["c", "d"]
}

class graph:
    def __init__(self, nodes):
        self.nodes = nodes

    # Function to generate the list of all edges
    def generate_edges(self):
        edges = []

        for node in self.nodes:
            for neighbour in self.nodes[node]:
                edges.append((node, neighbour))
        return edges

    # Function to calculate isolated hubs of a given graph
    def find_isolated_nodes(self):
        """ returns a list of isolated hubs. """
        isolated = []

        for node in self.nodes:
            if not self.nodes[node]:
                isolated += node
        return isolated

    # Function to find a path from a start vertex to an end vertex
    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex in graph """

        if path == None:
            path = []

        path = path + [start_vertex]

        if start_vertex == end_vertex:
            return path

        if start_vertex not in self.nodes:
            return None

        for vertex in self.nodes[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)

                if extended_path:
                    return extended_path

        return None


        # Function to check if a graph is a connected graph.

    def is_connected(self, vertices_encountered=None, start_vertex=None):
        """ determines if the graph is connected """

        if vertices_encountered is None:
            vertices_encountered = set()
        vertices = list(self.nodes.keys())  # "list" necessary in Python 3

        if not start_vertex:
            # choose a vertex from graph as a starting point
            start_vertex = vertices[0]
            vertices_encountered.add(start_vertex)
            if len(vertices_encountered) != len(vertices):
                for vertex in self.nodes[start_vertex]:
                    if vertex not in vertices_encountered:
                        if self.is_connected(vertices_encountered, vertex):
                            return True
                    else:
                        return True
        return False


    def find_all_paths(self, start_vertex, end_vertex, path=None):
        """Find all paths from start_vertex to end_vertex in graph."""
        if path is None:
            path = []
        path = path + [start_vertex]

        if start_vertex == end_vertex:
            return [path]

        if start_vertex not in self.nodes:
            return []

        paths = []
        for vertex in self.nodes[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path.copy())
                for p in extended_paths:
                    paths.append(p)
        return paths

    def bfs(self, start_node):
        """
            1. visit a node
            2. save to visited list
            3. append neighbors to queue
        """
        queue = []
        visited = []

        # put start node into the queue
        queue.append(start_node)

        while queue:
            cur = queue.pop(0)
            if cur not in visited:

                visited.append(cur)
                queue.extend(self.nodes[cur]) # add child hubs to the queue... will be visited after hubs on same level

        print("\nBFS Traversal: ")
        self.print_paths(paths=[visited])

    def dfs(self, start_node):
        """same idea as bfs but use a stack to sequence node visitation"""
        # using a list to model a stack...child node at top of stack is visited next
        stack = [start_node]
        visited = []

        while stack:
            cur = stack.pop()

            if cur not in visited:
                visited.append(cur)
                stack.extend(self.nodes[cur])

        print("\nDFS Traversal: ")
        self.print_paths(paths=[visited])
    def mst_djikstras(self, start_node=None):
        """Dijkstra's algorithm without priority queue:
            1. Mark all hubs as unvisited and put them into an unvisited set.
            2. Assign every node a tentative distance value (set to infinity for unvisited hubs and 0 for the initial node).
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

        #   empty set for visited hubs
        visited = set()

        while True:
            # Find the unvisited node with the smallest tentative distance:

            # add in hubs from distances if not visited
            unvisited_nodes = [node for node in distances if node not in visited]

            # all hubs have been vitsed...
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


    def print_paths(self, paths = []):
        for p in paths:
            print(" -> ".join(p), end = '\n')


example_graph = {
    "a": ["b", "c"],
    "b": ["a", "c", "d"],
    "c": ["a", "b", "d", "e"],
    "d": ["b", "c", "e"],
    "e": ["c", "d"]
}


g1 = graph(example_graph)
edges = g1.generate_edges()
print(edges)

adpaths = g1.find_all_paths('a','d')
g1.print_paths(adpaths)


g1.bfs('a')
g1.dfs('a')


ex3_graph = {
    '1': ['2', '3', '6'],
    '2': ['3'],
    '3': ['4', '6'],
    '4': ['5'],
    '5': ['6'],
    '6': ['4']
}

lab8_exercise_2 = {
    'a' : ['b', 'c', 'f'],
    'b' : ['a', 'd', 'e'],
    'c' : ['b', 'f'],
    'd' : ['a', 'e', 'f'],
    'e' : ['a', 'd'],
    'f' : ['b', 'e']
}

print("\n\n\n\n\nLABB 8")
k = graph(lab8_exercise_2)
k.bfs('a')
k.dfs('a')