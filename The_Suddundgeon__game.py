############################
##copyrighted (jk)
##by Sudharshan SambathKumar
##Warning to those, this is a very messy first piece of code. ime working to make it better and add more story
##if your reading this, thank you.




def intro():
    print("##################")
    print("##welcome to the##")
    print("###SUDDUNGEON!!###")
    print("##################")
    print()
    print("dare ye enter? y/n")
    answer = input()
    if answer == "y" or answer == "Y":
        print("Then Enter!!")
        lb()
        print("You wake up")
        play()
        
    elif answer == "n" or answer == "N":
        print("That's too bad")
        print("------------------------game--over-----------------------------")
    else:
        print("invalid answer")
        intro()
def gamelose():
    print("'I told you to do nothing!!!' the voice booms")
    print("You hear an explosion, before you feel a searing heat as your flesh melts off your bones")
    gameover()
def gamewin():
    print("Well done. you win")
    exit()
    #############################replace Riddle for room 3 with a riddle (use find and replace. replace the word "Riddle" with a riddle###############################
## put linebreak before and after every text and before each question (question includes optionbs)
## all objects and items are capitilsed
use_answer= 0
otheruse_answer = 0
## stuff
items = ["Nothing",]
objects = [["Left Door", "Middle Door","Right Door"],["Slime","Golden Door","Wooden Door"],["Tablet","Wooden Door"],["Darkness"]]
titles = ["","The Stone Room Of Three Doors","The Metal Room Of The Slime","The Gold Room Of The Riddle","The Room of Nothing"]
####
## unique variables for each room
room1RightDoorUnlocked = 0
room1LeftLooked = 0
room2SlimeDead = 0
room2GoldDoorUnlocked = 0
impulse = 0
room3Sword = 0
##################################################################################
def lb():
    print("---------------------------------------")
x=0
y=0
z=0
def gameover():
    print("------------------------game--over-----------------------------")
    print("( 1 )restart room ")
    print("( 2 )restart game ")
    answer = input()
    global room
    if answer == "1":
        if room == 4:
            print("Too bad. no restart room for you")
            exit()
        play()
    if answer == "2":
        room = 1
        items = ["Nothing"]
        objects = [["Left Door", "Middle Door","Right Door"],["Slime","Golden Door","Wooden Door"],["Tablet","Wooden Door"],["Darkness"]]
        play()
def resetSelf():
    f=0
    while f < len(objects):
        objects[f].remove("Self")
        f =f +1
room = 1

##room texts
def room1T():
    print("You are in a dark room made of stone. Stone walls stone roof,")
    print("everything is stone except for 3 wooden doors embedded in the eastern ")
    print("wall, each with iron outlines.")
def room2T():
    global room2SlimeDead
    if room2SlimeDead == 0:
        print("This room is a huge metal box.In the middle of it oozes a tiny ")
        print("Slime. It sees you and starts advancing. ")
        print("Embedded in the eastern wall is a golden door, and in the western")
        print("wall is a wooden one with iron outlines")
    else:
        print("This room is a huge metal box.")
        print("Embedded in the eastern wall is a golden door, and in the western")
        print("wall is a wooden one with iron outlines")
    #if impulse == 1:
        #room2SlimeDead = 1 (just do this from now on)
    try:
        if room2SlimeDead == 1:
            objects[room-1].remove("Slime")
    except:
        objects[room-1].append("Slime")
        objects[room-1].remove("Slime")
    finally:
        objects[room-1].append("s")
        objects[room-1].remove("s")
def room3T():
    print("You are in a small cupboard sized room made enirely of a smooth gold")
    print("except for the floor which is a nice red carpet.")
    if "Sword" in objects[room-1]:
        print("On the eastern side of the room is a sword embedded into the wall")
    elif "Hole" in objects[room-1]:
        print("On the Eastern side of the room is a palm sized circular hle that goes into the wall")
    else:
        print("On the eastern side of the room, embedded in the wall, is a tablet stating")
        print('"Select the symbol of Sud"')
        
def room4T():
    print("You are surrounded in darkness. Suddenly, you hear a deep booming voice say")
    print("'Do nothing, and you win'")
texts = [room1T, room2T, room3T, room4T]
####################################
def nothink():
    print("you can't think how to use that there")

####################################
##items endings
#(y = item, z = object/other item)
#univ items are sword, void sword, green,red,gold, purple vials. and lighter
def SelfE():
    if y == "Sword" or "VoidSword":
        print("you stab yourself. idk why you did that.")
        print("you die")
        gameover()
    #else:
 #       nothink()
def itemE():
    print("itemE")
    
