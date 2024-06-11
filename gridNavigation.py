import numpy as np
import matplotlib.pyplot as plt

# Create a 5x5 grid
grid = np.zeros((5, 5))

# Define the start, goal, and obstacles
start = (0, 0)
goal = (4, 4)
obstacles = [(1, 1), (1, 2), (2, 1), (3, 3)]

# Set obstacles in the grid
for obs in obstacles:
    grid[obs] = -1

# Set start and goal in the grid
grid[start] = 1
grid[goal] = 2

print("Grid Environment:")
print(grid)

class ReactiveAgent:
    def __init__(self, start, goal, grid):
        self.position = start
        self.goal = goal
        self.grid = grid
        self.path = [start]

    def move(self):
        x, y = self.position
        goal_x, goal_y = self.goal
        
        if x < goal_x and self.grid[x + 1, y] != -1:
            x += 1
        elif y < goal_y and self.grid[x, y + 1] != -1:
            y += 1
        elif y > goal_y and self.grid[x, y - 1] != -1:
            y -= 1
        elif x > goal_x and self.grid[x - 1, y] != -1:
            x -= 1

        self.position = (x, y)
        self.path.append(self.position)

    def is_at_goal(self):
        return self.position == self.goal

agent = ReactiveAgent(start, goal, grid)

# Move the agent until it reaches the goal
while not agent.is_at_goal():
    agent.move()

print("Agent's Path:")
print(agent.path)

def plot_grid(grid, path):
    plt.imshow(grid, cmap='gray_r')
    plt.grid(True)
    for (x, y) in path:
        plt.plot(y, x, 'bo-')  # Plot path as blue dots connected by lines
    plt.plot(start[1], start[0], 'go')  # Start in green
    plt.plot(goal[1], goal[0], 'ro')  # Goal in red
    plt.show()

plot_grid(grid, agent.path)
