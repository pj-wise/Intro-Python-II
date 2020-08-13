from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south. Before you go, have a nice picnic."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#Create Items

item = {
    'cheese': Item("cheese", "The cheese looks unspoiled and doesn't smell rotten"),
    'olives': Item("olives", "Are the olives stuffed with garlic? These are next level"),
    'bread': Item("bread", "A loaf of french break that's a little bit stale, but won't break teeth."),
    'mushrooms': Item("mushrooms", "The mushrooms are growing out of the rock walls and glowing"),
    'wine': Item("wine", "A bottle of pinot noir"),
    'cloth': Item("cloth", "Red and white gingham cloth")
}

#Add items to rooms
room['foyer'].items.append(item['wine'].name)
room['foyer'].items.append(item['bread'].name)
room['overlook'].items.append(item['cheese'].name)
room['overlook'].items.append(item['olives'].name)
room['narrow'].items.append(item['mushrooms'].name)
room['treasure'].items.append(item['cloth'].name)
# print(room['overlook'].items)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
while True:
    player_name = input("What's your name?: ")
    break

player = Player(player_name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    #print the current room name and decription
    print(f"\n{player.name} is currently at location: {player.current_room.name}. \n{player.current_room.description}\n\nItems in this room are:")
    if len(player.current_room.items) > 0:
        for item in player.current_room.items:
            print(f'{item}')
    else:
        print("None")

    cmd = input(f"\nMove: 'n', 's', 'e', 'w'\nAction: 'take', 'get', or 'drop <item name>\nCheck inventory: 'i' or 'inventory' \nQuit: 'q'\n\nWhat do you want to do?: ").split(' ')
 
    #check if room exists
    #if exists, go into room
    if cmd[0] == "n":
        print(f'{cmd}')
        if player.current_room.n_to != None:
            player.current_room = player.current_room.n_to
            # print(player.current_room.name)
        else:
            print("There is no room in that direction.")
    elif cmd[0] == "s":
        if player.current_room.s_to != None:
            player.current_room = player.current_room.s_to
        else:
            print("There is no room in that direction.")
    elif cmd[0] == "e":
        if player.current_room.e_to != None:
            player.current_room = player.current_room.e_to
        else:
            print("There is no room in that direction.")
    elif cmd[0] == "w":
        if player.current_room.w_to != None:
            player.current_room = player.current_room.w_to
        else:
            print("There is no room in that direction.")
    elif cmd[0] == "take" or cmd[0] == "get":
        player.add_item(cmd[1])
    elif cmd[0] == "drop":
        player.drop_item(cmd[1])
    elif cmd[0] == "i" or cmd[0] == "inventory":
        if len(player.items) > 0:
            print("These are the items in your inventory: ")
            for item in player.items:
                print(item)
        else:
            print("You have no items in your inventory.\n")
    elif cmd[0] == "q":
        print("See you soon, adventurer!")
        break
    else:
        print(f"Invalid command. \nInput a direction to move ('n', 's', 'e', 'w'), \nan action('get', 'take' or 'drop' <item name>, \nor input 'q' to quit.")
    
    #if it doesn't exist, throw err

    #exit game if "q" is pressed