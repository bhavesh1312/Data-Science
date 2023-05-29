from collections import deque

# Function to perform Depth First Search
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Function to perform Breadth First Search
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Function to construct the graph based on user input
def construct_graph():
    graph = {}
    n = int(input("Enter the number of nodes: "))

    for i in range(1, n+1):
        node = input("Enter node {}: ".format(i))
        edges = input("Enter the child nodes of {}: ".format(node))
        graph[node] = edges.split()

    return graph

# Example usage:
print("Construct the graph:")
graph = construct_graph()

start_node = input("Enter the starting node: ")

print("DFS traversal:")
dfs(graph, start_node)

print("\nBFS traversal:")
bfs(graph, start_node)
