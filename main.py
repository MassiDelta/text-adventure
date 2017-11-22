import time
import random
import os
inventory = {
    'allen wrench':
        {'qty':0, 'equ':False},
    'wrench':
        {'qty':0, 'equ':False},
    'tape measure':
        {'qty':0, 'equ':False},
    'hammer':
        {'qty':0, 'equ':False},
    'stop sign hammer':
        {'qty':0, 'equ':False},
    'safety glasses':
        {'qty':0, 'equ':False},
    'climber rope':
        {'qty':0, 'equ':False},
    'driver station':
        {'qty':0, 'equ':False},
    'controller':
        {'qty':0, 'equ':False},
    'blueprints':
        {'qty':0, 'equ':False},
    'money':
        {'qty':2, 'equ':False},
    '1257 shirt':
        {'qty':1, 'equ':True},
    'candy':
        {'qty':0, 'equ':False},
    'jug of water':
        {'qty':0, 'equ':False},
    'scouting sheets':
        {'qty':0, 'equ':False},
    'driver pin':
        {'qty':0, 'equ':False},
    'toolbox key':
        {'qty':0, 'equ':False},
    'camera':
        {'qty':0, 'equ':False},
    'first aid':
        {'qty':0, 'equ':False},
    'gear rope sign':
        {'qty':0, 'equ':False},
    '1257 pin':
        {'qty':0, 'equ':False},
    '1676 pin':
        {'qty':0, 'equ':False},
    '2590 pin':
        {'qty':0, 'equ':False},
    '747 pin':
        {'qty':0, 'equ':False},
    '1923 pin':
        {'qty':0, 'equ':False},
    '3637 pin':
        {'qty':0, 'equ':False},
    '303 pin':
        {'qty':0, 'equ':False},
    '25 pin':
        {'qty':0, 'equ':False},
    '303 band':
        {'qty':0, 'equ':False}
}
pos = 0
immorality = 0
finalopen = False
scout = 0
insane = False
nemesisbot = True
gameteams = ['25', '2590', '747', '1676', '225', '341', '5895',  '3637', '365', '1089', '75', '193', '11', '303']
#below are variables for requirements for awards
spirit_shirt = True
spiritwin = False
#below are maps for player use
pitmap = """_____________________
|00|  |00|  |00|  |00|
|00|1 |00|2 |00|3 |00|
|00|  |00|  |00|  |00|
|00|  |00|  |00|  |00|
|00|              |00|
|00|   ____ ___   |00|
|00|  |        |  |00|
|00|4 |   6    |5 |00|
|00|  |        |  |00|"""
def invcheck():
    for item in inventory.keys():
        if inventory[item]['qty']>0:
            print(f'{item} - {inventory[item]["qty"]}')

def choose(n):
    while True:
        choice = input("What do you do?: ")
        ok = False
        while ok == False:
            ok = True
            valint = True
            try:
                int(choice)
            except ValueError:
                choice = input("Not a command, try again: ")
                ok = False
                valint = False
            if valint == True:
                choice = int(choice)
                if choice>n or choice<1:
                    choice = input("Not a command, try again: ")
                    ok = False
        choice=int(choice)
        move = options(choice)
        if move == "h":
            pass
        else:
            return move

