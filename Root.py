import random


count = 0
while (count < 10000):
    leftlist = ["A large demonic idol with ruby eyes sits in an alcove here. The idol seems to be chanting something "
                "very quietly. DM Notes:She will cast reincarnate on any dead player", "This room is empty", "A stone sarcophagus sits in the south side of the room, and someone has scrawled 'Death comes on silent wings' on the east wall. A Half-Red dragon stands behind it ready to attack if anyone dares attempt to open it", "The floor is covered in perfect hexagonal tiles, and a metallic odor fills the north-east corner of the room. *If anyone investigates the room and gets above a DC15 they will discover a loose tile which reveals a Lodestone Marauder if pulled up*", "Several pieces of blood-soaked clothing are scattered throughout the room and a Drider looks up over with a bloody face and charges in", "Several shattered weapons are scattered throughout the room and amidst the mess is an immaculate  +1/+1 rapier", "A rotting odor fills the room. An orc warchief is reading a book and looking at the north wall of this room. *His passive perception is 14* and if anyone disrupts him he will become aggressive yelling about how they interrupted his readings. Someone has scrawled 'Lightning comes before thunder' on the north wall. *If anyone tells him that's what it says on the wall he will apologize and become relaxed*", "A group of demonic faces have been carved into the south wall. Stalagmites and stalactites are throughout this room. *If the party tries to leave or if they roll a DC15 investigation they will discover a rover that is trying to eat them.* ", "A statue of a cleric resurrecting an entire party sits surrounded by a pool of a vibrant green liquid", "This room is empty", "This room is empty", "This room is empty", "This room is empty", "This room is empty", "This room is empty", "This room is empty", "This room is empty", "This room is empty", "This room is empty", "This room is empty", "This room is empty", "This room is empty",
                "a room filled with water that doesnt spill over the door you see 1d6 sunken chests at the bottom of the "
                "room. You notice once you're in the room that the water seems breathable. GM notes: The chests are mimics"]
    left_list = random.choice(leftlist)
    rightlist = ["Peters being stinky", "a fat dude in a sundress"]
    right_list = random.choice(rightlist)
    colorlist = ["red", "black", "mirror", "brown", "amber", "verdant", "teal", "violet", "crimson", "black",
                  "silver", "gold", "green", "yellow", "white", "blue"]
    color_list = random.choice(colorlist)
    movementlist = ["20", "25", "30", "35", "40", "45", "50", "55", "60", "70", "80", "90", "100"]
    movement_list = random.choice(movementlist)
    count_list= count
    print("A crystal skull on a", color_list , "Podium speaks to you and asks in a deep gravely voice, "
            "'You have traveled through", count_list, "doors. What path do you wish to choose' "
                                                      "(Left or Right) or do you wish to leave")


    side = input()

    if side == "left" or side == "Left":

        print("You've chosen the left hallway. You move", movement_list,"feet down the hallway until you see a",
          color_list , "door at the end"),
        print("Behind this door you see:", left_list), "\n"
        count+=1

    elif side == "right" or side == "Right":

        print("You've chosen the right hallway. You move", movement_list,"feet down the hallway until you see a",
          color_list , "door at the end"),
        print("Behind this door you see:", right_list)
        count+=1


    elif side == "leave":
        print("You awake from what feels like a dream in a chair around a poker table with gashes from sharp objects and "
          "rings from spilled drinks. An old lady looks at you and congratulates your on your finished trial.")
        break
    else:
         print("Sorry i dont understand")

print("Thank you and come again")