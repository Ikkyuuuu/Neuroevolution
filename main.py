# main.py — Entry point (enhanced stats + cleaner logging)

import numpy as np
from config import POPULATION_SIZE, GENERATION_STEPS
from agent import Agent
from environment import Environment
from genetic_algorithm import population_stats, enforce_population_floor, can_reproduce
from visualizer import Visualizer

def initialize_population() -> list:
    return [Agent() for _ in range(POPULATION_SIZE)]

def run():
    print("=== Artificial Life Simulation (Continuous Reproduction) ===")
    print(f"Population: {POPULATION_SIZE} | Steps: {GENERATION_STEPS}\n")
    print("Speed buttons: 1x / 5x / 10x / 50x — click on the figure window\n")

env = Environment()
agents = initialize_population()
viz = Visualizer()

for step in range(1, GENERATION_STEPS + 1):

    # 1. Respawn food
    env.respawn_food()

    # 2. Step agents + reproduction
    newborns = []
    for agent in agents:
        agent.step(env.food_grid)

        if agent.wants_to_reproduce and can_reproduce(agents):
            try:
                child = agent.reproduce()
                newborns.append(child)
            except Exception as e:
                print(f"[WARN] reproduction failed: {e}")

    # 3. Update population
    agents.extend(newborns)
    agents = [a for a in agents if a.alive]

    # 4. Population floor safety net
    agents = enforce_population_floor(agents)

    # 5. Visualization (respects speed buttons)
    if step % viz.render_interval == 0:
        stats = population_stats(agents)
        viz.update(env.food_grid, agents, step, stats)

    # 6. Console logging (every 100 steps)
    if step % 100 == 0:
        stats = population_stats(agents)

        # Safe access (in case stats missing fields)
        alive        = stats.get("alive", 0)
        avg_fit      = stats.get("avg_fitness", 0)
        avg_energy   = stats.get("avg_energy", 0)

        max_w = stats.get("max_weight", 0)
        avg_w = stats.get("avg_weight", 0)
        min_w = stats.get("min_weight", 0)

        max_b = stats.get("max_bias", 0)
        avg_b = stats.get("avg_bias", 0)
        min_b = stats.get("min_bias", 0)

        weight_std = stats.get("weight_std", 0)

        print(
            f"Step {step:>5} | "
            f"Alive: {alive:>4} | "
            f"Fit: {avg_fit:>7.2f} | "
            f"Energy: {avg_energy:>6.2f} | "
            f"W[max:{max_w:>6.2f} avg:{avg_w:>6.2f} min:{min_w:>6.2f} std:{weight_std:>6.2f}] | "
            f"B[max:{max_b:>6.2f} avg:{avg_b:>6.2f} min:{min_b:>6.2f}] | "
            f"Newborns: {len(newborns):>3}"
        )

print("\n✓ Simulation complete.")
viz.close()

if __name__ == "__main__":
    run()
