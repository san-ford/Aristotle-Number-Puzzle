# Aristotle-Number-Puzzle

The Aristotle Number Puzzle is an octogonal grid with 19 cells, where each cell must contain a unique integer 1 - 19. To solve the puzzle, one must find an arrangement such that each row and each diagonal (both directions) sums to 38. The puzzle is arranged as such:

<img width="500" alt="Cell Path" src="https://github.com/san-ford/Aristotle-Number-Puzzle/blob/main/Cell_Path.png" />

The cell numbers in this diagram represent the path taken in my approach to solve the problem. Specifically, the numbers represent the node depth in a depth-first search. My approach is as follows:

## Initial Approach: Brute Force
This involves trying every combination until all rows and diagonals sum to 38. This approach runs in *O(n)*, which is very slow, since the number of possible combinations is 19 **!** ~ 1.2 x $10^{17}$.

## Depth-First Search
1. Set up a DFS algorithm to find all valid arrangements of numbers. Begin with every combination, then perform checks to limit the depth of branches.
2. Create the list of checks and implement them for their corresponding depths.
3. If all checks are passed at depth 19, record the solution (12 solutions due to symmetry).
4. Plot all solutions

Running the code produces the following graph:

<img width="1000" alt="Solutions" src="https://github.com/san-ford/Aristotle-Number-Puzzle/blob/main/Solutions.png" />

To optimize the run time and avoiding evaluating 19! configurations, as many checks as possible should be performed as early as possible. This is why I chose a path wrapping around the perimeter of the octogon, to implement a check at least every three node depths. The checks are as follows:

Checks:
1. sum of nodes(1,2,3) = 38 (depth = 3)
2. sum of nodes(3,4,5) = 38 (depth = 5)
3. sum of nodes(2,6) <= 35 (depth = 6) *
4. sum of nodes(5,6,7) = 38 (depth = 7)
5. sum of nodes(1,7) <= 32 (depth = 7) **
6. sum of nodes(4,8) <= 35 (depth = 8) *
7. sum of nodes(7,8,9) = 38 (depth = 9)
8. sum of nodes(3,9) <= 32 (depth = 9) **
9. sum of nodes(2,10) <= 35 (depth = 10) *
10. sum of nodes(6,10) <= 35 (depth = 10) *
11. sum of nodes(9,10,11) = 38 (depth = 11)
12. sum of nodes(5,11) <= 32 (depth = 11) **
13. sum of nodes(1,11,12) = 38 (depth = 12)
14. sum of nodes(4,12) <= 32 (depth = 12) **
15. sum of nodes(8,12) <= 32 (depth = 12) **
16. sum of nodes(4,12,13,14) = 38 (depth = 14)
17. sum of nodes(2,6,14,15) = 38 (depth = 15)
18. sum of nodes(4,8,15,16) = 38 (depth = 16)
19. sum of nodes(6,10,16,17) = 38 (depth = 17)
20. sum of nodes(8,12,17,18) = 38 (depth = 18)
21. sum of nodes(2,10,13,18) = 38 (depth = 18)
22. sum of nodes(5,11,15,18,19) = 38 (depth = 19)

*(other 2 in row can be 1 and 2 at minimum)

**(other 3 in row can be 1, 2, and 3 at minimum)

A timer was added to test the effectiveness of the checks on the runtime.
