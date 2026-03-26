# agent.py — Agent with perception, neural net brain, energy, color lineage

import numpy as np
from config import (
    GRID_WIDTH, GRID_HEIGHT, PERCEPTION_RADIUS,
    ENERGY_INIT, ENERGY_MAX, ENERGY_PER_STEP,
    ENERGY_FROM_FOOD, ENERGY_DEATH_THRESHOLD,
    USE_ENERGY_INPUT, USE_AGE_INPUT, AGE_LIMIT,
    REPRODUCE_ENERGY_THRESHOLD, REPRODUCE_ENERGY_COST,
    CHILD_ENERGY_START, COLOR_MUTATION_STRENGTH
)
from genome import genome_to_net, random_genome, clone, mutate

# Action index → (dy, dx) | index 4 = reproduce
ACTIONS = {
    0: (-1, 0),   # up
    1: (1, 0),    # down
    2: (0, -1),   # left
    3: (0, 1),    # right
    # 4 = reproduce (handled separately)
}


def _random_color() -> np.ndarray:
    """Random RGB color in [0, 255]."""
    return np.random.randint(0, 256, size=3, dtype=np.int32)


def _mutate_color(color: np.ndarray) -> np.ndarray:
    """Shift RGB channels slightly, clamp to [0, 255]."""
    delta = np.random.randint(
        -COLOR_MUTATION_STRENGTH,
        COLOR_MUTATION_STRENGTH + 1,
        size=3
    )
    return np.clip(color + delta, 0, 255).astype(np.int32)


class Agent:
    def __init__(self, genome=None, x=None, y=None, color=None):
        # Position
        self.x = x if x is not None else np.random.randint(0, GRID_WIDTH)
        self.y = y if y is not None else np.random.randint(0, GRID_HEIGHT)

        # Genome + brain
        self.genome = genome if genome is not None else random_genome()
        self.brain = genome_to_net(self.genome)

        # Color lineage (random if no parent)
        self.color = color if color is not None else _random_color()

        # State
        self.energy = ENERGY_INIT
        self.age = 0
        self.alive = True
        self.fitness = 0.0
        self.wants_to_reproduce = False   # flag set during step()

    def perceive(self, food_grid: np.ndarray) -> np.ndarray:
        """Build input vector from local food window + optional energy/age."""
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
            extras.append(self.energy / ENERGY_MAX)
        if USE_AGE_INPUT:
            max_age = AGE_LIMIT if AGE_LIMIT else 500
            extras.append(min(self.age / max_age, 1.0))

        if extras:
            return np.concatenate([perception, extras])
        return perception

    def step(self, food_grid: np.ndarray):
        """
        One simulation step:
          1. Perceive → decide action
          2. Move or flag reproduction intent
          3. Eat food if present
          4. Lose energy (living cost)
          5. Check death
        """
        if not self.alive:
            return

        self.wants_to_reproduce = False

        # 1. Perceive + decide
        inputs = self.perceive(food_grid)
        action = self.brain.forward(inputs)

        # 2. Act
        if action == 4:
            # Reproduce intent — only valid if enough energy
            if self.energy >= REPRODUCE_ENERGY_THRESHOLD:
                self.wants_to_reproduce = True
                self.energy -= REPRODUCE_ENERGY_COST
        else:
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
        self.fitness += max(self.energy, 0)

        # 5. Death checks
        if self.energy <= ENERGY_DEATH_THRESHOLD:
            self.alive = False
        if AGE_LIMIT and self.age >= AGE_LIMIT:
            self.alive = False

    def reproduce(self) -> "Agent":
        """
        Create one child agent:
          - Cloned + mutated genome
          - Color slightly shifted from parent
          - Spawns near parent position
          - Starts with CHILD_ENERGY_START energy
        """
        child_genome = mutate(clone(self.genome))
        child_color = _mutate_color(self.color)

        # Spawn within 2 cells of parent (toroidal)
        offset_x = np.random.randint(-2, 3)
        offset_y = np.random.randint(-2, 3)
        child_x = (self.x + offset_x) % GRID_WIDTH
        child_y = (self.y + offset_y) % GRID_HEIGHT

        child = Agent(genome=child_genome, x=child_x, y=child_y, color=child_color)
        child.energy = CHILD_ENERGY_START
        return child