# Imports
from random import choices, choice
from operator import attrgetter
import numpy as np

# Selection functions

def tournament(population, size=20):
    """
    Tournament selection implementation.

    :param population: Population to select from.
    :type population: Population
    :param int size: Size of the tournament.
    :return: Best individual in the tournament.
    :rtype: Individual
    """

    # Select individuals based on tournament size
    tournament = [choice(population.individuals) for i in range(size)]

    # Check if the problem is max or min
    if population.optim == 'max':
        return max(tournament, key=attrgetter('fitness'))
    elif population.optim == 'min':
        return min(tournament, key=attrgetter('fitness'))
    else:
        raise Exception("No optimization specified ('min' or 'max').")

def fitness_proportional(population):
    """
    Fitness proportional (aka 'roulette wheel') selection implementation.

    :param population: Population to select from.
    :type population: Population
    :return: Selected individual.
    :rtype: Individual
    """

    # Get the total fitness of the population
    total_fitness = sum([i.fitness for i in population])

    # Get the probability of each individual
    if population.optim == 'max':
        weights = [i.fitness/total_fitness for i in population]
    elif population.optim == 'min':
        weights = [1 - i.fitness/total_fitness for i in population]
        # Note that in the case of minimization, the weights don't
        # add up to 1, but it doesn't matter because we are interested in
        # the relative fitness of the individuals to make the draw.
    else:
        raise Exception("No optimization specified ('min' or 'max').")

    # Select an individual based on the probability
    return choices(population.individuals, weights=weights)[0]

def ranking(population):
    """
    Ranking selection implementation.

    :param population: Population to select from.
    :type population: Population
    :return: Selected individual.
    :rtype: Individual
    """

    # Sort the individuals by fitness
    if population.optim == 'max':
        sorted_population = sorted(population.individuals, key=attrgetter('fitness'))
    elif population.optim == 'min':
        sorted_population = sorted(population.individuals, key=attrgetter('fitness'), reverse=True)
    else:
        raise Exception("No optimization specified ('min' or 'max').")

    # Exponentially weighted ranking
    weights = [int(np.exp(i)) for i in range(len(sorted_population))]

    # Select an individual based on the probability
    return choices(sorted_population, weights=weights)[0]