def location():
    global pos
    while True:
        if pos == 0:
            print("\nYou are in the stands.\nAhead, you see an FRC STEAMWORKS field, but no robots are there.\nDespite this, there are past matches playing on the projector.\n1. get off the stands\n2. rummage through your bag\n3. scout a match\n4. item\n5. inventory")
            pos = choose(5)
        if pos == 1:
            print("\nYou find yourself in the hallway in the second floor.\n1. go into the stands\n2. head to the bathroom\n3. go south\n4. item\n5. inventory")
            pos = choose(5)
        if pos == 2:
            print("\nYou are in a long hallway, with stairs leading downstairs in the corner, and concession stands lining the inner side.\n1. go downstairs\n2. go north\n3. go to the pizza stand\n4. check out the condiment table\n5. item\n6. inventory")
            pos = choose(6)
        if pos == 3:
            print("\nYou are in the main lobby of Stabler Arena. Ahead, you see a small concession stand.\n1. go upstairs\n2. enter the pits\n3. look at the stand\n4. go to the main entrance\n5. item\n6. inventory")
            pos = choose(6)
        if pos == 4:
            print("You stand outside the bathroom, but the door is locked.\n1. go back\n2. wait\n3. open the door\n4. item\n5. inventory")
            pos = choose(4)
        if pos == 5:
            print("You are at the pizza stand. At the register, you see a small display rack with candy on it, and in the back you see an oven.\nMemories of awful pizza fill your head.\n1. go back\n2. buy some candy\n3. steal some candy\n4. go behind the counter\n5. items\n6. inventory")
            pos = choose(6)
        if pos == 6:
            print("You find yourself behind the counter of the pizza stand. The oven is directly in front of you.\n1. go back\n2. open the oven\n3. item\n4. inventory")
            pos = choose(4)
        if pos == 7:
            print("You are in the center of the pit area. Rows of different team pits lie in front of you (consult the pitmap below).\n1. first row\n2. second row\n3. third row\n4. fourth row\n5. fifth row\n6. enter the field\n7. leave the pits\n8. item\n9. inventory")
            print(f"{pitmap}")
            pos = choose(9)
        if pos == 8:
            print("You are in the first row of pits. You can see pits for 1257 and 1676.\n1. go back\n2. 1257 pit\n3. 1676 pit")
            pos = choose(3)
        if pos == 9:
            print("You are in the second row of pits. You can see pits for 2590 and 747.\n1. go back\n2. 2590 pit\n3. 747 pit")
            pos = choose(3)
        if pos == 10:
            print("You are in the third row of pits. You can see pits for 1923 and 3637.\n1. go back\n2. 1923 pit\n3. 3637 pit")
            pos = choose(3)
        if pos == 11:
            print("You are in the fourth row of pits. You can see pits for 303 and 25.\n1. go back\n2. 303 pit\n3. 25 pit")
            pos = choose(3)
        if pos == 13:
            print("You are standing on the edge of the field.")
            positem(13)
            print("1. go back\n2. go on the field\n3. go do the judges station\n4. item\n5. inventory")
            if inventory['gear rope sign']['qty'] == 0:
                print("6. take sign")
                pos = choose(6)
            else:
                pos = choose(5)
        if pos == 99:
            print("You stand in the final corridor.\n1. go forth")
            pos = choose(1)
        if pos == 1257:
            print("You are standing in the 1257 pit. You remember struggling to put together the pit structure the day before.\n1. leave\n2. rummage for parts\n3. look in the toolbox\n4. take a nap\n5. take a pin\n6. item\n7. inventory")
            pos = choose(7)
        if pos == 1676:
            print("You are standing in the 1676 pit. You can see a monitor displaying various footage of the team, and a basket of first aid kits.\n1. leave\n2. take a first aid kit\n3. take a pin\n4. look at the monitor\n5. item\n6. inventory")
            pos = choose(6)
        if pos == 2590:
            if nemesisbot == False:
                print("You are standing in the 1590 pit. Their robot lies, disabled, in the middle of the pit")
                positem(2590)
                print("1. leave\n2. take a pin\n3. item\n4. inventory")
                if inventory['driver station']['qty'] == 0:
                    print("5. take the driver station")
                    pos = choose(5)
                else:
                    pos = choose(4)
            else:
                event()
        if pos == 1923:
            print("You are standing in the 1923 pit. Their robot is on a cart in the center of the pit. It seems to be on")
            positem(1923)
            print("\n1. go back\n2. look at the robot\n3. grab a pin\n4. item\n5. inventory")
            if inventory['toolbox key']['qty'] == 0:
                print("6. take key")
                pos = choose(6)
            else:
                pos = choose(5)
        if pos == 303:
            print("You are standing in the 303 pit. A pachinko machine next to it, which seems to dispense various prizes.\n1. go back\n2. play the pachinko machine\n3. item\n4. inventory")
            pos = choose(4)



