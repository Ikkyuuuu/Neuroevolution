# config.py — All hyperparameters in one place

GRID_WIDTH = 100
GRID_HEIGHT = 100

POPULATION_SIZE = 80          # starting population
MIN_POPULATION = 20           # floor: spawn random agents if below this
MAX_POPULATION = 200          # ceiling: no reproduction allowed above this
GENERATION_STEPS = 100000       # total steps to run (no more per-gen resets)
NUM_GENERATIONS = 1           # kept for main loop compatibility (1 long run)

# Neural network shape
PERCEPTION_RADIUS = 3         # 1 = 3x3 window around agent
USE_ENERGY_INPUT = True
USE_AGE_INPUT = True
HIDDEN_SIZE = 20

# Compute input size automatically
_window = (2 * PERCEPTION_RADIUS + 1) ** 2
INPUT_SIZE = _window + (1 if USE_ENERGY_INPUT else 0) + (1 if USE_AGE_INPUT else 0)
OUTPUT_SIZE = 5               # up, down, left, right, reproduce

# Energy
ENERGY_INIT = 50.0
ENERGY_MAX = 150.0
ENERGY_PER_STEP = -0.5        # cost of living
ENERGY_FROM_FOOD = 20.0
ENERGY_DEATH_THRESHOLD = 0.0

# Reproduction
REPRODUCE_ENERGY_THRESHOLD = 80.0   # must have this much energy to reproduce
REPRODUCE_ENERGY_COST = 40.0        # energy lost by parent on reproduction
CHILD_ENERGY_START = 30.0           # child starts with this energy

# Food
FOOD_DENSITY = 0.07
FOOD_RESPAWN_RATE = 0.0005

# Genetic algorithm (mutation only — no crossover)
MUTATION_RATE = 0.4
MUTATION_STRENGTH = 0.3

# Color lineage
COLOR_MUTATION_STRENGTH = 15  # max RGB channel shift per child (0–255 scale)

# Age limit (set to None to disable)
AGE_LIMIT = None

# Visualization
VIZ_INTERVAL = 1              # render every N steps
ANIMATION_SPEED_MS = 50
