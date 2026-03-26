# genetic_algorithm.py — Selection, reproduction, population management

import numpy as np
import random
from config import (
    POPULATION_SIZE, ELITE_FRACTION, RANDOM_SURVIVOR_FRACTION
)
from genome import clone, mutate
from agent import Agent


def run_selection_and_reproduction(agents: list) -> list:
    """
    Given the current population (some may be dead), produce the next generation:
      1. Sort by fitness (descending)
      2. Keep elite fraction
      3. Add random survivors for diversity
      4. Fill remainder by cloning+mutating elites
    Returns a new list of Agent objects.
    """
    # Sort all agents by fitness (dead agents have low fitness)
    sorted_agents = sorted(agents, key=lambda a: a.fitness, reverse=True)

    n_elite = max(1, int(POPULATION_SIZE * ELITE_FRACTION))
    n_random = max(1, int(POPULATION_SIZE * RANDOM_SURVIVOR_FRACTION))

    elites = sorted_agents[:n_elite]

    # Random survivors from the non-elite pool
    pool = sorted_agents[n_elite:]
    random_survivors = random.sample(pool, min(n_random, len(pool))) if pool else []

    survivors = elites + random_survivors

    # Fill the rest by cloning and mutating from elites
    next_generation = []
    for agent in survivors:
        new_genome = mutate(clone(agent.genome))
        new_agent = Agent(genome=new_genome)
        next_generation.append(new_agent)

    while len(next_generation) < POPULATION_SIZE:
        parent = random.choice(elites)
        new_genome = mutate(clone(parent.genome))
        next_generation.append(Agent(genome=new_genome))

    return next_generation[:POPULATION_SIZE]


def population_stats(agents: list) -> dict:
    """Compute stats for logging/visualization."""
    fitnesses = [a.fitness for a in agents]
    alive = [a for a in agents if a.alive]
    return {
        "alive": len(alive),
        "avg_fitness": np.mean(fitnesses),
        "max_fitness": np.max(fitnesses),
        "min_fitness": np.min(fitnesses),
        "avg_energy": np.mean([a.energy for a in alive]) if alive else 0.0,
    }