# main.py — Entry point: wires everything together

import numpy as np
from config import (
    POPULATION_SIZE, GENERATION_STEPS, NUM_GENERATIONS, VIZ_INTERVAL
)
from agent import Agent
from environment import Environment
from genetic_algorithm import run_selection_and_reproduction, population_stats
from visualizer import Visualizer


def initialize_population() -> list:
    return [Agent() for _ in range(POPULATION_SIZE)]


def run():
    print("=== Artificial Life Simulation ===")
    print(f"Grid: {__import__('config').GRID_WIDTH}x{__import__('config').GRID_HEIGHT} | "
          f"Population: {POPULATION_SIZE} | Generations: {NUM_GENERATIONS}\n")

    env = Environment()
    agents = initialize_population()
    viz = Visualizer()

    for generation in range(1, NUM_GENERATIONS + 1):
        env.reset()

        # Reset agent state but keep their genomes
        for agent in agents:
            agent.energy = __import__('config').ENERGY_INIT
            agent.age = 0
            agent.alive = True
            agent.fitness = 0.0
            agent.x = np.random.randint(0, __import__('config').GRID_WIDTH)
            agent.y = np.random.randint(0, __import__('config').GRID_HEIGHT)

        # --- Run one generation ---
        for step in range(GENERATION_STEPS):
            env.respawn_food()

            for agent in agents:
                agent.step(env.food_grid)

            # Visualize every VIZ_INTERVAL generations, every step
            if generation % VIZ_INTERVAL == 0:
                stats = population_stats(agents)
                viz.update(env.food_grid, agents, generation, step, stats)

        # --- End of generation ---
        stats = population_stats(agents)
        viz.update_stats(generation, stats)

        print(
            f"Gen {generation:>4} | "
            f"Alive: {stats['alive']:>3} | "
            f"Avg Fit: {stats['avg_fitness']:>8.1f} | "
            f"Max Fit: {stats['max_fitness']:>8.1f} | "
            f"Avg Energy: {stats['avg_energy']:>6.1f}"
        )

        # --- Evolve ---
        agents = run_selection_and_reproduction(agents)

    print("\n✓ Simulation complete.")
    viz.close()


if __name__ == "__main__":
    run()