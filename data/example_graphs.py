# Imports
import networkx as nx

# Create examples graphs
## Graph 1 - Fitness of optimal solution: 13
g1 = nx.Graph()
g1.add_nodes_from(list('ABCD'))
g1.add_weighted_edges_from([
  ('A', 'B', 1.0),
  ('A', 'C', 1.0),
  ('A', 'D', 3.0),
  ('B', 'C', 2.0),
  ('C', 'D', 5.0)
])

## Graph 2 - Fitness of optimal solution: 28
g2 = nx.Graph()
g2.add_nodes_from(list('ABCDEF'))
g2.add_weighted_edges_from([
  ('A', 'B', 1.0),
  ('A', 'C', 5.0),
  ('A', 'D', 3.0),
  ('B', 'C', 2.0),
  ('C', 'E', 4.0),
  ('D', 'E', 6.0),
  ('D', 'F', 1.0),
  ('E', 'F', 1.0)
])

## Graph 3
g3 = nx.Graph()
g3.add_nodes_from(list('ABCDEF'))
g3.add_weighted_edges_from([
  ('A', 'B', 10.0),
  ('A', 'C', 20.0),
  ('A', 'E', 12.0),
  ('B', 'D', 50.0),
  ('B', 'E', 10.0),
  ('C', 'D', 20.0),
  ('C', 'E', 33.0),
  ('C', 'F', 22.0),
  ('D', 'E', 5.0),
  ('D', 'F', 12.0),
  ('E', 'F', 1.0)
])

## Graph 4
g4 = nx.Graph()
g4.add_nodes_from(list('ABCDEFGHIJK'))
g4.add_weighted_edges_from([
  ('A', 'B', 10.0),
  ('A', 'C', 9.0),
  ('A', 'E', 2.0),
  ('B', 'D', 5.0),
  ('B', 'E', 10.0),
  ('C', 'D', 10.0),
  ('C', 'E', 7.0),
  ('C', 'F', 8.0),
  ('D', 'E', 5.0),
  ('D', 'F', 12.0),
  ('E', 'F', 1.0),
  ('E', 'G', 1.0),
  ('F', 'G', 1.0),
  ('F', 'H', 8.0),
  ('G', 'H', 1.0),
  ('G', 'I', 10.0),
  ('H', 'I', 1.0),
  ('H', 'J', 1.0),
  ('I', 'J', 4.0),
  ('I', 'K', 3.0),
  ('J', 'K', 1.0),
  ('J', 'A', 1.0),
  ('K', 'D', 5.0),
  ('K', 'E', 3.0),
  ('K', 'B', 1.0),
  ('I', 'C', 1.0)
])