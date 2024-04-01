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

def dfs(graph):
    dfs_stack = [list(graph.keys())[0]] # queue will be treated as a stack
    visited = []

    while len(dfs_stack) > 0:
        cur = dfs_stack.pop()

        for child in graph[cur]:
            if child not in visited:
                dfs_stack.append(child)

        if cur not in visited:
            visited.append(cur)

    return visited

print("Running DFS: \n")

print("\ngraph 1: ")
for node in dfs(graph1):
    print("-> " + node+" ", end="")

print("\n\ngraph 2: ")
for node in dfs(graph2):
    print("-> " + node+" ", end="")