def options(opt):
    global pos
    global name
    global immorality
    global scout
    if pos == 0:
        if opt == 1:
            print("\nYou exit the bleachers")
            return 1
        if opt == 2 and inventory['safety glasses']['qty'] == 0:
            print("You rummage through your bag, and find your trusty safety glasses")
            inventory['safety glasses']['qty'] += 1
            return "h"
        if opt == 2 and inventory['safety glasses']['qty'] != 0:
            print("You rummage through your bag, but find nothing useful")
            return "h"
        if opt == 3 and inventory['scouting sheets']['qty'] == 0:
            print("You start to watch the match, but realize that you are out of scouting sheets")
            return "h"
        if opt == 3 and inventory['scouting sheets']['qty'] != 0:
            print("You pull out a scouting sheet, and begin to watch the match")
            frcgame()
            return "h"
        if opt == 4:
            ituse()
            return "h"
        if opt == 5:
            invcheck()
            return "h"
    if pos == 1:
        if opt == 1:
            print("\nYou enter the bleachers")
            return 0
        if opt == 2:
            print("\nYou walk over to the bathrooms")
            return 4
        if opt == 3:
            print("\nYou head south")
            return 2
        if opt == 4:
            ituse()
            return "h"
        if opt == 5:
            invcheck()
            return "h"
    if pos == 2:
        if opt == 1:
            print("\nYou walk down the stairs")
            return 3
        if opt == 2:
            print("\nYou head north")
            return 1
        if opt == 3:
            print("\nYou head over to the pizza stand")
            return 5
        if opt == 4 and inventory['jug of water']['qty'] == 0:
            print("You see a gallon jug of water that someone left on the stand.\nIt is covered in sharpie drawings, and reminds you of someone you haven't seen in a while")
            inventory['jug of water']['qty'] += 1
            return "h"
        if opt == 4 and inventory['jug of water']['qty'] != 0:
            print("You see a few dispensers of various condiments, but nothing useful")
            return "h"
        if opt == 5:
            ituse()
            return "h"
        if opt == 6:
            invcheck()
            return "h"
    if pos == 3:
        if opt == 1:
            print("\nYou walk up the stairs")
            return 2
        if opt == 2 and inventory['safety glasses']['equ'] == False:
            print("\nYou forgot your safety glasses! What a grave mistake!")
            death(1)
        if opt == 2 and inventory['safety glasses']['equ'] == True:
            print("\nYou walk into the pit area")
            return 7
        if opt == 3 and inventory['driver pin']['qty'] == 0:
            print("\nYou spot a drivers pin on the counter of the stand. Someone must have forgotten it")
            inventory['driver pin']['qty'] += 1
            return "h"
        if opt == 5:
            ituse()
            return "h"
        if opt == 6:
            invcheck()
            return "h"
    if pos == 4:
        if opt == 1:
            print("\nYou give up, and walk away from the bathroom")
            return 1
        if opt == 2:
            print("\nYou decide to wait a bit")
            time.sleep(5)
            return "h"
        if opt == 3 and finalopen == False:
            print("\nYou push and pull with all your might, but the door will not budge")
            return "h"
        if opt == 3 and finalopen == True:
            print("\nYou stride through the door, and off into the unknown")
            return 99
        if opt == 4:
            ituse()
            return "h"
        if opt == 5:
            invcheck()
    if pos == 5:
        if opt == 1:
            print("\nYou leave the stand and its wretched pizza behind")
            return 2
        if opt == 2:
            print("\nYou take a bag of M&Ms, and leave 2$ on the register")
            inventory['candy']['qty']+=1
            inventory['money']['qty']-=2
            return "h"
        if opt == 3:
            stl = input("\nAre you sure you want to do this? It seems pretty immoral. (Y/N)")
            while True:
                    if stl == 'y' or stl == 'Y':
                        print("\nYou take a bag of M&Ms from the rack. You feel a little bad, but at least you got your candy")
                        inventory['candy']['qty']+=1
                        immorality+=1
                        return "h"
                    elif stl == 'n' or stl == 'N':
                        print("\nYou decide to leave the candy where it is")
                        return "h"
                    else:
                        stl = input("not a command, try again: ")
        if opt == 4:
            print("\nYou climb over the stand.")
            return 6
        if opt == 5:
            ituse()
            return "h"
        if opt == 6:
            invcheck()
            return "h"
    if pos == 6:
        if opt == 1:
            print("\nYou jump back over the counter.")
            return 5
        if opt == 2 and inventory['scouting sheets']['qty'] == 0:
            print("\nYou open the oven, and find a stack of Daniel's scouting sheets.\nIt looks like someone was trying to burn them, but left before they could.")
            inventory['scouting sheets']['qty'] += 10
            return "h"
        if opt == 2 and inventory['scouting sheets']['qty'] != 0:
            print("\nYou open the oven and peer in. It seems to be perfectly functional.")
            return "h"
        if opt == 3:
            ituse()
            return "h"
        if opt == 4:
            invcheck()
            return "h"
    if pos == 7:
        if opt == 1:
            print("\nYou head into the first row of pits")
            return 8
        if opt == 2:
            print("\nYou head into the second row of pits")
            return 9
        if opt == 3:
            print("\nYou head into the third row of pits")
            return 10
        if opt == 4:
            print("\nYou head into the fourth row of pits")
            return 11
        if opt == 5:
            print("\nYou head into the fifth row of pits")
            return 12
        if opt == 6:
            print("\nYou head onto the field")
            return 13
        if opt == 7:
            print("\nYou leave the pit area")
            return 3
        if opt == 8:
            ituse()
            return "h"
        if opt == 9:
            invcheck()
            return "h"
    if pos == 8:
        if opt == 1:
            print("\nYou return to the main pit area")
            return 7
        if opt == 2:
            print("\nYou head over to the 1257 pit")
            return 1257
        if opt == 3:
            print("\nYou head over to the 1676 pit")
            return 1676
    if pos == 9:
        if opt == 1:
            print("\nYou return to the main pit area")
            return 7
        if opt == 2:
            print("\nYou head over to the 2590 pit")
            return 2590
        if opt == 3:
            print("\nYou head over to the 747 pit")
            return 747
    if pos == 10:
        if opt == 1:
            print("\nYou return to the main pit area")
            return 7
        if opt == 2:
            print("\nYou head over to the 1923 pit")
            return 1923
        if opt == 3:
            print("\nYou head over to the 3637 pit")
            return 3637
    if pos == 11:
        if opt == 1:
            print("\nYou return to the main pit area")
            return 7
        if opt == 2:
            print("\nYou head over to the 303 pit")
            return 303
        if opt == 3:
            print("\nYou head over to the 25 pit")
            return 25
    if pos == 13:
        if opt == 1:
            print("\nYou return to the main pit area")
            return 7
        if opt == 6 and inventory['gear rope sign']['qty'] == 0:
            print("\nYou grab the gear rope sign")
            inventory['gear rope sign']['qty'] += 1
            return "h"
    if pos == 1257:
        if opt == 1:
            print("\nYou leave the pit")
            return 8
        if opt == 2:
            print("\nYou look around for the bin of spare parts, but can't seem to find it. Someone must have forgotten it.")
            return "h"
        if opt == 3 and inventory['toolbox key']['qty'] == 0:
            print("\nThe toolbox is locked")
            return "h"
        if opt == 3 and inventory['toolbox key']['qty'] != 0 and inventory['hammer']['qty'] == 0:
            print('\nYou slide your key into the toolbox keyhole and it opens.\nYou find a hammer with "Erika" written on the side, and a broken xbox controller beside it')
            inventory['hammer']['qty'] += 1
            return "h"
        if opt == 3 and inventory['hammer']['qty'] != 0:
            print("\nYou open up the toolbox, but only find a broken xbox controller")
            return "h"
        if opt == 4:
            print("\nYou lie down on a bench towards the back of the pit and take a short nap")
            time.sleep(3)
            print("You feel a lot like a certain member of build team")
            return "h"
        if opt == 5:
            pinget(1257)
            return "h"
        if opt == 6:
            ituse()
            return "h"
        if opt == 7:
            invcheck()
            return "h"
    if pos == 1676:
        if opt == 1:
            print("\nYou leave the pit")
            return 8
        if opt == 2 and inventory['first aid']['qty'] == 0:
            print("\nYou take a first aid kit from the basket")
            inventory['first aid']['qty'] += 1
            return "h"
        if opt == 2 and inventory['first aid']['qty'] != 0:
            print("\nDo you really need another first aid kit?")
            return "h"
        if opt == 3:
            pinget(1676)
            return "h"
        if opt == 4 and inventory['camera']['qty'] == 0:
            print("\nYou begin to watch the video on 1676, but notice something behind the monitor.\nLooking closer, you can see that it is Justin's camera. How did it get there?")
            inventory['camera']['qty'] += 1
            return "h"
        if opt == 4 and inventory['camera']['qty'] != 0:
            print("\nYou watch the video, and note how well it's edited")
            return "h"
        if opt == 5:
            ituse()
            return "h"
        if opt == 6:
            invcheck()
            return "h"
    if pos == 2590:
        if opt == 1:
            print("\nYou leave the pit")
            return 9
        if opt == 2:
            pinget(2590)
            return "h"
        if opt == 3:
            ituse()
            return "h"
        if opt == 4:
            invcheck()
            return "h"
        if opt == 5 and inventory['driver station']['qty'] == 0:
            inventory['driver station']['qty'] += 1
            return "h"
    if pos == 1923:
        global insane
        if opt == 1:
            print("\nYou leave the pit")
            return 10
        if opt == 2 and insane == False:
            print("You peer into the robot and notice a crescent wrench in the center of the robot. Only an insane person would reach for it, however.")
            return "h"
        if opt == 2 and insane == True and inventory['wrench']['qty'] == 0:
            print("You peer into the robot and notice a crescent wrench in the center of the robot.\nYour insanity causing a complete disregard for safety, you reach in and grab the wrench.\nLuckily, you don't lose your hand.")
            inventory['wrench']['qty'] += 1
            return "h"
        if opt == 2 and inventory['wrench']['qty'] != 0:
            print("You peer into the robot, and note 1923's fine engineering.")
            return "h"
        if opt == 3:
            pinget(1923)
            return "h"
        if opt == 4:
            ituse()
            return "h"
        if opt == 5:
            invcheck()
            return "h"
        if opt == 6 and inventory['toolbox key']['qty'] == 0:
            print("\nYou grab the toolbox key")
            inventory['toolbox key']['qty'] += 1
            return "h"
    if pos == 303:
        if opt == 1:
            print("\nYou leave the pit")
            return 11
        if opt == 2:
            prize = pachinko()
            print("You grab a miniature gear from the side of the machine and drop it in")
            if prize == 1 and inventory['tape measure']['qty'] == 0:
                print("A miniature tape measure with a 303 logo falls out.")
                inventory['tape measure']['qty'] += 1
                return "h"
            if prize == 1 and inventory['tape measure']['qty'] != 0:
                print("A miniture tape measure with a 303 logo falls out, however, you don't need another one.")
                return "h"
            if prize == 2 and inventory['blueprints']['qty'] == 0:
                print("A sheet of paper detailing plans for something falls out.")
                inventory['blueprints']['qty'] += 1
                return "h"
            if prize == 2 and inventory['blueprints']['qty'] != 0:
                print("A sheet of paper detailing plans for something falls out, however, you don't need another one.")
                return "h"
            if prize == 3 and inventory['303 band']['qty'] == 0:
                print('A wristband with "303" printed on the side falls out.')
                inventory['303 band']['qty'] += 1
                return "h"
            if prize == 3 and inventory['303 band']['qty'] != 0:
                print('A wristband with "303" printed on the side falls out, however, you do not need another one.')
                return "h"
            if prize == 4 and inventory['303 pin']['qty'] == 0:
                print("An official team 303 pin falls out.")
                inventory['303 pin']['qty'] += 1
                return "h"
            if prize == 4 and inventory['303 pin']['qty'] != 0:
                print("An official team 303 pin falls out, however, you don't need another one.")
                return "h"

