# Grid Navigation with a Reactive Agent

This project demonstrates the implementation of a reactive agent to solve a grid navigation problem. The agent moves towards the goal while avoiding obstacles in a 5x5 grid environment.

## Table of Contents
- Introduction
- Dependencies
- Setup
- Usage
- Project Structure
- Reactive Agent Algorithm
- Future Improvements
- Contributing
- License

## Introduction
A reactive agent is a simple form of agent that makes decisions based solely on the current environment state, without memory of past actions. This project uses a reactive agent to navigate a grid from a start position to a goal position, avoiding obstacles.

## Dependencies
This project requires the following Python libraries:
- numpy
- matplotlib

Install the dependencies using pip:

```
pip install numpy matplotlib
```

## Setup
1. Clone the repository:
   ```
   git clone https://github.com/shruthigudimalla/grid-navigation-reactive-agent.git
   cd grid-navigation-reactive-agent
   ```

2. Save the provided Python script as `gridNavigation.py` in the project directory.

## Usage
Run the Python script to execute the reactive agent in the grid environment:

```
python gridNavigation.py
```

The script will:
1. Set up a 5x5 grid environment with a start, goal, and obstacles.
2. Initialize a reactive agent at the start position.
3. Move the agent step-by-step towards the goal.
4. Print the agent's path from start to goal.
5. Visualize the grid and the agent's path.

## Project Structure
```
grid-navigation-reactive-agent/
│
├── gridNavigation.py      # Main script to initialize and run the reactive agent
└── README.txt             # Project README file
```

## Reactive Agent Algorithm
The reactive agent uses the following logic to move towards the goal:
- It checks if it can move downwards without hitting an obstacle.
- If not, it checks if it can move rightwards without hitting an obstacle.
- If not, it checks if it can move leftwards without hitting an obstacle.
- If not, it checks if it can move upwards without hitting an obstacle.

The agent repeats these steps until it reaches the goal.

## Future Improvements
- Experiment with different grid sizes and more complex obstacle layouts.
- Implement additional agent types (e.g., goal-based or learning agents) for comparison.
- Enhance visualization to show the agent's movement step-by-step.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
```
