# Imports
from charles.charles import Individual
from random import randint, choice

# Mutation functions

def tail_mutation(individual):
  """
  Mutate the tail of an individual by picking a random node in
  the path, and then randomly traversing the graph until we are
  back at the origin.

  :param Individual individual: Individual to mutate.
  :return: The mutated individual.
  :rtype: Individual
  """
  # Pick a random node in the path
  rand_node_index = randint(0, len(individual) - 1)
  rand_node = individual[rand_node_index]

  # Starting at the random node, randomly traverse the graph until
  # we are back at the origin
  random_path = [rand_node]
  while (random_path[-1] != individual.origin_node) or (len(random_path) < 2):
    neighbors = list(individual.target_graph.neighbors(random_path[-1]))
    random_path.append(choice(neighbors))

  mutated_individual = individual[:rand_node_index] + random_path
  mutated_individual = Individual(
    target_graph=individual.target_graph,
    representation=mutated_individual
  )

  return mutated_individual

def middle_mutation(individual):
  """
  Mutate a random sub-path in the middle of an individual by
  picking a random start and end nodes and randomly traversing
  the graph between them.

  :param Individual individual: Individual to mutate.
  :return: The mutated individual.
  :rtype: Individual
  """

  # Pick a random start and end node (it's okay if they are the same)
  rand_start_index = randint(0, len(individual) - 1)
  rand_end_index = randint(0, len(individual) - 1)
  # Order the indices so that the start node is always before the end node
  if rand_start_index > rand_end_index:
    rand_start_index, rand_end_index = rand_end_index, rand_start_index
  rand_start = individual[rand_start_index]
  rand_end = individual[rand_end_index]

  # Starting at the random start node, randomly traverse the graph
  # until we are back at the random end node
  random_path = [rand_start]
  while (random_path[-1] != rand_end) or (len(random_path) < 2):
    neighbors = list(individual.target_graph.neighbors(random_path[-1]))
    random_path.append(choice(neighbors))

  mutated_individual = individual[:rand_start_index] + random_path + individual[rand_end_index + 1:]

  mutated_individual = Individual(
    target_graph=individual.target_graph,
    representation=mutated_individual
  )

  return mutated_individual