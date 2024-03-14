import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин і ребер
# Припустимо, що маємо 10 людей у соціальній мережі
nodes = range(1, 11)
G.add_nodes_from(nodes)

# Додавання ребер між деякими вершинами для імітації взаємозв'язків
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 9), (6, 10), (7, 1), (8, 9), (9, 10)]
G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, edge_color='k')
plt.title('Граф соціальної мережі')
plt.show()

# Основні характеристики графа
number_of_nodes = G.number_of_nodes()
number_of_edges = G.number_of_edges()
average_degree = sum(dict(G.degree()).values()) / number_of_nodes

# Виведення основних характеристик
print(f'Кількість вершин: {number_of_nodes}')
print(f'Кількість ребер: {number_of_edges}')
print(f'Середній ступінь вершин: {average_degree:.2f}')
