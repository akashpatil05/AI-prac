# Simple A* Algorithm for 8 Puzzle Problem

goal = [1,2,3,8,-1,4,7,6,5]

# Print Board
def print_board(state):

    for i in range(9):

        if i % 3 == 0:
            print()

        if state[i] == -1:
            print("_", end=" ")
        else:
            print(state[i], end=" ")

    print()


# Heuristic Function
def heuristic(state):

    count = 0

    for i in range(9):

        if state[i] != goal[i] and state[i] != -1:
            count += 1

    return count


# Move Function
def move(state, p1, p2):

    temp = state[:]

    temp[p1], temp[p2] = temp[p2], temp[p1]

    return temp


# A* Function
def astar(start):

    current = start
    visited = []
    steps = 0

    print("\nInitial State:")
    print_board(current)

    while current != goal:

        visited.append(current)

        blank = current.index(-1)

        possible = []

        # Left
        if blank % 3 != 0:
            possible.append(move(current, blank, blank-1))

        # Right
        if blank % 3 != 2:
            possible.append(move(current, blank, blank+1))

        # Up
        if blank >= 3:
            possible.append(move(current, blank, blank-3))

        # Down
        if blank <= 5:
            possible.append(move(current, blank, blank+3))

        best = None
        min_f = 999

        for p in possible:

            if p not in visited:

                g = steps + 1
                h = heuristic(p)

                f = g + h

                if f < min_f:

                    min_f = f
                    best = p

        current = best
        steps += 1

        print("\nStep", steps)
        print_board(current)

    print("Goal State Reached")
    print("Solved in", steps, "moves")


# Main Program

start = []

print("Enter start state (-1 for blank):")

for i in range(9):
    start.append(int(input()))

astar(start)