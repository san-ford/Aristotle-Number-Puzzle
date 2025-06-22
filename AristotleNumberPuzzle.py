import time
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np


# plot solutions
def make_plots(sol):
    fig = plt.figure(figsize=(10, 10))
    for i, p in enumerate(sol):
        ax = plt.subplot(3, 4, i + 1)
        plt.axis('off')
        # coordinates with center block at origin
        coord = [[-1, 2], [0, 2], [1, 2], [-1.5, 1], [-0.5, 1], [0.5, 1], [1.5, 1],
                 [-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0], [-1.5, -1], [-0.5, -1],
                 [0.5, -1], [1.5, -1], [-1, -2], [0, -2], [1, -2]]
        labels = [[str(p[1])], [str(p[2])], [str(p[3])], [str(p[12])], [str(p[13])],
                  [str(p[14])], [str(p[4])], [str(p[11])], [str(p[18])], [str(p[19])],
                  [str(p[15])], [str(p[5])], [str(p[10])], [str(p[17])], [str(p[16])],
                  [str(p[6])], [str(p[9])], [str(p[8])], [str(p[7])]]

        # horizontal cartesian coords
        hcoord = [c[0] for c in coord]

        # vertical cartesian coords
        vcoord = [c[1] * np.cos(np.radians(30)) for c in coord]

        ax.set_aspect('equal')

        # add colored hexagons
        for x, y, l in zip(hcoord, vcoord, labels):
            hex = RegularPolygon((x, y), numVertices=6, radius=0.575,
                                 orientation=np.radians(60),
                                 facecolor='goldenrod', edgecolor='black')
            ax.add_patch(hex)
            # add text labels
            ax.text(x, y, l[0], ha='center', va='center',
                    color='saddlebrown', size=15)

        # Also add scatter points in hexagon centres
        ax.scatter(hcoord, vcoord, color='goldenrod')
        plt.title('Solution {}'.format(i + 1))
        plt.axis('off')
    plt.show()


# performs validity checks for a specified depth
def checks(d):
    if d == 3:
        if pos[1] + pos[2] + pos[3] != 38:
            return False
    elif d == 5:
        if pos[3] + pos[4] + pos[5] != 38:
            return False
    elif d == 6:
        if pos[2] + pos[6] > 35:
            return False
    elif d == 7:
        if pos[5] + pos[6] + pos[7] != 38:
            return False
        if pos[1] + pos[7] > 32:
            return False
    elif d == 8:
        if pos[4] + pos[8] > 35:
            return False
    elif d == 9:
        if pos[7] + pos[8] + pos[9] != 38:
            return False
        if pos[3] + pos[9] > 32:
            return False
    elif d == 10:
        if pos[2] + pos[10] > 35:
            return False
        if pos[6] + pos[10] > 35:
            return False
    elif d == 11:
        if pos[9] + pos[10] + pos[11] != 38:
            return False
        if pos[5] + pos[11] > 32:
            return False
    elif d == 12:
        if pos[1] + pos[11] + pos[12] != 38:
            return False
        if pos[4] + pos[12] > 32:
            return False
        if pos[8] + pos[12] > 32:
            return False
    elif d == 14:
        if pos[4] + pos[12] + pos[13] + pos[14] != 38:
            return False
    elif d == 15:
        if pos[2] + pos[6] + pos[14] + pos[15] != 38:
            return False
    elif d == 16:
        if pos[4] + pos[8] + pos[15] + pos[16] != 38:
            return False
    elif d == 17:
        if pos[6] + pos[10] + pos[16] + pos[17] != 38:
            return False
    elif d == 18:
        if pos[8] + pos[12] + pos[17] + pos[18] != 38:
            return False
        if pos[2] + pos[10] + pos[13] + pos[18] != 38:
            return False
    elif d == 19:
        if pos[5] + pos[11] + pos[15] + pos[18] + pos[19] != 38:
            return False
        # solution found
        else:
            # add solution to list
            solutions.append(pos.copy())
    return True


# recursive function performs DFS
def solve(depth):
    depth += 1
    # run through each block number for this node
    for i in range(1, 20):
        # if the number is not yet used, add to stack
        if i not in pos:
            pos.append(i)
            # if the number passes the check for its depth, move on to next node
            if checks(depth):
                solve(depth)
            # if the number fails the check, remove it and move on to next number
            else:
                pos.pop()
    # all combinations exhausted for previous number
    # remove it and return to previous node (depth - 1)
    pos.pop()


# keep list of positions and block numbers
# index = position, value = block number
pos = [0]
solutions = []

# keep track off runtime
start = time.time()
# perform DFS and retrieve solutions
solve(0)
# plot solutions
make_plots(solutions)
# display runtime
end = time.time()
print("12 solutions found in", end-start, "seconds.")
