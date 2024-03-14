import heapq

# Визначення графа з вагами ребер
graph = {
    1: {2: 2, 3: 2, 4: 7, 10: 2},
    2: {1: 2, 5: 3, 6: 1},
    3: {1: 2, 7: 2},
    4: {1: 7, 8: 5},
    5: {2: 3, 9: 4},
    6: {2: 1, 10: 1},
    7: {3: 2, 10: 1},
    8: {4: 5, 9: 8},
    9: {5: 4, 8: 8, 10: 1},
    10: {1: 2, 6: 1, 7: 1, 9: 1}
}

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # Оновлення відстаней для сусідів
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_vertices

# Пошук шляху
def reconstruct_path(start, end, previous_vertices):
    path = []
    current_vertex = end
    while current_vertex != start:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    path.append(start)
    path.reverse()
    return path

# Запускаємо алгоритм Дейкстри з вершини 1
shortest_distances, previous_vertices = dijkstra(graph, 1)
paths = {vertex: reconstruct_path(1, vertex, previous_vertices) for vertex in graph}

print("Найкоротші відстані від вершини 1 до інших вершин:")
for vertex, distance in shortest_distances.items():
    print(f"До {vertex}: {distance}")

print("\nНайкоротші шляхи від вершини 1 до інших вершин:")
for vertex, path in paths.items():
    print(f"Шлях до {vertex}: {' -> '.join(map(str, path))}")
