from controller import Controller

if __name__ == "__main__":
    placedRobots = 0
    newctrlr = Controller()

    # main loop for commands
    while(True):
        try:
            args = input("").upper().split()

            if args[0] == "PLACE":
                placeargs = args[1].split(",")
                newctrlr.placeRobot(int(placeargs[0]), int(placeargs[1]), placeargs[2])

            elif (newctrlr.robotCount):
                if args[0] == "MOVE":
                    newctrlr.move()

                elif args[0] == "LEFT" or args[0] == "RIGHT":
                    newctrlr.rotate(args[0])
                    
                elif args[0] == "REPORT":
                    print(newctrlr.getData())
                
                elif args[0] == "ROBOT":
                    newctrlr.setActiveRobot(int(args[1]))
                
                else:
                    raise IOError("Invalid command given.")

            else:
                print("You must place a robot first.")

        except IOError as e:
            print("Error in arguments: " + str(e))
