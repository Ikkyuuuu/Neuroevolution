# neural_net.py — Lightweight 2-layer neural network (NumPy only)

import numpy as np
from config import INPUT_SIZE, HIDDEN_SIZE, OUTPUT_SIZE


class NeuralNet:
    """
    Simple feedforward network:
        input (INPUT_SIZE) -> hidden (HIDDEN_SIZE, tanh) -> output (OUTPUT_SIZE, linear)
    Weights are stored flat in the genome and loaded via from_genome().
    """

    def __init__(self):
        # Dimensions
        self.w1_shape = (HIDDEN_SIZE, INPUT_SIZE)
        self.b1_shape = (HIDDEN_SIZE,)
        self.w2_shape = (OUTPUT_SIZE, HIDDEN_SIZE)
        self.b2_shape = (OUTPUT_SIZE,)

        # Genome size (total number of parameters)
        self.genome_size = (
            HIDDEN_SIZE * INPUT_SIZE +
            HIDDEN_SIZE +
            OUTPUT_SIZE * HIDDEN_SIZE +
            OUTPUT_SIZE
        )

        # Initialize with random weights
        self.W1 = np.random.randn(*self.w1_shape) * 0.5
        self.b1 = np.zeros(self.b1_shape)
        self.W2 = np.random.randn(*self.w2_shape) * 0.5
        self.b2 = np.zeros(self.b2_shape)

    def forward(self, x: np.ndarray) -> int:
        """
        Forward pass. Returns argmax action index (0=up,1=down,2=left,3=right).
        x: 1D input vector of length INPUT_SIZE
        """
        h = np.tanh(self.W1 @ x + self.b1)
        out = self.W2 @ h + self.b2
        return int(np.argmax(out))

    def to_genome(self) -> np.ndarray:
        """Flatten all weights into a 1D genome array."""
        return np.concatenate([
            self.W1.flatten(),
            self.b1.flatten(),
            self.W2.flatten(),
            self.b2.flatten()
        ])

    def from_genome(self, genome: np.ndarray):
        """Load weights from a 1D genome array."""
        idx = 0

        size = HIDDEN_SIZE * INPUT_SIZE
        self.W1 = genome[idx:idx + size].reshape(self.w1_shape)
        idx += size

        size = HIDDEN_SIZE
        self.b1 = genome[idx:idx + size]
        idx += size

        size = OUTPUT_SIZE * HIDDEN_SIZE
        self.W2 = genome[idx:idx + size].reshape(self.w2_shape)
        idx += size

        size = OUTPUT_SIZE
        self.b2 = genome[idx:idx + size]