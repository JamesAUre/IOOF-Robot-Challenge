from controller import Controller
import unittest

# to run these tests, type: python -m unittest tests.py
class TestController(unittest.TestCase):
    def test_ctrlr_count(self):
        testctrlr = Controller()
        
        # Initially, there should be 0 robots
        self.assertEqual(testctrlr.getRobotCount(), 0)

        # When we place in bounds, count should increase by 1
        testctrlr.placeRobot(1,1,"north")
        self.assertEqual(testctrlr.getRobotCount(), 1)

        # Out of bounds should not place the robot
        testctrlr.placeRobot(-1, -1, "north")
        self.assertEqual(testctrlr.getRobotCount(), 1)

        # Test for out of bounds on one axis
        testctrlr.placeRobot(6, 4, "south")
        self.assertEqual(testctrlr.getRobotCount(), 1)

        # Will still place after out of bounds entries if next one is in bounds
        testctrlr.placeRobot(3, 3, "east")
        self.assertEqual(testctrlr.getRobotCount(), 2)

    def test_movement(self):
        testctrlr = Controller()
        testctrlr.placeRobot(1,1,"north")
        testctrlr.move()

        # Move north should increment Y
        self.assertEqual(testctrlr.getActiveRobotCoord(), (1,2))

        testctrlr.move()
        testctrlr.move()

        # Can move multiple times
        self.assertEqual(testctrlr.getActiveRobotCoord(), (1,4))

        # Rotations dont move the robot
        testctrlr.rotate("RIGHT")
        self.assertEqual(testctrlr.getActiveRobotCoord(), (1,4))

        # After rotating right, robot should move on the x axis
        testctrlr.move()
        self.assertEqual(testctrlr.getActiveRobotCoord(), (2,4))

        # After rotating right again, it should move along the y axis (decrementing)
        testctrlr.rotate("RIGHT")
        testctrlr.move()
        self.assertEqual(testctrlr.getActiveRobotCoord(), (2,3))

        # Test whether left rotation works as well
        testctrlr.rotate("LEFT")
        testctrlr.move()
        self.assertEqual(testctrlr.getActiveRobotCoord(), (3,3))

        # Does behaviour maintain with a combination of different commands
        testctrlr.rotate("LEFT")
        testctrlr.rotate("RIGHT")
        testctrlr.rotate("LEFT")
        testctrlr.move()
        testctrlr.move()

        self.assertEqual(testctrlr.getActiveRobotCoord(), (3,5))

    def test_active_robot(self):

        # Should not have a active robot until placed
        testctrlr = Controller()
        self.assertEqual(testctrlr.getActiveIndex(), None)

        # Now it should be the first robot placed
        testctrlr.placeRobot(1,1,"north")
        self.assertEqual(testctrlr.getActiveIndex(), 0)

        # Keep the first robot placed as the active one
        testctrlr.placeRobot(3,3,"east")
        self.assertEqual(testctrlr.getActiveIndex(), 0)

        testctrlr.placeRobot(3,3,"east")
        self.assertEqual(testctrlr.getActiveIndex(), 0)

        # Can swap to another active robot when called
        testctrlr.setActiveRobot(3)
        self.assertEqual(testctrlr.getActiveIndex(), 2)