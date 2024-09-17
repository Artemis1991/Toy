import unittest
from Toy import ToyRobot

class TestToyRobotWithObstacles(unittest.TestCase):

    def setUp(self):
        self.robot = ToyRobot()
        self.obstacles = [(1, 1), (2, 2)]  # Example obstacles

    def test_place_robot_avoids_obstacles(self):
        # Test placing robot on an obstacle
        self.robot.place(1, 1, "NORTH", self.obstacles)
        self.assertIsNone(self.robot.x, "Robot should not be placed on an obstacle")
    
    def test_move_robot_into_obstacle(self):
        # Test robot doesn't move into obstacle
        self.robot.place(1, 0, "NORTH", self.obstacles)
        self.robot.move()  # Shouldn't move into (1, 1)
        self.assertEqual((self.robot.x, self.robot.y), (1, 0), "Robot should not move into an obstacle")

    def test_move_robot_successfully(self):
        # Test robot moves correctly when no obstacle
        self.robot.place(0, 0, "NORTH", self.obstacles)
        self.robot.move()  # Should move to (0, 1) since no obstacle
        self.assertEqual((self.robot.x, self.robot.y), (0, 1), "Robot should move normally without obstacles")

if __name__ == '__main__':
    unittest.main()
