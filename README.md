# COMP390 Risk AI

A simplified two-player Risk simulation developed for the University of Liverpool COMP390 Individual Project.

## Project aim

The project investigates AI decision-making in a stochastic turn-based strategy environment. The submitted dissertation proposal compares three required approaches:

- manually designed heuristic agent
- Monte Carlo Tree Search (MCTS)
- genetic-algorithm-optimised heuristic policy

A reinforcement-learning extension is optional if the core project is completed.

## Current development stage

The project is currently in game-engine development. The implemented foundation includes:

- territory representation
- territory ownership and army state
- adjacency using neighbouring territories
- map storage and lookup
- two-way map connections
- owned-territory queries
- enemy-neighbour queries

## Planned development order

1. Complete the core game engine.
2. Add unit tests.
3. Add a random baseline agent.
4. Implement the manual heuristic agent.
5. Implement MCTS.
6. Implement genetic-algorithm policy optimisation.
7. Run automated AI-vs-AI experiments.
8. Analyse results and computational cost.

## Running the project

Python 3 is required.

```bash
python3 main.py
```

## Repository structure

```text
COMP_390_RiskAI/
├── territory.py
├── risk_map.py
├── main.py
├── README.md
└── .gitignore
```

The structure will expand as player, combat, game-controller, AI and testing modules are added.
