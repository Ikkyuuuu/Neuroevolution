# agent.py — Agent with perception, neural net brain, and energy

import numpy as np
from config import (
    GRID_WIDTH, GRID_HEIGHT, PERCEPTION_RADIUS,
    ENERGY_INIT, ENERGY_MAX, ENERGY_PER_STEP,
    ENERGY_FROM_FOOD, ENERGY_DEATH_THRESHOLD,
    USE_ENERGY_INPUT, USE_AGE_INPUT, AGE_LIMIT
)
from genome import genome_to_net, random_genome

# Action index → (dy, dx)
ACTIONS = {
    0: (-1, 0),  # up
    1: (1, 0),   # down
    2: (0, -1),  # left
    3: (0, 1),   # right
}


class Agent:
    def __init__(self, genome=None, x=None, y=None):
        # Position
        self.x = x if x is not None else np.random.randint(0, GRID_WIDTH)
        self.y = y if y is not None else np.random.randint(0, GRID_HEIGHT)

        # Genome + brain
        self.genome = genome if genome is not None else random_genome()
        self.brain = genome_to_net(self.genome)

        # State
        self.energy = ENERGY_INIT
        self.age = 0
        self.alive = True
        self.fitness = 0.0

    def perceive(self, food_grid: np.ndarray) -> np.ndarray:
        """
        Build input vector from local food window + optional energy/age.
        Returns a 1D numpy array.
        """
        r = PERCEPTION_RADIUS
        window_size = (2 * r + 1) ** 2
        perception = np.zeros(window_size)

        idx = 0
        for dy in range(-r, r + 1):
            for dx in range(-r, r + 1):
                ny = (self.y + dy) % GRID_HEIGHT
                nx = (self.x + dx) % GRID_WIDTH
                perception[idx] = food_grid[ny, nx]
                idx += 1

        extras = []
        if USE_ENERGY_INPUT:
            extras.append(self.energy / ENERGY_MAX)   # normalized [0,1]
        if USE_AGE_INPUT:
            max_age = AGE_LIMIT if AGE_LIMIT else 500
            extras.append(min(self.age / max_age, 1.0))

        if extras:
            return np.concatenate([perception, extras])
        return perception

    def step(self, food_grid: np.ndarray):
        """
        One simulation step:
          1. Perceive environment
          2. Decide action via neural net
          3. Move
          4. Eat food if present
          5. Lose energy (cost of living)
          6. Update fitness & check death
        """
        if not self.alive:
            return

        # 1. Perceive + decide
        inputs = self.perceive(food_grid)
        action = self.brain.forward(inputs)

        # 2. Move (toroidal grid)
        dy, dx = ACTIONS[action]
        self.y = (self.y + dy) % GRID_HEIGHT
        self.x = (self.x + dx) % GRID_WIDTH

        # 3. Eat food
        if food_grid[self.y, self.x] > 0:
            self.energy = min(self.energy + ENERGY_FROM_FOOD, ENERGY_MAX)
            food_grid[self.y, self.x] = 0.0

        # 4. Living cost
        self.energy += ENERGY_PER_STEP
        self.age += 1

        # 5. Accumulate fitness
        self.fitness += self.energy

        # 6. Death checks
        if self.energy <= ENERGY_DEATH_THRESHOLD:
            self.alive = False
        if AGE_LIMIT and self.age >= AGE_LIMIT:
            self.alive = False