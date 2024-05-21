import random
import time
#Philipp's Adventure Game
## Define a map and let the player move around it
#Define our map: 1 = wall, 0 = path
#0,0 is the top left of the map, therefore...
#moving up decreases the y location and
#moving left decreases the x location and vice versa
WALL=1
M=2
SECRET=-4
NUMBER=-9
KEYCARD=-20
DOOR=-3
TERMINAL=-2
POTATO=-69
CurrCount=1
keys=[]
found_numbers=[]
Map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, -2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, -4, -4, -9, 1, 1],
    [1, 1, 1, -9, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, -9, 1, 0, 0, 0, -9, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, M, M, M, M, 1, 1],
    [1, 0, 0, 0, 0, 0, M, M, M, M, 1, 1],
    [1, 0, 1, 1, 1, 1, M, M, M, M, M, 1],
    [1, -69, 1, 0, -9, 1, M, 1, 1,M, M, -3],
    [1, 0, 1, 0, 1, 1, M, M, M, M, M, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, -20, 0, 0, -9, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, -9, 0, 0, 0, 0, 0, 0, 0, -9, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#0=space where you can move
#2=minefield
#-2=minefield toggle
#-9=a number
#-3=exit
#-4=secret passageway
#make it so that -1 is a minefield, so, it is solid and you can
#only pass through two mines before you die (restart)
#you have to find the switch to deactivate the minefield to pass to the next obstacle
#which is going to be 
#Define a function to print our Map and current Player location

def drawMap(currX, currY):
    global CurrCount, keys, inverted_turns, M
    NumFound=False
    #print ("map size is : ", len(Map), " rows by ", len(Map[0]), " columns")
    print()
    for y in range(0, len(Map)):
        for x in range(0, len(Map[y])):
            if (currX == x) and (currY == y):   # print * if they are in this square
                print("* ", end="")
            if Map[y][x]==NUMBER and currX== x and currY == y:
                if CurrCount==1: #I was kind of stuck here so I looked this part up
                    if not num1 in found_numbers: #I kind of learned how to use the not parameter and how to use the not in. the not is kind of similar to the "!="
                        found_numbers.append(num1)
                        print ("You found it! 1st num is", num1)
                        CurrCount+=1
                elif CurrCount==2:
                    if not num2 in found_numbers:
                        found_numbers.append(num2)
                        print ("Boom! 2nd num is", num2)
                        CurrCount+=1
                elif CurrCount==3:
                    if not num3 in found_numbers:
                        found_numbers.append(num3)
                        print ("You found it! 3rd num is", num3)
                        CurrCount+=1
                elif CurrCount==4:
                    if not num4 in found_numbers:
                        found_numbers.append(num4)
                        print ("You found the one! 4th num is", num4)
                        CurrCount+=1
                elif CurrCount==5:
                    if not num5 in found_numbers:
                        found_numbers.append(num5)
                        print ("You did it! 5th num is", num5)
                        CurrCount+=1

                        
                
            if Map[y][x]==KEYCARD and currX== x and currY == y and len(keys)==0:
                print ("You picked up a keycard.")
                keys.append("Keycard") #keycards
            if Map[y][x]==TERMINAL and currX== x and currY == y and MineStatus==True and InteractionComplete==False:
                terminal() #terminal; basically just prompts the player if he steps on the coordinates with the terminal when the minefield is active
            if Map[y][x]==-69 and currX== x and currY == y:  # Potato
                eat_potato = input("You have not eaten for days but at last, you found an uncooked potato. Do you want to eat it? (y/n): ")
                if eat_potato.lower() == 'y':
                    print("You eat the potato...")
                    invert_directions(currX, currY)
            if Map[y][x]==DOOR and currX== x and currY == y and len(keys)==1:
                win()
            #while (currX == 1) and (currY == 1) and MineStatus==True and Interaction:
               #terminal()
            #if (currX == 16) and (currY == 9) and MineStatus==False:
                #win()
            else:
                if MineStatus == False and (Map[y][x] == M):
                    print(" ", end="")
                else:
                    if Map[y][x] == 0:
                        print("  ", end="")
                    elif Map[y][x] == WALL:
                        print("▧", end=" ")
                    elif Map[y][x] == SECRET:
                        print("▧", end=" ")
                    elif Map[y][x] == TERMINAL:
                        print("?", end=" ")
                    elif Map[y][x] == 2:
                        print("x", end=" ")
                    elif Map[y][x] == -1:
                        print(" ", end=" ")
                    elif Map[y][x] == DOOR:
                        print("𓉞", end=" ")
                    elif Map[y][x] == KEYCARD:
                        print(" ", end=" ")
                    elif Map[y][x] == NUMBER:
                        print(" ", end=" ")
        print()
    print()


def invert_directions(currX, currY):  # Added an invert directions function for when player eats the poisonous potato
    global inverted_turns  
    inverted_turns = 4  
    print("You feel weird after eating the potato, almost as if everything is uʍop ǝpᴉsdn???")
def welcomeMsg():
    name=input("Hello, Traveler. Please enter your name: ")
    print("Hello, ", name, "\n Beware. this dungeon has mines in it that will all explode in 5 minutes, burying you inside of this dungeon, but dont fret, \n a mine deactivator is somewhere here \n find all 5 numbers around the map to deactivate the mines and win.")
#Define our function that will move the player
#The function will first check if the player can move or hits a wall
#If the player can move, then the current location will be updated
#If the player cannot move due to a wall, the location will not be updated
    
def movePlayer(x,y,moveDir):
    global M
    #assume invalid move is attempted
    badMove = True

    #Now check if the move is valid - brute force method - better ways exist
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
def terminal():
    global MineStatus, InteractionComplete, M
    InteractionComplete=False #making a flag so player doesn't get stuck at the terminal forever
    MineStatus=True #change logic because mines will activate every time you enter terminal
    print (num1, num2, num3, num4, num5)
    code=int(input("TERMINAL3847: greetings, AGENT. Please enter 5-digit access code: "))
    if code==(num1*10000)+(num2*1000)+(num3*100)+(num4*10)+(num5) and InteractionComplete==False: #make random num for code
        MinePrompt=input("[disable mines? (y/n)")
        if MinePrompt=="y":
            MineStatus=False
            InteractionComplete=True
            M=-1
        if MinePrompt=="n":
            Boomprompt=input("detonate Mines? (y/n)")
            if Boomprompt=="y":
                print("boom") #I will make it so that the prompt from the events() function activates
                InteractionComplete=True
            if Boomprompt=="n":
                print ("Diagnostics complete, have a nice day, AGENT")
                InteractionComplete=True
    if MineStatus==False:
        M=-1

    elif code!=num1:
        print ("Invalid Code!")
        InteractionComplete=True
    else:
        print ("error!")
    if  InteractionComplete==True:
        ("🃑")
        return (currX+1, currY)
    return MineStatus
#making a mechanic for the terminal code, so that it is completely random for higher replayability
##def DungeonCode(num1):
##    num1=random.randint(10001, 99999)
##    #print ("dungeon code is", num1, num2, num3, num4, num5)
##    return num1

def events():
    Chance=random.randint(0,30)
    if Chance==13:
        print(" ")
    if AutoDetonation==True:
        print("You were unsuccessful. The mines exploded and you now hear the walls and the roof coming in on you \n The greeting voice that asked you for your name disappeared altogether \n was it ever even there..?")
        time.sleep(15)
        exit()
#added a countdown function to use for events with a switch that will turn on when time's up
def countdown(time_sec):
    global Toggle
    while time_sec:
        mins, secs = divmod(time_sec, 300)
        time.sleep(1)
        time_sec -= 1
    if time_sec == 1:
        print("demise imminent")
        Toggle=True

    return Toggle

def win():
    print("You have won. You run up the stairs of the dungeon and hear the room collapsing behind you. \n if you waited a second longer, you would have probably died")
    time.sleep(10)
    exit()
#Set our starting location
currX = 1
currY = 4
num1=random.randint(0,9)
num2=random.randint(0,9)
num3=random.randint(0,9)
num4=random.randint(0,9)
num5=random.randint(0,9)
inverted_turns = 0
##DungeonCode(num1)
AutoDetonation=0
#adding global variables to be used by the functions
MineStatus=True
InteractionComplete=False
Toggle=False
#draw the map the first time before asking for a move
welcomeMsg()
drawMap(currX, currY)

#Forever just let the player move around the map on the path

while True:
    print ("value of mines is", M)
    moveDir = input("Enter direction (w, a, s, d): ")
    if inverted_turns > 0:  # Made a a statement that inverts the players turns while the potato effect is active
        if moveDir == "w":
            moveDir = "s"
        elif moveDir == "s":
            moveDir = "w"
        elif moveDir == "a":
            moveDir = "d"
        elif moveDir == "d":
            moveDir = "a"
        inverted_turns -= 1
    currX, currY = movePlayer(currX, currY, moveDir)
    drawMap(currX, currY)
#test
    
