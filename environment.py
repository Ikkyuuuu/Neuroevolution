# environment.py — 2D grid world managing food

import numpy as np
from config import GRID_WIDTH, GRID_HEIGHT, FOOD_DENSITY, FOOD_RESPAWN_RATE


class Environment:
    def __init__(self):
        self.food_grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=np.float32)
        self._seed_food()

    def _seed_food(self):
        """Place initial food randomly across the grid."""
        mask = np.random.rand(GRID_HEIGHT, GRID_WIDTH) < FOOD_DENSITY
        self.food_grid[mask] = 1.0

    def respawn_food(self):
        """Each step, randomly respawn food on empty cells."""
        empty = self.food_grid == 0
        spawn_mask = (np.random.rand(GRID_HEIGHT, GRID_WIDTH) < FOOD_RESPAWN_RATE) & empty
        self.food_grid[spawn_mask] = 1.0

    def reset(self):
        """Full reset between generations."""
        self.food_grid[:] = 0.0
        self._seed_food()

    def get_food_count(self) -> int:
        return int(np.sum(self.food_grid))