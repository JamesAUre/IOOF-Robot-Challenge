from robot import Robot
from surface import Surface

class Controller:
    def __init__ (self):
        self.surface = Surface(5, 5)
        self.robotCount = 0
        self.robots = []
        self.activeRobot = None
    
    # places a new robot on the surface
    def placeRobot(self, x, y, f):
        if (self.surface.inBoundary(x,y)):
            self.robotCount += 1
            if self.robotCount == 1: self.activeRobot = 0
            self.robots.append(Robot(x, y, f))

    # move the robot on the surface
    def move(self):
        if self.surface.checkBoundary(self.robots[self.activeRobot]):
            self.robots[self.activeRobot].move()

    def rotate(self, dir):
        self.robots[self.activeRobot].rotate(dir)

    def setActiveRobot(self, num):
        self.activeRobot = num - 1

    # generates the report
    def getData(self):
        output = "Robot count: {}\n".format(self.robotCount)

        for i in range(len(self.robots)):
            if i == self.activeRobot:
                output += "ROBOT {} (ACTIVE)\n Coordinates: {} Facing: {}\n".format(i + 1, self.robots[i].getCoords(), self.robots[i].getFacing())

            else:
                output += "ROBOT {} \n Coordinates: {} Facing: {}\n".format(i + 1, self.robots[i].getCoords(), self.robots[i].getFacing())
        
        return output

    def getActiveRobotCoord(self):
        return self.robots[self.activeRobot].getCoords()

    def getRobotCount(self):
        return self.robotCount

    def getActiveIndex(self):
        return self.activeRobot

