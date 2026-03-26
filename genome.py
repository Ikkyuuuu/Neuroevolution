# genome.py — Genome encoding, mutation, and cloning

import numpy as np
from config import MUTATION_RATE, MUTATION_STRENGTH
from neural_net import NeuralNet


def random_genome() -> np.ndarray:
    """Create a random genome (random NN weights)."""
    net = NeuralNet()
    return net.to_genome()


def clone(genome: np.ndarray) -> np.ndarray:
    """Return a deep copy of a genome."""
    return genome.copy()


def mutate(genome: np.ndarray) -> np.ndarray:
    """
    Apply mutation: randomly perturb a fraction of genes
    with Gaussian noise.
    """
    mutated = genome.copy()
    mask = np.random.rand(len(genome)) < MUTATION_RATE
    noise = np.random.randn(np.sum(mask)) * MUTATION_STRENGTH
    mutated[mask] += noise
    return mutated


def genome_to_net(genome: np.ndarray) -> NeuralNet:
    """Instantiate a NeuralNet and load the genome into it."""
    net = NeuralNet()
    net.from_genome(genome)
    return net