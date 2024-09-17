
TABLE_SIZE = 5
DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]

class ToyRobot:
    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None
        self.obstacles = []

    def place(self, x, y, facing, obstacles=None):
        if 0 <= x < TABLE_SIZE and 0 <= y < TABLE_SIZE and facing in DIRECTIONS:
            if obstacles is None:
                obstacles = []
            # Only place the robot if the position is not an obstacle
            if (x, y) not in obstacles:
                self.x = x
                self.y = y
                self.facing = facing
                self.obstacles = obstacles  # Store the obstacles for future checks

    def move(self):
        new_x, new_y = self.x, self.y
        if self.facing == "NORTH" and self.y < TABLE_SIZE - 1:
            new_y += 1
        elif self.facing == "EAST" and self.x < TABLE_SIZE - 1:
            new_x += 1
        elif self.facing == "SOUTH" and self.y > 0:
            new_y -= 1
        elif self.facing == "WEST" and self.x > 0:
            new_x -= 1

        # Only move if the new position is not an obstacle
        if (new_x, new_y) not in self.obstacles:
            self.x = new_x
            self.y = new_y

    def left(self):
        if self.facing:
            self.facing = DIRECTIONS[(DIRECTIONS.index(self.facing) - 1) % 4]

    def right(self):
        if self.facing:
            self.facing = DIRECTIONS[(DIRECTIONS.index(self.facing) + 1) % 4]

    def report(self):
        if self.x is not None and self.y is not None and self.facing:
            print(f"{self.x},{self.y},{self.facing}")
            