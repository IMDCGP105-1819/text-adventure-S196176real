print("You are Captain Morgan and someone has stolen your treasure overnight you have narrowed down the search to Twig Island nearby. You have your crew set sail to visit the nearby island town Vert. Type Commands to see the available commands")

#this is where the items picked up will be stored in memory
items=[]

place=1

town=2

forest=3

mine=4

lair=5
#this is an empty room so no commands can be  used when the game is complete
fin=6

game=0

on=90

game=on

place=town


while game==on:

#while loop is used for each places in the game so you can go back and forth between areas
    while place==town:
#input allows the user to write
        direction=input("What would you like to do?\n")
#writing west in the input triggers the inkeeper scene
        if direction=="west":
            if "iron ore" and "wood" and "50 gold" in items:
                print ("'Ah look who it is!'.Thank you kindly, you will find your thief hiding in a tree trunk in the Jungle it is a kobold mage be careful lad. Oh and here take this gem we call it Lit we use it to dispel magic illusions such as that mist in the Jungle.")
                #these items are removed from the item list and will no longer show up until added again
                items.remove ("saw")
                items.remove ("50 gold")
                items.remove ("iron ore")
                items.remove ("wood")
                #this item is added to the items list
                items.append ("Lit")
            #if the criteria is not met for the above statement then trigger this
            else:
              print ("You visit the local Inn of Vert, many different kinds of hunting trophies adorn the Inn, the barkeep is a tall, hairy man who smiles as you enter the door.\n You tell him that you need information about local criminals. He laughs and says  'Let me guess someone stole your treasure? You're not the first pirate to ask old Barry.'.You nod 'I'll help ye out but before i tell you who stole your treasure, help me acquire some treasure of my own.\n '50 gold, firewood and some iron will do just fine")

#writing north triggers this scene
        elif direction=="north":
            print ("You head east. There isn't much else of note here in Vert aside from the Huntmaster inn, you decide to head back to the center of town")
#writing east triggers this scene
        elif direction=="east":
            print ("You take a stroll along the beach up north. Nothing eventful occurs.")

        elif direction=="south":
            print ("You tread south in to the forest")
            place=forest
#writing commands triggers this text to appear
        elif direction=="commands":
            print ("type the commands north, south, east, and west in order to navigate,type the command use followed by the item name to use an item, type the command inventory to look at the items in your posession, type the command look to look around you, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")
#writing inventory prints the current strings stored in items to the player
        elif direction=="inventory":
            print (items)
#writing look will print this statement into the console
        elif direction=="look":
            print ("You're located in the seaside town known as Vert, here you see the Huntmaster Inn to the west, the Beach to the north, bugger all to the east, and the wild Jungle south")
#writing use will print this statement
        elif "use" in direction:
            print ("You have nothing to use")
#writing use will print this statement
        elif "search" in direction:
            print ("Nothing to search here")
#else breaks the elif statements
        else:
            print ("Invalid command. Type commands for a list of available commands")

    while place==forest:

        direction=input("What would you like to do?\n")

        if direction=="west":
            print ("You head into the mine")
            place=mine

        elif direction=="south":
            print ("You decide to head south and check out that person by an unusual tree you saw.")

        elif direction=="east":
            if "Lit" in items:
                print ("The mist clears revealing a tree trunk with a door jammed in it")
                place=lair
            else:
                print ("A thick mist blocks your path")

        elif direction=="north":
            print ("You head back to Vert")
            place=town

        elif direction=="look":
            print ("You are at the center of the mighty Jungle, many tall trees crowd around you, you can defintiely get Barry the barkeep some firewood here, but you would need an axe first.  To your west lies a dank and dark cavern, to your south you see a tent with a thatch roof surrounded by trees, to your east a thick mist blocks your vision but you can make out some sort of out of place tree, and to the north the town of Vert")
#using the pickaxe item if the pickaxe string is stored in items triggers this scene
        elif "use" in direction:
            if "pickaxe" in direction:
                if "iron ore" in items:
                    if "person" in directions:
                        print ("Ah there ye are. Thank you very much!")
                        items.append ("saw")
                        items.remove ("pickaxe")
