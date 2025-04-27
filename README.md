# Tic-Tac-Toe AI Implementations

Code for Tic-tac-toe game using Random choice, Minimax and Alpha Beta Pruning algorithms.

## Implementations

### 1. prog.py (Standard Minimax)
This implementation uses the classic Minimax algorithm without any pruning. The AI evaluates all possible game states recursively to determine the optimal move.

### 2. pruning.py (Alpha-Beta Pruning)
This version implements the Alpha-Beta Pruning optimization for Minimax, which reduces the number of nodes evaluated by eliminating branches that won't affect the final decision.

## Performance Comparison: Minimax vs Alpha-Beta Pruning

The key difference in performance between standard Minimax and Alpha-Beta Pruning is efficiency:

### Computational Efficiency
Alpha-Beta Pruning significantly reduces the number of nodes evaluated during calculation, particularly in complex game trees.

### Decision Quality
Both algorithms make optimal decisions for a perfect information game like tic-tac-toe, but Alpha-Beta reaches the same decision more efficiently and quickly.

### Practical Impact
For tic-tac-toe, the difference is less noticeable due to the relatively small game tree, but would be more significant in more complex games like chess.

## Performance Metrics

### Standard Minimax without pruning:
- It would evaluate approximately 20,000 to 30,000 nodes for the first move

### Alpha-Beta Pruning:
- With optimal move ordering, this could drop to around 3,000 to 5,000 nodes for the first move
- This represents an 80-85% reduction in nodes evaluated
