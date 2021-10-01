from vec import Vec, Dir

class Robot:
    def __init__(self, x, y, f):
        self.coords = Vec(x, y)
        self.facing = Robot.getDir(f)

    def getCoords(self):
        return self.coords.getCoords()

    # Returns where its next position will be if it moves
    def getNextPos(self):
        (x, y) = self.coords.getCoords()
        (xf, yf) = self.facing.getCoords()
        return (x + xf, y + yf)

    def move(self):
        self.coords.addCoords(self.facing)

    def rotate(self, dir):
        if dir == "RIGHT":
            self.facing.rotateRight()

        if dir == "LEFT":
            self.facing.rotateLeft()

    # Will return a string indicating its direction
    def getFacing(self):
        return self.facing.get()

    # Generates a direction object based on string input
    def getDir(f):
        if f == "SOUTH":
            return Dir(0, -1)

        elif f == "WEST":
            return Dir(-1, 0)

        elif f == "EAST":
            return Dir(1, 0)

        elif f == "NORTH": 
            return Dir(0, 1)

        else:
            raise IOError("Invalid direction given.")