def item_ending():
    global y
    global z
    global room
    global impulse
    if y == "Sword":
        if z == "Self":
            print("You stab yourself with the sword and die")
            gameover()
        if room == 1:
            print("You attack the door with your sword")
            print("Nothing happens to the door, but you sword shatters and breaks")
            items.remove("Sword")
        if room == 2:
            if z == "Slime":
                print("The slime jumps at you, but you slice the Slime in half midair, killing it. Its remains disappear into a mist before they even hit the floor")
                objects[room-1].remove("Slime")
            if z == "Golden Door" or z == "Wooden Door":
                print()
            if z == "Hidden Switch":
                print("You attack the hidden switch with surprising accuracy")
                print("You break the switch, and your sword shatters on contact with the gold of the door he switch was hiding in")
                items.remove("Sword")
                objects[room-1].remove("Hidden Switch")
            else:
                nothink()
        if room == 3:
            if z == "Wooden Door":
                print("You attack the",z,"with your sword")
                print("The Sword shatters on impact")
                items.remove("Sword")
                print("Unfortunatly, the",z,"does not seem to even be scratched")
            if z == "Hole":
                print("You insert the sword back into the hole, and it disappeares along with the hole.")
                print("The Tablet reappers")
                objects[room-1].append("Tablet")
                objects[room-1].append("@ symbol")
                objects[room-1].append("£ symbol")
                objects[room-1].append("$ symbol")
                objects[room-1].remove("Hole")
                items.remove("Sword")
            else:
                nothink()
        if room == 4:
            gamelose()
    if y == "Lighter":
        if z == "Self":
            print("You hold the lighter to your hand.")
            print("You feel a searing pain and pull the flame away before you burn yourself.")
        if room == 1:
            print("You try to burn the door, but it seems impervious to flame")
        if room == 2:
            if z == "Golden Door" or z == "Hidden Switch":
                print("The door surprisingly catches fire, but as it burns away, it leaves behind not an open passage, but a blank wall")
                objects[room-1].remove("Golden Door")
            if z == "Wooden Door":
                print("You try to burn the door, but it seems impervious to flame")
        if room == 4:
            gamelose()
        else:
            nothink()

##################################

##interact endings
#y=object

def room1Int():
    global room
    global y
    if y == "Left Door":
        print("You go through the left door")
        room = 2
    if y == "Middle Door":
        print("You go through the middle door")
        room = 3
    if y == "Right Door" and room1RightDoorUnlocked == 0:
        print("The door is locked")
    if y == "Right Door" and room1RightDoorUnlocked == 1:
        print("You go through the right door")
        room = 21
def room2Int():
    global y
    global room
    global room2SlimeDead
    global room2GoldDoorUnlocked
    global impulse
    ##need to add slime attacking you if not dead and you interact.
    if y == "Wooden Door":
        print("You go through the door.")
        room = 1
    if y == "Golden Door":
        if room2GoldDoorUnlocked == 0:
            print("The door is locked")
            if room2SlimeDead == 0:
                print("While you spend your time trying to open it, the slime in the room jumps on you, sinking into your pores, and into your brain.")
                print("You feel it making you more impulsive")
                room2SlimeDead = 1
                impulse = 1
        else:
            print("You go through the door")
            room = 4
    if y == "Hidden Switch":
        if room2GoldDoorUnlocked == 0:
            print("You hear the sound of a lock opening behind the gold door.")
            room2GoldDoorUnlocked = 1
        elif room2GoldDoorUnlocked == 1:
            print("You hear the sound of a lock closing behind the gold door.")
            room2GoldDoorUnlocked = 0
    if y == "Slime":
        print("You walk over to the slime to touch it")
        print("The slime jumps on you, sinking into your pores, and into your brain")
        print("You feel it making you more impulsive")
        impulse = 1
        room2SlimeDead = 1
def room3Int():
    global room
    global y
    global x
    global z
    if y == "Wooden Door":
        print("You go through the door")
        room = 1
    if y == "Tablet":
        print("You touch the tablet. Nothing happens.")
    if y == "Hole":
        print("you put you hand into the hole. Nothing happens. You pull yoiur hand out of the hole")
    if y == "$ symbol":
        print("the tablet falls away, revealing a sword embedded in the wall")
        objects[room-1].append("Sword")
        objects[room-1].remove("Tablet")
        objects[room-1].remove("$ symbol")
        objects[room-1].remove("£ symbol")
        objects[room-1].remove("@ symbol")

    if y == "@ symbol" or y == "£ symbol":
        print("As soon as you touch the symbol, the room explodes.")
        print("You feel a searing pain all over your body before you black out.")
        gameover()
    if y == "Sword":
        print("you pull the sword out of the hole")
        objects[room-1].remove("Sword")
        objects[room-1].append("Hole")
        items.append("Sword")