def pinget(x):
    pin = (f"{x} pin")
    if inventory[pin]['qty'] == 0:
        print(f"\nYou take a {pin} and put it in your pocket")
        inventory[pin]['qty'] += 1
    elif inventory[pin]['qty'] != 0:
        print("\nYou already took a pin")

def frcgame():
    global gameteams
    global winner
    global scout
    global insane
    e10 = 0
    e11 = 0
    e12 = 0
    e13 = 0
    e14 = 0
    e20 = 0
    e21 = 0
    e22 = 0
    e23 = 0
    e24 = 0
    e25 = 0
    e26 = 0
    e30 = 0
    e31 = 0
    e32 = 0
    event = random.randint(0,4)
    team = random.sample(gameteams, 1)
    steam = team[0]
    print(f"You are scouting team {steam}")
    time.sleep(.5)
    print("The match begins")
    time.sleep(1)
    if event == 0:
        print(f"{steam}'s auto code fails, and their robot remains motionless")
        e10 += 1
    elif event == 1:
        print(f"{steam}'s robot moves past the auto line and stops")
        e11 += 1
    elif event == 2:
        print(f"{steam}'s robot moves forward and drops a gear on the peg")
        e12 += 1
    elif event == 3:
        print(f"{steam}'s robot unloads their fuel into the high goal")
        e13 += 1
    elif event == 4:
        print(f"{steam}'s robot tries to shoot into the high goal, but misses")
        e14 += 1
    print("Teleop begins")
    time.sleep(1)
    for x in range(0,6):
        event = random.randint(0,6)
        if event == 0:
            print(f"{steam} heads off to the loading zone, grabs a gear, comes back, and drops it off on a peg")
            e20 += 1
        elif event == 1:
            print(f"{steam} heads off to the loading zone, grabs a gear, comes back, but it is hit by another robot and drops their gear")
            e21 += 1
        elif event == 2:
            print(f"{steam} drives into a hopper and fills their robot with fuel. They drive back and begin shooting fuel into the high boiler")
            e22 += 1
        elif event == 3:
            print(f"{steam} drives into a hopper and fills their robot with fuel. They drive back and begin shooting fuel into the high boiler, but they miss every shot")
            e23 += 1
        elif event == 4:
            print(f"{steam} goes on defense, and is moderately successful")
            e24 += 1
        elif event == 5:
            print(f"{steam} goes on defense, but don't really do much")
            e25 += 1
        elif event == 6:
            print(f"{steam}'s robot isn't moving.")
            e26 += 1
        time.sleep(1)
    print("There are 30 seconds left in the match.")
    event = random.randint(0,2)
    if event == 0:
        print(f"{steam} heads straight for their rope, and climb quickly")
        e30 += 1
    elif event == 1:
        print(f"{steam} heads straight for their rope, but their climber fails to attach to the rope")
        e31 += 1
    elif event == 2:
        print(f"{steam} drop off one last year, but cannot climb in time")
        e32 += 1
    time.sleep(1)
    print("The match ends, and you jot down a few notes at the bottom of the sheet")
    time.sleep(5)
    os.system('clear')
    qu = random.randint(0,4)
    if qu == 0:
        ans = int(input(f"How many times did {steam} deliver a gear? "))
        if ans == e20:
            scoutcorrect()
        else:
            scoutwrong()
    if qu == 1:
        ans = input(f"Did {steam} deliver a gear in auto? (Y/N) ")
        if e12 == 0:
            if ans == 'N' or ans == 'n':
                scoutcorrect()
            else:
                scoutwrong()
        if e12 != 0:
            if ans == 'Y' or ans == 'y':
                scoutcorrect()
            else:
                scoutwrong()
    if qu == 2:
        ans = int(input(f"How many times did {steam} shoot fuel into the high boiler"))
        if ans == e22:
            scoutcorrect()
        else:
            scoutwrong()
    if qu == 3:
        ans == input(f"Did {steam} climb? (Y/N) ")
        if e30 == 0:
            if ans == 'N' or ans == 'n':
                scoutcorrect()
            else:
                scoutwrong()
        if e30 != 0:
            if ans == 'Y' or ans == 'y':
                scoutcorrect()
            else:
                scoutwrong()
    if qu == 4:
        ans = int(input(f"How many times did {steam} go on defense? "))
        if ans == e24+e25:
            scoutcorrect()
        else:
            scoutwrong()

