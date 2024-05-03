

## Define a map and let the player move around it
#Define our map: 1 = wall, 0 = path
#0,0 is the top left of the map, therefore...
#moving up decreases the y location and
#moving left decreases the x location and vice versa

Map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, -2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, -1, -1, -1, -1, 1, 1],
    [1, 0, 0, 0, 0, 0, -1, -1, -1, -1, 1, 1],
    [1, 0, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1],
    [1, 0, 1, 0, 0, 1, -1, 1, 1, 1, -1, -3],
    [1, 0, 1, 0, 1, 1, -1, -1, -1, -1, -1, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#0=space where you can move
#-1=minefield
#-2=minefield toggle
#make it so that -1 is a minefield, so, it is solid and you can
#only pass through two mines before you die (restart)
#you have to find the switch to deactivate the minefield to pass to the next obstacle
#which is going to be 
#Define a function to print our Map and current Player location

def drawMap(currX, currY):
    #print ("map size is : ", len(Map), " rows by ", len(Map[0]), " columns")
    print()
    for y in range(0, len(Map)):
        for x in range(0, len(Map[y])):
            if (currX == x) and (currY == y):   # print * if they are in this square
                print("* ", end="")
            else:
                if Map[y][x] == 0:
                    print("  ", end="")
                if (currX == 1) and (currY == 1) and MineStatus==True:
                    terminal()
                else:
                    elif Map[y][x] == 1:
                        print("▧", end=" ")
                    elif Map[y][x] == -2:
                        print("?", end=" ")
                    elif Map[y][x] == -1:
                        print("x", end=" ")
                    elif Map[y][x] == -3:
                        print("𓉞", end=" ")
                
                    else:
                        print(Map[y][x], "", end="")
        print()
    print()
    
def welcomeMsg():
    name=input("Hello, Traveler. Please enter your name: ")
    print("Hello, ", name, "\n Beware. this dungeon has mines in it, but dont fret, \n a mine deactivator is somewhere here \n find all 5 numbers around the map to deactivate the mines and win.")
#Define our function that will move the player
#The function will first check if the player can move or hits a wall
#If the player can move, then the current location will be updated
#If the player cannot move due to a wall, the location will not be updated
    
def movePlayer(x,y,moveDir):
    #assume invalid move is attempted
    badMove = True

    #Now check if the move is valid - brute force method - better ways exist
    #doing an experiment with moveplayer function. Added a specific condition where you can move through minefield if it is turned off, 
    
    if moveDir == "w":
        if Map[y-1][x] <= 0 or Map[y][x+1] == 5:
            #print ("valid up move")
            return (x, y-1)

    if moveDir == "s":
        if Map[y+1][x] <= 0 or Map[y][x+1] == 5:
            #print ("valid down move")
            return (x, y+1)

    if moveDir == "a":
        if Map[y][x-1] <= 0 or Map[y][x+1] == 5:
            #print ("valid left move")
            return (x-1, y)

    if moveDir == "d":
        if Map[y][x+1] <= 0 or Map[y][x+1] == 5:
            #print ("valid right move")
            return (x+1, y)
            
    #they attempted a bad move
    if badMove:
        print ("**Invalid move** Try again.")
        return (x,y)   #return the same location they are in since no move

#made a terminal that is a question mark on the map; when player steps up to terminal he gets prompted to disable mines
#however, still unknown how to do list operation to change values to make mines pass-through
def terminal():
    MineStatus=True
    code=int(input("TERMINAL3847: greetings, AGENT. Please enter 5-digit access code: "))
    if code==("34873"): #make random num for code
        MinePrompt=input("disable mines? (y/n)")
        if MinePrompt=="y":
            MineStatus=False
    else:
        print ("Invalid Code!")
    return MineStatus
    


#Set our starting location
currX = 1
currY = 4

#draw the map the first time before asking for a move
welcomeMsg()
drawMap(currX, currY)
#Forever just let the player move around the map on the path

while True:
    moveDir = input("Enter direction (u,d,l,r): ")
    currX, currY = movePlayer(currX, currY, moveDir)
    drawMap(currX, currY)

    
