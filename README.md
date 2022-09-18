# Game-of-life

This project consists of implementing Conway's Game of Life (1970) in Python. It is broken down into 4 steps. The first step was to generate a state of the game of life. The second step was to count the neighbours. The third step was to compute a step of the game. Finally, the implementation of a main loop was the fourth step.
Definition: The game of life is a cellular automaton running on a grid composed of cells that have a binary state: 1 for alive and 0 for dead. The neighbourhood of the cells makes them evolve in time. The grid is therefore modified at each stage of evolution.
How it works: to stay alive, a cell must have 2 or 3 living neighbours. If it is surrounded by more than 3 or less than 2 living neighbours, it dies. If a dead cell is surrounded by 3 living cells, then it comes to life at the next evolution. (Source: Game of Life - Parametric Cellular Automaton - Online Simulator (dcode.fr))