def scoutcorrect():
    global scout
    global insane
    print("You have scouted well.")
    inventory['scouting sheets']['qty']-=1
    scout+=1
    if scout == 5:
        print("\nYou have spent a countless amount of time scouting. The edges of you vision start to cloud, and a terrible power starts to come over you.\nYou embrace this power, and achieve true insanity. You can hear Daniel and Jeff laughing in the distance")
        insane = True

def scoutwrong():
    print("You have failed to scout properly. You can feel Daniel's displeasure at your failure")

def pachinko():
    res = random.randint(1,16)
    if res == 1:
        return 1
    if res == 2:
        return 2
    if res == 3 or res == 4 or res == 5 or res == 6 or res == 7 or res == 8 or res == 9 or res == 10:
        return 3
    if res == 11 or res == 12 or res == 13 or res == 14 or res == 15 or res == 16:
        return 4


def ituse():
    global inventory
    global spirit_shirt
    for item in inventory.keys():
        if inventory[item]['qty']>0:
            print(f"- {item}")
    print("- cancel")
    use = input("What do you use? ")
    if use in inventory.keys() and inventory[use]['qty'] != 0:
        if use == 'safety glasses' and inventory['safety glasses']['equ'] == False:
            print("You put on your safety glasses, and feel the glorious power of eye protection")
            inventory['safety glasses']['equ'] = True
            return "h"
        if use == 'safety glasses' and inventory['safety glasses']['equ'] == True:
            print("You take off your safety glasses")
            inventory['safety glasses']['equ'] = False
            return "h"
        if use == '303 band' and inventory['303 band']['equ'] == False:
            print("You put on your 303 band")
            inventory['303 band']['equ'] = True
            return "h"
        if use == '303 band' and inventory['303 band']['equ'] == True:
            print("You take off your 303 band")
            inventory['303 band']['equ'] = False
            return "h"
        if use == '1257 shirt' and inventory['1257 shirt']['equ'] == True:
            print("Why would you want to take off your 1257 shirt? Have you no team spirit?")
            off = input("take off the shirt anyway? (Y/N) ")
            while True:
                if off == 'Y' or off == 'y':
                    print("You take your shirt off. Are you proud of yourself?")
                    spirit_shirt = False
                    inventory['1257 shirt']['equ'] = False
                    return "h"
                elif off == 'N' or off == 'n':
                    print("You decide to leave your shirt on")
                    return "h"
                else:
                    off = input("Not a command, try again: ")
        if use == '1257 shirt' and inventory['1257 shirt']['equ'] == False:
            print("You put your team shirt back on. Shame you took it off in the first place")
            inventory['1257 shirt']['equ'] = True
            return "h"
        if pos == 4 and use == 'stop sign hammer':
            global finalopen
            print("You can feel the power of a million CIM motors as you bring Matt's hammer down in a triumphant arc over your head.\nThe door is completely and utterly decimated.")
            finalopen = True
            return "h"
        if use == 'cancel':
            return "h"
        else:
            print(f"""You can hear Priscilla's words echoing in your head:
                "{name}, why would you ever use that here" """)
            return "h"
    else:
        print("Not an item")
        return "h"

