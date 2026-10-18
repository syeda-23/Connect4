# Comparing the minimax algorithm and MCTS in the context of Connect 4
## What this is
A Connect 4 terminal-based game in Python primarily developed to investigate and compare effectiveness of MCTS and the minimax algorithm. Thus, the program allows users to simulate competing AI agents: minimax with alpha-beta pruning, and Monte Carlo Tree Search with UCB1. However users can also play against each other, or an AI opponent.

## How to run
python terminalui.py

**MENU**
1. Multiplayer (Human v Human)
2. Play against computer opponent(non intelligent)
3. Play against minimax
4. Play against MCTS
5. Observe MCTS vs Minimax
6. Stats mode
    
## Design process and file breakdown
- terminalui.py - gathering user inputs from the terminal 
- game.py - board representation, move generation, win detection
- minimax.py - minimax  and alpha-beta pruning
- mcts.py - MCTS with UCB1
- Node.py - Node class to build the object-oriented game tree for MCTS
- evaluation.py - automated head-to-head simulation harness

## Results
I first tested the effects of varying depth and alpha-pruning within the minimax component, and varying the number of rollouts and altering the UCB1 calculation within MCTS. The effects of varying these parameters can be examined through looking at win rates of simulated games, speed of execution and in some cases, number of nodes explored within the game tree. After testing each algorithm separately, I compared both algorithms to each other. 

### Minimax
#### Effect of depth on nodes explored
<img width="603" height="463" alt="image" src="https://github.com/user-attachments/assets/de6f6b6a-83a6-4c6a-b5d1-72d67f5b12fa" />

#### Effect of depth on win rate
<img width="626" height="472" alt="image" src="https://github.com/user-attachments/assets/d80d1dfc-3531-4bea-ad61-f8875b4d4858" />

#### Effect of depth on time taken to make a move
<img width="634" height="484" alt="image" src="https://github.com/user-attachments/assets/a9152560-065e-4b93-a852-17f6b0185b72" />


### MCTS

### Minimax vs MCTS

### Notes on methodology

## Future changes
Investigate the effect of different evaluation functions on win rate (minimax)
Investigate the effect of varying the exploration factor within the UCB1 calculation on win rate (MCTS)

## References
* https://file.scirp.org/Html/1-9601415_90972.htm#t1
* https://int8.io/monte-carlo-tree-search-beginners-guide/
* https://youtu.be/BEFY7IHs0HM?si=zWrrw39ImbldtLXl
* https://medium.com/@quasimik/implementing-monte-carlo-tree-search-in-node-js-5f07595104df
* https://medium.com/@quasimik/monte-carlo-tree-search-applied-to-letterpress-34f41c86e238
* https://en.wikipedia.org/wiki/Monte_Carlo_tree_search
* https://www.researchgate.net/publication/331552609_Research_on_Different_Heuristics_for_Minimax_Algorithm_Insight_from_Connect-4_Game
* https://www.researchgate.net/publication/412699289_Tactical_Precision_versus_Statistical_Exploration_An_Empirical_Study_of_Minimax_and_Monte_Carlo_Tree_Search_in_Connect_Four