def room4Int():
    gamelose()
interact_endings = [room1Int,room2Int,room3Int,room4Int]

####################################

##inspect endings
#y=object
def item_look():
    if z == "Sword":
        print("It is a sword with an ornatley crafted silver blade and hilt, mahogany handle, and with a ruby jewel attached to the pommel")
def room1Look():
    global room
    global y
    global room1LeftLooked
    if y == "Left Door":
        print("The left door has the runes £$%%$£^&^ engraved into it. Apart from that, it is completely normal")
        room1LeftLooked = 1
    if y == "Middle Door":
        print("the middle door has nothing special about it. its just a wooden door")
    if y == "Right Door":
        print("the right door has nothing special about it. its just a wooden door. However, it is locked.")

def room2Look():
    global impulse
    global room2SlimeDead
    global room
    global y
    if y == "Golden Door":

            print("The door is made from a very shiny gold metal.")
            print("You spot a hidden switch in the ornate patterns decorating it")
            if room2SlimeDead == 1:
                if "Hidden Switch" not in objects[room-1]:
                    objects[room-1].append("Hidden Switch")
                else:
                    items.append("S")
                    items.remove("S")
            else:
                if "Hidden Switch" not in objects[room-1]:
                    objects[room-1].append("Hidden Switch")
                else:
                    items.append("S")
                    items.remove("S")
            
                print("While you spend your time admiring it, the slime in the room jumps on you, sinking into your pores, and into your brain.")
                print("You feel it making you more impulsive")
                impulse = 1
                room2SlimeDead = 1
                
    if y == "Wooden Door":
        print("Its a wooden door rimmed with iron")
    if y == "Hidden Switch":
        print("Its a switch hidden in the ornate patterns decorating the Golden Door")
        if room2SlimeDead == 0:
            print("While you spend your time admiring it, the slime in the room jumps on you, sinking into your pores, and into your brain.")
            print("You feel it making you more impulsive")
            impulse = 1
            room2SlimeDead = 1
                
        else:
            play()
    if y == "Slime":
        print("Its a small gelatinous cube the size of a dog that is moving towards you.")
        print("While you spend your time admiring it, it jumps on you, sinking into your pores, and into your brain")
        print("You feel it making you more impulsive")
        impulse = 1
        room2SlimeDead = 1
                
    if y == "Wooden Door":
        print("Its just a wooden door.")
        if room2SlimeDead == 0:
            print("While you spend your time admiring it, the slime in the room jumps on you, sinking into your pores, and into your brain.")
            print("You feel it making you more impulsive")
            impulse = 1
            room2SlimeDead = 1
                
        else:
            play()
def room3Look():
    if y == "Tablet":
        print("The words 'Select the symbol of Sud' are written on it")
        print("Below it are the symbols @,£, and $")
        if "ᛋ symbol" not in objects[room-1]:
            objects[room-1].append("$ symbol")
            objects[room-1].append("£ symbol")
            objects[room-1].append("@ symbol")
        else:
            items.append("S")
            items.remove("S")
    if y == "Hole":
        print("It is a palm sized circular hole that goes in very deep into the wall.")
    if y == "Sword":
        print("It is an ornately crafted silver blade, half embedded in the golden wall, with a nice mahogany handle, silver hilt and a ruby jewel on the pommel")
    if y == "$ symbol" or y == "£ symbol" or y == "@ symbol":
        print("It is a strange rune of sorts, engraved into the tablet")
        if y == "$ symbol" and room1LeftLooked == 1 :
            print("This symbol looks similar to the one on the Left door of the first room")
def room4Look():
    gamelose()
inspect_endings = [room1Look,room2Look,room3Look, room4Look]
########################################################################################################################################