def positem(x):
    if x == 13 and inventory['gear rope sign']['qty'] == 0:
        print("You see the gear rope sign on the side of the field. Alan must have left it there.")
    if x == 2590 and inventory['driver station']['qty'] == 0:
        print("There is a driver station computer plugged in to the robot.")
    if x == 1923 and inventory['toolbox key']['qty'] == 0:
        print("There a key lying on the table, presumably for a toolbox")

def event():
    global pos
    retry = True
    while retry == True:
        global position
        retry = False
        if pos == 2590:
            print("As you walk into the pit, you see 2590's robot whir to life, the green glow of their vision looking oddly menacing\n1. leave\n2. step forwards\n3. item\n4. inventory")
            echoice = int(input("What do you do?: "))
            if echoice == 1:
                print("You back out of the pit, and the robot seems to turn off")
                pos = 9
            if echoice == 2:
                print("You take a single step forward. The robot's shooter turns on, and launches fuel at you with incredible speed")
                death(2)
            if echoice == 4:
                invcheck()
            if echoice == 3:
                for item in inventory.keys():
                    if inventory[item]['qty']>0:
                        print(f"- {item}")
                print("- cancel")
                use = input("What do you use?: ")
                if use in inventory.keys() and inventory[use]['qty'] != 0:
                    if use == 'gear rope sign':
                        print("You take a step forward. The robot prepares to fire fuel at you, but you bring up your gear rope sign with expert reflexes.\n1. run\n2. item")
                        rchoice = int(input("What do you do?: "))
                        if rchoice == 1:
                            print("You back out of the pit, and the robot seems to turn off")
                            pos = 9
                        if rchoice == 2:
                            for item in inventory.keys():
                                if inventory[item]['qty']>0:
                                    print(f"- {item}")
                            print("- cancel")
                            use = input("What do you use?: ")
                        if use in inventory.keys() and inventory[use]['qty'] != 0:
                            if use == 'hammer' or use == 'stop sign hammer':
                                print("You take yet another step forward, and bring your hammer down in a triumphant arc right onto 2590's vision")
                                global nemesisbot
                                nemesisbot = False
                            elif use == 'cancel':
                                return "h"
                            else:
                                print(f"Before you have a chance to use the {use}, the robot begins firing upon you")
                                death(2)

                    elif use == 'cancel':
                        return "h"
                    else:
                        print(f"Before you have a chance to use the {use}, the robot begins firing upon you")
                        death(2)
                else:
                    print("Not an item")
                    return "h"


