# Imports
from random import choice, sample
from charles.charles import Individual

# Crossover functions

def co_on_common_node(p1, p2):
  """
  Given two parent individuals, do a crossover between them by
  choosing a random node they have in common, and then swapping
  the paths that lead into and out of this node between the two
  parents.

  :param p1: The first parent.
  :param p2: The second parent.
  :return: Two crossed-over offspring.
  """

  # Find a random node they have in common (remember that two
  # valid individuals should have all nodes in common).
  common_nodes = set(p1.representation).intersection(p2.representation)
  if not common_nodes:
    raise Exception("No common nodes between parents.")
  
  # Choose a random node they have in common
  common_node = choice(list(common_nodes))

  # In each parent, get the indices of all occurrences of the
  # common node.
  p1_common_node_indices = [i for i, x in enumerate(p1.representation) if x == common_node]
  p2_common_node_indices = [i for i, x in enumerate(p2.representation) if x == common_node]

  # In each parent, pick a random index from the list of indices
  # of the common node.
  p1_common_node_index = choice(p1_common_node_indices)
  p2_common_node_index = choice(p2_common_node_indices)

  # Swap the paths that lead into and out of the common node of
  # the two parents.
  p1_path_before_common_node = p1.representation[:p1_common_node_index]
  p1_path_after_common_node = p1.representation[p1_common_node_index:]
  p2_path_before_common_node = p2.representation[:p2_common_node_index]
  p2_path_after_common_node = p2.representation[p2_common_node_index:]

  offspring1 = p1_path_before_common_node + p2_path_after_common_node
  offspring2 = p2_path_before_common_node + p1_path_after_common_node

  offspring1 = Individual(target_graph=p1.target_graph, representation=offspring1)
  offspring2 = Individual(target_graph=p2.target_graph, representation=offspring2)

  return offspring1, offspring2

# def co_on_two_common_nodes(p1, p2):
#   return None

def co_on_two_common_nodes(p1, p2):
  """
  Given two parent individuals, do a crossover between them by
  choosing two random nodes they have in common, breaking each
  parent into 3 parts (start, middle and end) and then swapping
  the middle paths of the two parents.

  :param p1: The first parent.
  :param p2: The second parent.
  :return: Two crossed-over offspring.
  """

  # Find two random nodes they have in common (remember that two
  # valid individuals should have all nodes in common).
  common_nodes = set(p1.representation).intersection(p2.representation)
  if len(common_nodes) < 2:
    return p1, p2

  two_nodes = sample(list(common_nodes), 2)

  # In each parent, get the indices of all occurrences of the two common nodes
  p1_1st_common_node_indices = [i for i, x in enumerate(p1.representation) if x == two_nodes[0]]
  p2_1st_common_node_indices = [i for i, x in enumerate(p2.representation) if x == two_nodes[0]]
  p1_2nd_common_node_indices = [i for i, x in enumerate(p1.representation) if x == two_nodes[1]]
  p2_2nd_common_node_indices = [i for i, x in enumerate(p2.representation) if x == two_nodes[1]]

  # In each parent, pick a random index from the list of indices
  # of the common node.
  p1_1st_common_node_index = choice(p1_1st_common_node_indices)
  p2_1st_common_node_index = choice(p2_1st_common_node_indices)
  p1_2nd_common_node_index = choice(p1_2nd_common_node_indices)
  p2_2nd_common_node_index = choice(p2_2nd_common_node_indices)

  # In each parent make sure the 1st node comes before the 2nd node
  if p1_1st_common_node_index > p1_2nd_common_node_index:
    p1_1st_common_node_index, p1_2nd_common_node_index = p1_2nd_common_node_index, p1_1st_common_node_index

  if p2_1st_common_node_index > p2_2nd_common_node_index:
    p2_1st_common_node_index, p2_2nd_common_node_index = p2_2nd_common_node_index, p2_1st_common_node_index
  
  # Break the two parents in three (start, middle and end), and swap the
  # middle paths of the two parents.
  p1_start_path = p1.representation[:p1_1st_common_node_index+1]
  p1_middle_path = p1.representation[p1_1st_common_node_index+1:p1_2nd_common_node_index]
  p1_end_path = p1.representation[p1_2nd_common_node_index:]

  p2_start_path = p2.representation[:p2_1st_common_node_index+1]
  p2_middle_path = p2.representation[p2_1st_common_node_index+1:p2_2nd_common_node_index]
  p2_end_path = p2.representation[p2_2nd_common_node_index:]

  if (p1_start_path[-1] != p2_start_path[-1]):
    p1_middle_path.reverse()
    p2_middle_path.reverse()

  offspring1 = p1_start_path + p2_middle_path + p1_end_path
  offspring2 = p2_start_path + p1_middle_path + p2_end_path

  offspring1 = Individual(target_graph=p1.target_graph, representation=offspring1)
  offspring2 = Individual(target_graph=p2.target_graph, representation=offspring2)

  return offspring1, offspring2