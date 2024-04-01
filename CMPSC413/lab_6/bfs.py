graph1 = { "a" : ["d","f"],
"b" : ["c"],
"c" : ["b", "c", "d", "e"],
"d" : ["a", "c"],
"e" : ["c"],
"f" : ["a"]}

graph2 = { "a" : ["d","f"],
"b" : ["c","b"],
"c" : ["b", "c", "d", "e"],
"d" : ["a", "c"],
"e" : ["c"],
"f" : ["a"]}

def bfs(graph):
    root =  list(graph.keys())[0]
    bfs_queue = [root]
    visited = []

    while len(bfs_queue) > 0:
        # get first node in the queue
        cur = bfs_queue.pop()

        for child in graph[cur]:

            if child not in visited:
                bfs_queue = [child] + bfs_queue # FIFO ordering

        if cur not in visited:
            visited.append(cur)

    return visited

print("Running BFS:")

print("\ngraph 1: ")
for node in bfs(graph1):
    print("-> " + node+" ", end="")

print("\n\ngraph 2: ")
for node in bfs(graph2):
    print("-> " + node+" ", end="")
