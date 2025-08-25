import random

GRID_SIZE = 5
START = (0, 0)  
GOAL = (4, 4)   

def random_position(exclude_positions=None):
    """Generate a random position on the grid, excluding certain positions."""
    exclude_positions = exclude_positions or []
    while True:
        pos = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        if pos not in exclude_positions:
            return pos

class ReflexAgent:
    def __init__(self, start, goal, obstacles):
        self.position = start  
        self.goal = goal      
        self.obstacles = obstacles  
        self.actions = ['up', 'down', 'left', 'right']  

    def is_valid_move(self, position):
        """Check if the move is within the grid and not hitting an obstacle."""
        return 0 <= position[0] < GRID_SIZE and 0 <= position[1] < GRID_SIZE and position not in self.obstacles

    def get_possible_moves(self):
        """Return a list of valid moves the agent can make from its current position."""
        moves = []
        x, y = self.position
        if self.is_valid_move((x - 1, y)): moves.append('up')
        if self.is_valid_move((x + 1, y)): moves.append('down')
        if self.is_valid_move((x, y - 1)): moves.append('left')
        if self.is_valid_move((x, y + 1)): moves.append('right')
        return moves

    def move(self):
        """Move the agent towards the goal."""
        possible_moves = self.get_possible_moves()
        if not possible_moves:
            print("No valid moves left. Agent is stuck!")
            return

        best_move = None
        min_distance = float('inf')

        for move in possible_moves:
            if move == 'up':
                new_position = (self.position[0] - 1, self.position[1])
            elif move == 'down':
                new_position = (self.position[0] + 1, self.position[1])
            elif move == 'left':
                new_position = (self.position[0], self.position[1] - 1)
            elif move == 'right':
                new_position = (self.position[0], self.position[1] + 1)

            distance = abs(new_position[0] - self.goal[0]) + abs(new_position[1] - self.goal[1])
            if distance < min_distance:
                min_distance = distance
                best_move = move

        if best_move == 'up':
            self.position = (self.position[0] - 1, self.position[1])
        elif best_move == 'down':
            self.position = (self.position[0] + 1, self.position[1])
        elif best_move == 'left':
            self.position = (self.position[0], self.position[1] - 1)
        elif best_move == 'right':
            self.position = (self.position[0], self.position[1] + 1)

    def reached_goal(self):
        """Check if the agent has reached the goal."""
        return self.position == self.goal

    def print_grid(self):
        """Print the grid with agent's position, obstacles, and goal."""
        for i in range(GRID_SIZE):
            row = ""
            for j in range(GRID_SIZE):
                if (i, j) == self.position:
                    row += "A "  
                elif (i, j) == self.goal:
                    row += "G "  
                elif (i, j) in self.obstacles:
                    row += "X "  
                else:
                    row += ". "  
            print(row)
        print()

    def run(self):
        """Run the agent until it reaches the goal or gets stuck."""
        steps = 0
        while not self.reached_goal():
            print(f"Step {steps}: Agent at {self.position}")
            self.print_grid()  
            self.move()
            steps += 1
            if steps > 20:  
                print("Max steps reached. Agent couldn't reach the goal.")
                break
        if self.reached_goal():
            print(f"Goal reached in {steps} steps!")
            self.print_grid()  

def main():
    obstacles = [random_position(exclude_positions=[START, GOAL]) for _ in range(3)]
    while len(set(obstacles)) != len(obstacles):
        obstacles = [random_position(exclude_positions=[START, GOAL] + obstacles) for _ in range(3)]
    print(f"Start: {START}, Goal: {GOAL}, Obstacles: {obstacles}")
    agent = ReflexAgent(START, GOAL, obstacles)
    agent.run()

if __name__ == "__main__":
    main()
