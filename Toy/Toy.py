TABLE_SIZE = 5
DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]

class ToyRobot:
    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None
    def place(self, x, y, facing):
        if 0 <= x < TABLE_SIZE and 0 <= y < TABLE_SIZE and facing in DIRECTIONS:
            self.x = x
            self.y = y
            self.facing = facing
    def move(self):
        if self.facing == "NORTH" and self.y < TABLE_SIZE - 1:
            self.y += 1
        elif self.facing == "EAST" and self.x < TABLE_SIZE - 1:
            self.x += 1
        elif self.facing == "SOUTH" and self.y > 0:
            self.y -= 1
        elif self.facing == "WEST" and self.x > 0:
            self.x -= 1
    def left(self):
        if self.facing:
            self.facing = DIRECTIONS[(DIRECTIONS.index(self.facing) - 1) % 4]
    def right(self):
        if self.facing:
            self.facing = DIRECTIONS[(DIRECTIONS.index(self.facing) + 1) % 4]
    def report(self):
        if self.x is not None and self.y is not None and self.facing:
            print(f"{self.x},{self.y},{self.facing}")

def execute_commands():
    robot = ToyRobot()
    while True:
        command = input("Enter command (or type 'EXIT' to quit): ").strip().upper()
        if command == "EXIT":
            print("Exiting the program.")
            break
        if command.startswith("PLACE"):
            try:
                _, args = command.split()
                x, y, facing = args.split(',')
                robot.place(int(x), int(y), facing)
            except ValueError:
                print("Invalid PLACE command format. Correct format is: PLACE X,Y,FACING (e.g., PLACE 0,0,NORTH)")
        elif command == "MOVE":
            robot.move()
        elif command == "LEFT":
            robot.left()
        elif command == "RIGHT":
            robot.right()
        elif command == "REPORT":
            robot.report()
        else:
            print("Invalid command. Valid commands are: PLACE, MOVE, LEFT, RIGHT, REPORT, EXIT.")

# Run the program to accept user inputs
execute_commands()