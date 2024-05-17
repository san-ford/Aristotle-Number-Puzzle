import time

# print solution
def printit():
    solutions[0] += 1
    print("Solution " + str(solutions[0]) + ":")
    print(f"{'        '}{pos[1] : ^8}{pos[2] : ^8}{pos[3] : ^8}")
    print()
    print()
    print(f"{'    '}{pos[12] : ^8}{pos[13] : ^8}{pos[14] : ^8}{pos[4] : ^8}")
    print()
    print(f"{pos[11] : ^8}{pos[18] : ^8}{pos[19] : ^8}{pos[15] : ^8}{pos[5] : ^8}")
    print()
    print(f"{'    '}{pos[10] : ^8}{pos[17] : ^8}{pos[16] : ^8}{pos[6] : ^8}")
    print()
    print(f"{'        '}{pos[9] : ^8}{pos[8] : ^8}{pos[7] : ^8}")


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
        else:
            printit()
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


"""
    index = position, value = block number
    the numbers of the positions are defined by the graph
"""
pos = [0]
solutions = [0]

start = time.time()
solve(0)
end = time.time()
print(solutions[0], "solutions found in", end-start, "seconds.")
