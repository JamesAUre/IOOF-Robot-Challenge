class Vec:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getCoords(self):
        return (self.x, self.y)

    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y

    def setCoords(self, x, y):
        self.x = x
        self.y = y

    def addCoords(self, vec):
        (x, y) = vec.getCoords()
        self.x += x
        self.y += y

# A vector that specifies the direction the object is moving in
class Dir(Vec):
    dirs = [(0,1), (1,0), (0, -1), (-1, 0)]

    def __init__(self, x=0, y=0):
        x = max(-1, min(1, x))
        y = max(-1, min(1, y))

        if (x, y) == (0,0):
            x = 1
        
        Vec.__init__(self, x, y)

    # change direction to left 90 degrees
    def rotateLeft(self):
        for i in range(len(Dir.dirs)):
            if (self.x,self.y) == Dir.dirs[i]:
                (self.x, self.y) = Dir.dirs[(i-1) % len(Dir.dirs)]
                break

    # change direction to right 90 degrees
    def rotateRight(self):
            for i in range(len(Dir.dirs)):
                if (self.x,self.y) == Dir.dirs[i]:
                    (self.x, self.y) = Dir.dirs[(i+1) % len(Dir.dirs)]
                    break
    
    # get direction as a string description
    def get(self):
        if (self.x, self.y) == Dir.dirs[0]:
            return "NORTH"

        elif (self.x, self.y) == Dir.dirs[1]:
            return "EAST"

        elif (self.x, self.y) == Dir.dirs[2]:
            return "SOUTH"

        elif (self.x, self.y) == Dir.dirs[3]:
            return "WEST"