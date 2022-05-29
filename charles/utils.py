# Imports
import networkx as nx
from random import choice
import numpy as np

# Define utlity functions
def random_path(G, origin_node, length=None):
  """
  Given a graph, `G`, and a lenth, `length`, start at the origin node
  and then randomly traverses the edges of the graph, taking the number
  of steps specified by `length`.
  """
  # If no length is specified, set it to the square of the number of
  # edges in the graph
  if length is None:
    length = int((len(G.edges())**2)/2)
  
  # Randomly traverse the edges of the graph
  path = [origin_node]

  for _ in range(length):
    neighbors = list(G.neighbors(path[-1]))    
    path.append(choice(neighbors))
  
  return path

def cap_path_at_origin(path, origin_node):
  """
  Given a path, `path`, and an origin node, `origin_node`,
  cap the path so that it ends at the last occurence of the
  origin node.
  """
  # Get the index of the last occurence of the origin node
  last_index = max(index for index, item in enumerate(path) if item == origin_node)

  return path[:last_index+1]

def path_is_valid(G, path):
  """
  Given a graph, `G`, and a path, `path`, return True if the path
  is valid and False otherwise. A path is valid if it contains a
  possible traversal of the graph (only edges that exist and in a
  valid order).
  """
  # Check if the path is valid
  for i in range(len(path)-1):
    if not G.has_edge(path[i], path[i+1]):
      return False
  
  return True

def path_weight(G, path):
  """
  Given a graph, `G`, and a path, `path`, return the weight of the
  path.
  """
  path_weight = sum(G[u][v]['weight'] for u, v in zip(path, path[1:]))
  return int(path_weight)

def path_contains_all_edges(G, path):
  """
  Given a graph, `G`, and a path, `path`, return True if the path
  contains all the edges of the graph and False otherwise.
  """
  # Extract the edges from the path
  path_edges = [{path[i], path[i+1]} for i in range(len(path)-1)]

  # Check if the path contains all the edges of the graph
  for u, v in G.edges():
    if {u, v} not in path_edges:
      return False
  
  return True

def get_fitness(self):
  """
  Given a graph, `G`, and a path, `path`, return the fitness of the
  path.

  The fitness of a path is given by the sum of the weights of the
  edges in the path. The smaller the fitness, the better the path.
  However, the fitness of a path also depends on other factors, such
  as:

  - Does the path start and end at the origin?
  - Does the path contain all the edges in the graph?
  - Is the path valid?
  """
  # Get the initial fitness of the path
  fitness = path_weight(self.target_graph, self.representation)

  # Penalize the fitness of the path depending on the other factors
  penalizations = 0
  penalization_list = []
  if self.representation[0] != self.origin_node:
    penalizations += int(1e6)
    penalization_list.append("Doesn't start at origin")
  if self.representation[-1] != self.origin_node:
    penalizations += int(1e6)
    penalization_list.append("Doesn't end at origin")
  if not path_contains_all_edges(self.target_graph, self.representation):
    penalizations += int(1e6)
    penalization_list.append("Doesn't contain all edges")
  if not path_is_valid(self.target_graph, self.representation):
    penalizations += int(1e6)
    penalization_list.append('Not valid path')
  
  fitness = fitness + penalizations
  self.penalizations = penalization_list

  return fitness