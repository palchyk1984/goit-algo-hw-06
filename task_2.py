from collections import deque

# Створення графа як словника
social_network = {
    1: [2, 3, 4, 10],
    2: [1, 5, 6],
    3: [1, 7],
    4: [1, 8],
    5: [2, 9],
    6: [2, 10],
    7: [3, 10],
    8: [4, 9],
    9: [5, 8, 10],
    10: [6, 7, 9, 1]
}

# Реалізація DFS
def dfs(graph, start):
    visited = set()
    path = []

    def dfs_recursive(vertex):
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            for neighbor in graph[vertex]:
                dfs_recursive(neighbor)

    dfs_recursive(start)
    return path

# Реалізація BFS
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    path = []

    while queue:
        vertex = queue.popleft()
        path.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return path

# Знаходження шляхів за допомогою DFS
dfs_path = dfs(social_network, 1)
print("Шляхи DFS:", dfs_path)

# Знаходження шляхів за допомогою BFS
bfs_path = bfs(social_network, 1)
print("Шляхи BFS:", bfs_path)