def use_item():
    global room
    global x
    global z
    global y
    global use_answer
    global otheruse_answer
    x=0
    y=0
    z=0
    lb()
    print("what do you use")
    while len(items)> x:
        print("(",x+1,")","use",items[x])
        x=x+1
    try:
        use_answer = int(input())##
    except:
        print("invalid answer")
        play()
    finally: 
        if use_answer<=len(items) and use_answer>0:
            y = items[use_answer-1]
            x=0
            if y != "Nothing":
                lb()
                print("what do you use",y,"on?")
                print("( 1 ) on another item?")
                f = 0
                while f < len(objects):
                    objects[f].append("Self")
                    f =f +1
                while len(objects[room-1])> x:
                    print("(",x+2,")","on",objects[room-1][x])
                    x+=1
                try:
                    otheruse_answer = int(input())
                except:
                    print("invalid answer")
                    resetSelf()
                    play()
                finally:
                    if otheruse_answer <= len(objects[room-1])+1 and otheruse_answer > 0 :
                        z = objects[room-1][otheruse_answer-2]
                        
                        if otheruse_answer == 1:
                            f=0
                            
                            items.remove(y)
                            while f < len(items):
                                print("(",f+1,")", "on",items[f])
                                f = f+1
                            try:
                                otherotheruse_answer = int(input())
                            except:
                                print("invalid answer")
                                resetSelf()
                                play()
                            finally:
                                if otherotheruse_answer <= len(items) and otherotheruse_answer > 0 :
                                    z = items[otherotheruse_answer-1]
                                    items.append(y)
                                    
                                    if z != "Nothing":
                                        lb()
                                        item_ending()
                                        resetSelf()
                                        play()
                                    else:
                                        resetSelf()
                                        play()
                                        
                        elif z != "Nothing":  
                            lb()
                            item_ending()
                            resetSelf()
                            play()
                        elif room == 4 and z == "Nothing":
                            gamewin()
                        else:
                            resetSelf()
                            play()
            elif room == 4 and y == "Nothing":
                gamewin()
            else:
                play()
                
        else:
            print("invalid answer")
            play()

#######################################

def interact():
    global room
    global x
    global z
    global y
    global use_answer
    x=0
    y=0
    z=0
    lb()
    print("interact with?")
    while len(objects[room-1])> x:
        print("(",x+1,")","interact with",objects[room-1][x])
        x+=1
    try:
        use_answer = int(input())##
    except:
        print("invalid answer")
        play()
    finally:
        
        if use_answer <= len(objects[room-1]) and use_answer > 0:
            y = objects[room-1][use_answer-1]
            if y != "Nothing":
                lb()
                interact_endings[room-1]()
                play()
            elif room == 4 and y == "Nothing":
                gamewin()
            else:
                play()
        else:
            print("invalid answer")
            play()
#######################################
            
def inspect():
    global room
    global x
    global z
    global y
    global use_answer
    x=0
    y=0
    z=0
    lb()
    print("inspect what?")
    objects[room-1].append("An Item")
    while len(objects[room-1])> x:
        print("(",x+1,")","inspect",objects[room-1][x])
        x+=1
    try:
        use_answer = int(input())##
    except:
        print("invalid answer")
        play()
    finally:
        if use_answer <= len(objects[room-1]) and use_answer > 0:
            y = objects[room-1][use_answer-1]
            objects[room-1].remove("An Item")
            if y == "An Item":
                x = 0
                lb()
                print("Inspect what?")
                while len(items) > x:
                    print("(",x+1,")","inspect",items[x])
                    x = x+1
                try:
                    use_answer = int(input())
                except:
                    print("Invalid anwer")
                    play()
                finally:
                    if use_answer <= len(items):
                        z = items[use_answer-1]
                        if z != "Nothing":
                            z = items[use_answer-1]
                            item_look()
                            play()
                        elif z == "Nothing" and room ==4:
                            gamewin()
                        else:
                            play()
                    else:
                        print("invalid answer")
                        play()
            elif y != "Nothing":
                lb()
                inspect_endings[room-1]()
                play()
            elif room == 4 and y == "Nothing":
                gamewin()
            else:
                play()
        else:
            print("invalid answer")
            play()
#######################################
def play():
    
    global impulse
    if impulse == 1:
        f = 0
        while f < len(objects):
            objects[f].remove("Nothing")
            f =f+1
        impulse = 0
        lb()
        print(titles[room],":")
        texts[room-1]()
        lb()
        print("what do you do?")
        print("( 1 ) use item" )
        print("( 2 ) interact with room" )
        print("( 3 ) inspect room")
        answer = input()
        if answer == ("1"):
            use_item()
        elif answer == ("2"):
            interact()
        elif answer == ("3"):
            inspect()
        else:
            print("invalid answer")
            play()
    else:
        lb()
        print(titles[room],":")
        texts[room-1]()
        lb()
        print("what do you do?")
        print("( 1 ) use item ")
        print("( 2 ) interact with room")
        print("( 3 ) inspect room")
        answer = input()
        if answer == ("1"):
            use_item()
        elif answer == ("2"):
            interact()
        elif answer == ("3"):
            inspect()
        else:
            print("invalid answer")
            play()
f = 0
while f < len(objects):
    objects[f].append("Nothing")
    f =f+1
intro()
