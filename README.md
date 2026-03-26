# Neuroevolution : Ikkyu's Game of Life

Inspired by "Conway’s Game of Life", this project reimagines classical cellular automata through the lens of modern artificial intelligence. Instead of simple rule-based cells, agents in this environment are driven by neural networks and evolve over time using genetic algorithms. <br><br>
<img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif" width="100%" />

Apply knowledge from 01076582 Artificial Intelligence course at KMITL, particularly neural networks and evolutionary algorithms—this project explores how complex, lifelike behaviors can emerge from simple components. Agents perceive their surroundings, make decisions, compete for resources, and adapt across generations, transforming a static grid world into a dynamic, evolving ecosystem. <br><br>
<img width="100%" alt="สกรีนช็อต 2026-03-26 192012" src="https://github.com/user-attachments/assets/ef49f7bf-c992-4cbd-9f51-860fed80039c" />


---

## 🚀 Overview

The traditional Game of Life operates on fixed, deterministic rules to update cell states. In this project, those rules are replaced with learned behavior, where each cell functions as an autonomous agent.

Each agent:

- Observes its local environment (configurable perception range)
- Uses a neural network to decide its next action (single hidden layer with adjustable size)
- Evolves over time through genetic algorithms

This transforms the system from a rule-based simulation into an artificial life environment, where complex and adaptive behaviors emerge from simple interactions.

---

## 🧠 Key Concepts

This project applies knowledge from artificial intelligence coursework, including:

- **Cellular Automata** – A grid-based environment where global behavior emerges from local interactions
- **Neural Networks** – Each agent uses a lightweight neural model to map perceptions to actions
- **Genetic Algorithms** – Agent behaviors evolve over time through mutation and selection
- **Emergence** – Complex, system-level patterns arise from simple agent-environment interactions

---

## ⚙️ System Architecture

### Environment
- 2D grid-based world
- Each cell may contain food, an agent, or remain empty
- Food is dynamically generated, creating a structured and evolving resource landscape

### Cell Agent
Each cell is treated as an agent with:
- **Inputs**: Local perception of the surrounding grid (configurable radius), optionally including internal states such as energy and age
- **Brain**: A feedforward neural network (weights, biases, activation functions)
- **Output**: Action decisions (e.g., move, stay, or reproduce)

### Evolution Mechanism
- A population of agents evolves continuously over time (no discrete generations)
- Fitness is implicit, driven by survival and reproduction success
- Genetic operations:
  - Mutation Random perturbations to neural network parameters
  - Selection Agents that survive longer and reproduce more frequently pass on their traits

---

## ⚙️ Control Variables & Experiment Settings

This simulation is designed to be configurable, allowing experimentation with different environmental conditions, agent capabilities, and evolutionary strategies.

---

### 🌍 Environment Observability

- **Fully Observable**
  - Agents have access to the entire grid state
  - Enables global decision-making
  - Higher computational complexity

- **Partially Observable**
  - Agents perceive only a local region (e.g., radius-based sensing)
  - Encourages exploration and emergent behavior
  - More biologically realistic

---

### 👁️ Perception / Sensor Model

- **Local Radius Sensing**
  - Detects environment within a fixed radius
  - Can include food, other agents, or hazards

- **Directional Sensing**
  - Aggregated signals (e.g., food_up, food_down, etc.)
  - Lower dimensional input

- **Gradient-Based Sensing**
  - Uses directional differences (dx, dy)
  - More efficient representation

---

### 🧠 Neural Network Configuration

- **Hidden Layer Size**
  - Number of neurons in hidden layer (e.g., 8–20)

- **Network Depth**
  - Single-layer (recommended)
  - Multi-layer (experimental)

- **Activation Function**
  - tanh (default)
  - ReLU (optional)

---

### 🧬 Evolution Strategy

- **Reproduction Type**
  - Asexual (mutation only)
  - Sexual (crossover + mutation) *(optional)*

- **Mutation Scale**
  - Controls magnitude of weight changes

- **Mutation Probability**
  - Fraction of parameters mutated per generation

- **Selection Strategy**
  - Top-k selection (e.g., top 20%)
  - Tournament selection
  - Random survivor inclusion

---

### ⚡ Fitness & Survival

- **Energy System**
  - Gain energy from food
  - Lose energy per step

- **Reproduction Threshold**
  - Minimum energy required to reproduce

- **Reproduction Cost**
  - Energy deducted during reproduction

- **Aging**
  - Optional age tracking
  - Maximum lifespan or decay over time

---

### 🧠 Internal State Awareness

- **Include Energy as Input**
  - Agent can adapt behavior based on current energy

- **Include Age as Input**
  - Enables lifecycle-based decision-making

- **Disabled**
  - Purely reactive agent (environment-only)

---

### 🔄 Population Control

- **Population Size Limit**
  - Maximum number of agents in environment

- **Elitism**
  - Preserve top-performing agents across generations

- **Random Injection**
  - Introduce new random agents to maintain diversity

---

### 🎮 Action Space

- **Discrete Movement**
  - Up, Down, Left, Right

- **Continuous Movement** *(optional)*
  - Directional vector (dx, dy)

- **Reproduction Action**
  - Explicit (agent decides when to reproduce)
  - Implicit (triggered by proximity + energy)

---

### ⏱️ Simulation Parameters

- **Steps per Generation**
  - Number of simulation steps before evolution

- **Simulation Speed**
  - Controls visualization update rate

- **Grid Size**
  - Environment dimensions

---

## 🧪 Purpose

These control variables allow systematic experimentation with:

- Emergent behavior under different constraints  
- Impact of observability on intelligence  
- Trade-offs between exploration and exploitation  
- Evolution dynamics under varying selection pressure  

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