#using the saw alongside tree and use command results in this scene
            if "saw" in direction:
                if "saw" in items:
                    if "tree" in direction:
                        print ("you use the saw to cut some wood off of a nearby tree for Barry")
                        items.append ("wood")
                else:
                   print ("you can't use that")


        elif direction=="inventory":
            print (items)

        elif "search" in direction:
            if direction== "search person":
                print ("Before you even touch the tent a skinny figure emerges from the tent, he appears to be a miner and is carrying a saw ready to strike .  'You have some nerve scaring me like that', you ask if you can borrow the saw to get some firewood. \n 'sure i don't see why not but get me a pickaxe first. Be careful of those creatures in the cave if you go down there'.")
            else:
                print ("You can't search for that")

        elif direction=="commands":
            print ("type the commands north, south, east, and west in order to navigate,type the command use followed by the item name to use an item, type the command inventory to look at the items in your posession, type the command look to look around you, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")


    while place==mine:

        direction=input("What would you like to do?\n")

        if direction=="west":
            print ("As you head west towards the red spheres a bloodcurdling scream stops you in your tracks, you decide its best to head back to the center of the mineshaft")

        elif direction=="east":
            print ("You head back to the forest")
            place=forest

        elif direction=="south":
            print ("More than enough Iron for Barry, however you don't have a way to mine it")

        elif direction=="north":
            print ("You head north to find the mangled corpse of the once pickaxe thief, you have a slight suspicion as to how he died a gruesome death.  You see a pickaxe handle poking out underneath what remains of him alongside a pouch of gold coins")

        elif direction=="look":
            print ("You find yourself in the center of a large mineshaft.  To the east lies the exit back to the Jungle, to your north a foul stench assaults your nose, to your south lies a small vein of Iron, and to your west lies a hundred reflective blinking red spheres.")
#searching the word body will trigger this scene
        elif "search" in direction:
            if "body" in direction:
                if "pickaxe" not in items:
                    print ("You take the pickaxe and the bag which contained 50 Gold")
                    items.append ("pickaxe")
                    items.append ("50 gold")
            else:
                print ("You cannot search that")

        elif "use" in direction:
            if "pickaxe" in direction:
                if "pickaxe" in items:
                    if "iron" in direction:
                        print ("You use the pickaxe to mine the iron ore")

                        items.append ("iron ore")
#this is an error message for when the user does the command incorrectly so they know they have done something wrong
            else:
                print ("You cannot use that")

        elif direction=="inventory":
           print (items)

        elif direction=="commands":
            print ("type the commands north, south, east, and west in order to navigate,type the command use followed by the item name to use an item, type the command inventory to look at the items in your posession, type the command look to look around you, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")


    while place==lair:

        direction=input("What would you like to do?\n")

        if direction=="west":
            print ("You head back into the forest")
            place==forest
#if robe is not a string in the items then this scene triggers
        elif direction=="south":
            if "robe" not in items:
                print ("Beyond the mist lies a door shoved in to a tree trunk, as you enter you catch a glimpse of a small rat like creature wearing a black robe far too big for it. It screams 'Karza N'thul!' and tries to attack you with a magic spell!")
#the user inputs whatever text and gets a scene based on whether they wrote use lit or something else
                action=input ("What will you do?")

                if "Lit" in action:
                    print ("But as the Kobold is channeling its spell the glow from Lit distracts it long enough for you to decapitate the kobold, you decide to wear your newly acquired robe!")
                    items.append ("robe")
                    print ("You head back to the center of the lair")
                    place=lair

                else:
                    print ("The Kobold casts it's spell, your vision fades. You find yourself back in the Jungle.")
                    place=forest
#two different states for this allow for two scenes in one room haing a locked state (2) and an unlocked state (1) thus using the key changes the value to 1
        elif direction=="east":
            if "key" in items:
                print ("You head east towards the towering wooden door with a comically large lock.")
                cell=1
                locked=2
                cell=locked
                while cell==locked:
                    action=input("What would you like to do?")
                    if "key" in action:
                        cell=1
                        print ("You unlock the door to be greeted with the site of your treasure and more!. Thus ends the adventure of Captain Morgan and the kobold who stole his treasure.")
                        game=win
                        place=fin
            else:
                print ("All that stops you from getting back your treasure is this comically large lock.")

        elif direction=="north":
            if "robe" in items:
                print ("You feel a sudden rise in temperature as you make your way too the floating gold key, strangely enough the robe remains cold to the touch ")
                action=input("What will you do?")
                if "robe" in action:
                    print ("You wrap the robe to cover as much of your body as possible and make a sprint for the key. You make your way back key in hand.")
                    items.append ("key")
                else:
                    print ("Slowly your vision fades as the onslaught of heat becomes too much to bear.")
                    place=forest

            else:
                print ("Stepping into this room as you are right now would be suicide in that heat.")

        elif direction=="look":
            print ("The Kobold mage's house feels as if it is has broken off from the world. To the west the small door you came through, to the north you see a floating golden key but the very air is distorted by the heat coming from that room. A large door with a strange lock bars you entry to the east but too the south is a regular stone room.")

        elif "use" in direction:
            print ("No time for messing about when treasure is on the line")

        elif direction=="commands":
            print ("type the commands north, south, east, and west in order to navigate,type the command use followed by the item name to use an item, type the command inventory to look at the items in your posession, type the command look to look around you, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")

        elif direction=="inventory":
            print (items)

        elif "search" in direction:
            print ("Waste of time searching. Lets get back that treasure!")
#this is a while loop where the user cannot input any commands so they can close the game
while game==win:
    print ("Captain Morgan now wealthier than before sets out too retire his pirate ways. The end.")
    game=99
