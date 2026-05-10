# Graph Coloring using Backtracking and Branch & Bound

# Number of vertices
n = int(input("Enter number of vertices: "))

# Adjacency matrix
graph = []

print("Enter adjacency matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# Number of colors
m = int(input("Enter number of colors: "))

# Color array
colors = [0] * n


# Function to check if current color can be assigned
def isSafe(node, color):

    # Check adjacent vertices
    for k in range(n):
        if graph[node][k] == 1 and colors[k] == color:
            return False

    return True


# Backtracking function
def solve(node):

    # If all vertices are colored
    if node == n:
        return True

    # Try all colors
    for color in range(1, m + 1):

        # Branch and Bound pruning
        if isSafe(node, color):

            # Assign color
            colors[node] = color

            # Recur for next vertex
            if solve(node + 1):
                return True

            # Backtracking
            colors[node] = 0

    return False


# Main
if solve(0):

    print("\nSolution Found:")
    for i in range(n):
        print("Vertex", i, "--> Color", colors[i])

else:
    print("No solution exists")