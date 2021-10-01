class Surface:
    def __init__ (self, xdim, ydim):
        self.xUpper = xdim
        self.yUpper = ydim
        self.xLower = 0
        self.yLower = 0

    # Checks to see whether the robot is within the boundaries of the surface
    def checkBoundary(self, robot):
        if (self.xUpper, self.yUpper) >= robot.getNextPos() and (self.xLower, self.yLower) <= robot.getNextPos():
            return True

        return False

    def getXUpper(self):
        return self.xUpper
    
    def getYUpper(self):
        return self.yUpper
    
    def getXLower(self):
        return self.xLower

    def getYLower(self):
        return self.yLower

    # Explicitly check whether the surface contains a coordinate
    def inBoundary(self, x, y):
        if self.xLower <= x <= self.xUpper and self.yLower <= y <= self.yUpper:
            return True
        return False
