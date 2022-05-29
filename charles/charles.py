# Imports
from charles.utils import random_path, cap_path_at_origin
from data.example_graphs import *
from operator import attrgetter
from random import random
from copy import deepcopy

# Define classes

class Individual:
  def __init__(
    self,
    target_graph=None,
    representation=None,
    origin_node='A',
    penalizations=None,
  ):

    self.target_graph = target_graph
    self.origin_node = origin_node
    self.penalizations = penalizations

    if representation is None:
      self.representation = cap_path_at_origin(random_path(target_graph, origin_node), origin_node)
    else:
      self.representation = representation
    
    self.fitness = self.get_fitness()

  def get_fitness(self):
    raise Exception("You need to monkey patch the fitness method.")

  def __len__(self):
    return len(self.representation)

  def __getitem__(self, position):
    return self.representation[position]

  def __setitem__(self, position, value):
    self.representation[position] = value

  def __repr__(self):
    return f"Individual(\n  Path: {' → '.join(self.representation)}\n  Fitness: {self.fitness}\n)"

class Population:
  def __init__(
    self,
    size,
    target_graph,
    optim,
    **kwargs,
  ):

    self.individuals = []
    self.size = size
    self.target_graph = target_graph
    self.optim = optim

    for _ in range(size):
      self.individuals.append(
        Individual(target_graph=target_graph)
      )

  def evolve(
    self,
    gens,
    select,
    crossover,
    mutate,
    co_p,
    mu_p,
    elitism,
    verbose=False
  ):
    """
    Method to evolve the population for a given number of generations,
    with a given selection method, crossover, mutation, and elitism.
    
    Parameters:
    
    :param int gens: The number of generations to evolve the population for.
    :param func select: The selection method to use.
    :param func crossover: The crossover method to use.
    :param mutate: The mutation method to use.
    :param co_p: The crossover probability.
    :param mu_p: The mutation probability.
    :param bool elitism: Whether to use elitism.
    :param bool verbose: Whether to print the best individual in each generation.
    """

    # Keep track of the best individual in each generation, and the its fitness.
    evolution_log = []

    for gen in range(gens):
      new_pop = []

      if elitism:
        if self.optim == 'max':
          elite = deepcopy(max(self.individuals, key=attrgetter('fitness')))
        elif self.optim == 'min':
          elite = deepcopy(min(self.individuals, key=attrgetter('fitness')))

      while len(new_pop) < self.size:
        # Selection
        parent1, parent2 = select(self), select(self)
        # Crossover
        if random() < co_p:
          offspring1, offspring2 = crossover(parent1, parent2)
        else:
          offspring1, offspring2 = parent1, parent2
        # Mutation
        if random() < mu_p:
          offspring1 = mutate(offspring1)
        if random() < mu_p:
          offspring2 = mutate(offspring2)

        new_pop.append(offspring1)
        
        if len(new_pop) < self.size:
          new_pop.append(offspring2)

      if elitism:
        if self.optim == 'max':
          least = min(new_pop, key=attrgetter('fitness'))
        elif self.optim == 'min':
          least = max(new_pop, key=attrgetter('fitness'))
        new_pop.pop(new_pop.index(least))
        new_pop.append(elite)

      self.individuals = new_pop

      if self.optim == 'max':
        best_individual = max(self, key=attrgetter('fitness'))        
      elif self.optim == 'min':
        best_individual = min(self, key=attrgetter('fitness'))
      
      if verbose:
        print(f'Best Individual: {best_individual}')

      evolution_log.append([
        gen + 1,
        best_individual.fitness,
        best_individual.representation
      ])
    
    return evolution_log

  def __len__(self):
    return len(self.individuals)

  def __getitem__(self, position):
    return self.individuals[position]

  def __repr__(self):
    return f"Population(Size: {len(self.individuals)})"