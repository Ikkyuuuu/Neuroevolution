# Neuroevolution: Ikkyu’s Game of Life

Inspired by **Conway’s Game of Life**, this project reimagines classical cellular automata using modern artificial intelligence. Instead of fixed rules, agents are controlled by neural networks and evolve over time through genetic algorithms.

<br>
<img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif" width="100%" />
<br>

Using concepts from artificial intelligence—particularly neural networks and evolutionary algorithms—this project explores how complex, lifelike behaviors can emerge from simple components.

<br>
<img width="100%" src="https://github.com/user-attachments/assets/ef49f7bf-c992-4cbd-9f51-860fed80039c" />

---

## 🚀 Overview

The traditional Game of Life operates on deterministic rules.  
Here, those rules are replaced with **learned behavior**, where each cell acts as an autonomous agent.

Each agent:
- Observes its local environment
- Uses a neural network to decide actions
- Evolves over time through mutation and selection

This creates an **artificial life system** where behavior emerges rather than being predefined.

---

## 🧠 Key Concepts

- **Cellular Automata** – Local interactions drive global behavior  
- **Neural Networks** – Map perception to action  
- **Genetic Algorithms** – Evolve behavior over time  
- **Emergence** – Complex patterns arise from simple rules  

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

---

## 🧠 Neural Network

- Hidden layer: 10 neurons  
- Activation: `tanh`  

---

## 🧬 Evolution

- Asexual reproduction (mutation only)  
- Mutation controls behavioral variation  
- Selection emerges naturally via survival  

---

## ⚡ Dynamics

- Agents gain energy from food  
- Lose energy over time  
- Reproduce when energy threshold is reached  
- Die when energy is depleted  

---

## 🎮 Agent Actions

- Move: Up, Down, Left, Right  
- Reproduce  

---

## 💡 Motivation

> Intelligence can emerge from simple agents interacting locally, without explicit global rules.

This project connects:
- Artificial Life (ALife)  
- Machine Learning  
- Complex Systems  

---

## 📌 Summary
This project reimagines the Game of Life as a neuroevolutionary system, where agents learn, adapt, and evolve over time—demonstrating how complex behavior can emerge from simple local interactions.
