# genetic_algorithm.py — Population floor guardian (no more generational GA)
# Reproduction now happens agent-by-agent inside the main loop.
# This module only handles: stats + emergency respawning if population collapses.

import numpy as np
from config import MIN_POPULATION, MAX_POPULATION
from agent import Agent


def population_stats(agents: list) -> dict:
    """Compute stats for logging/visualization."""
    alive = [a for a in agents if a.alive]
    fitnesses = [a.fitness for a in agents]
    return {
        "alive": len(alive),
        "total": len(agents),
        "avg_fitness": float(np.mean(fitnesses)) if fitnesses else 0.0,
        "max_fitness": float(np.max(fitnesses)) if fitnesses else 0.0,
        "avg_energy": float(np.mean([a.energy for a in alive])) if alive else 0.0,
    }


def enforce_population_floor(agents: list) -> list:
    """
    If population drops below MIN_POPULATION, inject fresh random agents.
    This acts as an extinction safety net.
    """
    alive = [a for a in agents if a.alive]
    while len(alive) < MIN_POPULATION:
        alive.append(Agent())
    return alive


def can_reproduce(agents: list) -> bool:
    """True if population is below the ceiling."""
    alive_count = sum(1 for a in agents if a.alive)
    return alive_count < MAX_POPULATION