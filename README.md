# Neuroevolution : Game of Life

Inspired by Conway’s Game of Life, this project extends the classical cellular automata model by integrating concepts from 01076582 ARTIFICIAL INTELLIGENCE Course at KMITL, including neural networks and genetic algorithms.

---

## 🚀 Overview

The traditional Game of Life uses fixed, deterministic rules to evolve cell states. In this project, those rules are replaced with **learned behavior**, where each cell acts as an autonomous agent.

Each cell:
- Observes its local environment
- Uses a neural network to decide its next state
- Evolves over time through genetic algorithms

This transforms the system from rule-based simulation into an **artificial life environment with emergent behavior**.

---

## 🧠 Key Concepts

This project applies knowledge from artificial intelligence coursework, including:

- **Cellular Automata** – Grid-based simulation with local interactions  
- **Neural Networks** – Each cell uses a small neural model for decision-making  
- **Genetic Algorithms** – Evolution of cell behavior through mutation and selection  
- **Emergence** – Complex global patterns arising from simple local rules  

---

## ⚙️ System Architecture

### Environment
- 2D grid-based world
- Each position contains a cell (alive or dead)

### Cell Agent
Each cell is treated as an agent with:
- **Inputs**: Neighboring cell states  
- **Brain**: Neural network (weights + bias + activation)  
- **Output**: Decision to live, die, or change state  

### Evolution Mechanism
- Population of cells evolves over generations
- Fitness based on survival, stability, or pattern formation
- Genetic operations:
  - Mutation (random weight changes)
  - Selection (retain high-performing cells)

---

## 🔁 Simulation Loop

1. Initialize grid with random cells and neural weights  
2. For each timestep:
   - Cells observe neighbors  
   - Neural network determines next state  
3. Evaluate fitness  
4. Select top-performing cells  
5. Reproduce with mutation  
6. Repeat  

---

## 📊 Features

- Replaces fixed rules with adaptive neural behavior  
- Demonstrates emergent patterns beyond Conway’s rules  
- Visual simulation of evolving cellular systems  
- Modular design for experimenting with different AI methods  

---

## 🧪 Future Improvements

- Add multi-layer neural networks  
- Introduce stochastic environments  
- Compare rule-based vs learned behavior  
- Add visualization of fitness over generations  
- Extend to continuous space instead of grid  

---

## 💡 Motivation

This project explores the idea that:

> Intelligent behavior can emerge from simple agents interacting locally, without explicit global rules.

By combining cellular automata with learning and evolution, this system serves as a bridge between:
- Artificial Life (A-Life)
- Machine Learning
- Complex Systems

---

## 📌 Summary

Ikkyu reimagines Conway’s Game of Life by replacing deterministic rules with adaptive, evolving agents. It demonstrates how intelligence and structure can emerge through local interactions, learning, and evolution.

---