def loop():
    while True:
        e = input()

def death(x):
    if x == 1:
        print('\nYou see a small figure emerging from the shadows out of the corner of your eye.')
        time.sleep(1)
        print("\nYou suddenly realize who it is, but it is too late, you are already dead.")
        time.sleep(1)
        print("\nAs everything fades to black, you can hear Priscilla standing over you, laughing")
        time.sleep(.5)
        x = random.randint(10,20)
        for y in range(x):
            print("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
            time.sleep(.2)
        time.sleep(1.5)
        print("HA")
        time.sleep(1.5)
        print("\n\nYOU HAVE DIED")
        loop()
    if x == 2:
        print("\nThe fuel rips through your chest. You fall over, dead.\n\nYOU HAVE DIED")
        loop()

def awards():
    global spiritwin
    global spirit_shirt
    if spirit_shirt == True:
        spiritwin = True
        print('"The winner of the Team Spirit Award is..."')
        time.sleep(.5)
        print('"Team 1257 Parallel Universe!"')


name = input("Hey, welcome to this steaming pile of garbage I call a game.\nWho am I? That's not important.\nWhat is important, however, is your name.\n")
print(f"Well {name}, it's time to get up.")
time.sleep(1)
print("\n\n\nYou wake up in the stands of Stabler Arena during DCMP.\nHowever, nobody seems to be around, and the place seems to be abandoned.")
location()


