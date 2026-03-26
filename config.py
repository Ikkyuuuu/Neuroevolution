# config.py — All hyperparameters in one place

GRID_WIDTH = 60
GRID_HEIGHT = 60

POPULATION_SIZE = 10
GENERATION_STEPS = 200       # steps per generation
NUM_GENERATIONS = 200        # total generations to run

# Neural network shape
PERCEPTION_RADIUS = 2        # 1 = 3x3 window around agent, 2 = 5x5 window around agent
USE_ENERGY_INPUT = True
USE_AGE_INPUT = True
HIDDEN_SIZE = 10

# Compute input size automatically
_window = (2 * PERCEPTION_RADIUS + 1) ** 2
INPUT_SIZE = _window + (1 if USE_ENERGY_INPUT else 0) + (1 if USE_AGE_INPUT else 0)
OUTPUT_SIZE = 4              # up, down, left, right

# Energy
ENERGY_INIT = 50.0
ENERGY_MAX = 150.0
ENERGY_PER_STEP = -0.5       # cost of living
ENERGY_FROM_FOOD = 20.0
ENERGY_DEATH_THRESHOLD = 0.0

# Food
FOOD_DENSITY = 0.15          # fraction of grid cells with food at start
FOOD_RESPAWN_RATE = 0.005    # probability per empty cell per step

# Genetic algorithm
MUTATION_RATE = 0.1          # fraction of genome weights mutated
MUTATION_STRENGTH = 0.3      # std of Gaussian noise added
ELITE_FRACTION = 0.2         # top fraction kept each generation
RANDOM_SURVIVOR_FRACTION = 0.05  # random extras to keep diversity

# Age limit (set to None to disable)
AGE_LIMIT = None

# Visualization
VIZ_INTERVAL = 1             # render every N generations
ANIMATION_SPEED_MS = 50      # milliseconds per frame