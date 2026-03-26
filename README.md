# Neuroevolution: Ikkyu’s Game of Life

Inspired by **Conway’s Game of Life**, this project reimagines classical cellular automata using modern artificial intelligence. Instead of fixed rules, agents are controlled by neural networks and evolve over time through genetic algorithms.

<br>
<img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif" width="100%" />
<br>

Using concepts from artificial intelligence—particularly neural networks and evolutionary algorithms—this project explores how complex, lifelike behaviors can emerge from simple components.

<br>
<img width="100%" src="https://github.com/user-attachments/assets/ef49f7bf-c992-4cbd-9f51-860fed80039c" />
<br><br>

---

## 🚀 Overview

The traditional Game of Life operates on deterministic rules.  
Here, those rules are replaced with **learned behavior**, where each cell acts as an autonomous agent.

Each agent:
- Observes its local environment
- Uses a neural network to decide actions
- Evolves over time through mutation and selection

This creates an **artificial life system** where behavior emerges rather than being predefined.<br><br>

---

## 🧠 Key Concepts

- **Cellular Automata** – Local interactions drive global behavior  
- **Neural Networks** – Map perception to action  
- **Genetic Algorithms** – Evolve behavior over time  
- **Emergence** – Complex patterns arise from simple rules  
<br><br>

---

## ⚙️ System Architecture

### Environment
- 2D grid world  
- Cells may contain food, agents, or be empty  
- Food is dynamically generated  

### Agent
- **Inputs**: Local grid perception (+ optional energy/age)  
- **Brain**: Feedforward neural network  
- **Outputs**: Actions (move, stay, reproduce)  

### Evolution
- Continuous (no fixed generations)  
- Survival and reproduction define success  
- Mutation drives diversity  
<br><br>

---

## 🧠 Neural Network

- Hidden layer: 10 neurons  
- Activation: `tanh`  
<br><br>

---

## 🧬 Evolution

- Asexual reproduction (mutation only)  
- Mutation controls behavioral variation  
- Selection emerges naturally via survival  
<br><br>

---

## ⚡ Dynamics

- Agents gain energy from food  
- Lose energy over time  
- Reproduce when energy threshold is reached  
- Die when energy is depleted  
<br><br>

---

## 🎮 Agent Actions

- Move: Up, Down, Left, Right  
- Reproduce  
<br><br>

---

## 💡 Motivation

> Intelligence can emerge from simple agents interacting locally, without explicit global rules.

This project connects:
- Artificial Life (ALife)  
- Machine Learning  
- Complex Systems  
<br><br>

---

## 📌 Summary
This project reimagines the Game of Life as a neuroevolutionary system, where agents learn, adapt, and evolve over time—demonstrating how complex behavior can emerge from simple local interactions.
<br><br>

---

## ⚙️ Installation

### 1. Clone the repository
```
git clone https://github.com/Ikkyuuuu/Neuroevolution.git
cd Neuroevolution
```
### 2. Install dependencies
```
pip install numpy matplotlib
```
### 3. Run the simulation
```
python main.py
```
<br><br>

---

## ⚙️ Environment Parameters Configuration

All simulation parameters are defined in `config.py`, allowing easy experimentation with agent behavior, evolution, and environment dynamics.

---

### 🌍 Environment
- `GRID_WIDTH`, `GRID_HEIGHT` — Size of the grid world  
- `FOOD_DENSITY` — Initial food distribution  
- `FOOD_RESPAWN_RATE` — Probability of food appearing per step  

---

### 👥 Population
- `POPULATION_SIZE` — Initial number of agents  
- `MIN_POPULATION` — Minimum population (auto refill)  
- `MAX_POPULATION` — Maximum population cap  
- `GENERATION_STEPS` — Total simulation steps  

---

### 🧠 Neural Network
- `PERCEPTION_RADIUS` — Size of local observation window  
- `HIDDEN_SIZE` — Number of neurons in hidden layer  
- `USE_ENERGY_INPUT`, `USE_AGE_INPUT` — Include internal state as input  
- `OUTPUT_SIZE` — Action space (movement + reproduction)  

---

### ⚡ Energy System
- `ENERGY_INIT` — Starting energy  
- `ENERGY_MAX` — Maximum energy limit  
- `ENERGY_PER_STEP` — Energy decay per step  
- `ENERGY_FROM_FOOD` — Energy gained from food  
- `ENERGY_DEATH_THRESHOLD` — Death condition  

---

### 🧬 Reproduction
- `REPRODUCE_ENERGY_THRESHOLD` — Minimum energy to reproduce  
- `REPRODUCE_ENERGY_COST` — Energy cost of reproduction  
- `CHILD_ENERGY_START` — Initial energy of offspring  

---

### 🧪 Evolution (Mutation)
- `MUTATION_RATE` — Probability of mutation  
- `MUTATION_STRENGTH` — Magnitude of weight changes  

---

### 🎨 Visualization
- `VIZ_INTERVAL` — Rendering frequency  
- `ANIMATION_SPEED_MS` — Visualization speed  

---

These parameters control the balance between **exploration, survival, and evolution**, and can be tuned to observe different emergent behaviors.
