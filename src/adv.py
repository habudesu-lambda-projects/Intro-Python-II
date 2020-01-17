from room import Room
from player import Player
from item import Item
import sys
import random

# Make Items
items = {
    'coins': Item("coins", "There are some copper coins on the ground.", random.randint(0,10)),
    'sword': Item("sword", "There is a beat up sword with no hilt against the wall.", 1)
}


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     []),

    'foyer':    Room("Foyer",
                    """Dim light filters in from the south. Dusty passages run north and east.""",
                    [items["sword"]]),

    'overlook': Room("Grand Overlook",
                    """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                    []),

    'narrow':   Room("Narrow Passage",
                    """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
                    []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
                    [items["coins"]]),
}


# Link rooms together

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(input("What's your name? "), "outside", [])
print(f"Hi {player.name}!\nTo move, type which direction you want to move (north, south, east, west).\nTo pick up an item, type 'get (item name)'.\nTo drop an item type 'drop (item name)'.\nTo quit the game, type 'q'.\nHave Fun!")

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

while player:
    print(f"Current Room: {room[player.room_key].name}")
    print(room[player.room_key].description)
    for item in room[player.room_key].items:
        print(item.description)
    action = input("What do you want to do? ").split(" ")
    if len(action) == 1:
        if action[0].lower() == "north":
            try:
                player.room_key = room[player.room_key].n_to
            except AttributeError:
                print("Can't go that way. Try a different direction.")
        elif action[0].lower() == "south":
            try:
                player.room_key = room[player.room_key].s_to
            except AttributeError:
                print("Can't go that way. Try a different direction.")
        elif action[0].lower() == "east":
            try:
                player.room_key = room[player.room_key].e_to
            except AttributeError:
                print("Can't go that way. Try a different direction.")
        elif action[0].lower() == "west":
            try:
                player.room_key = room[player.room_key].w_to
            except AttributeError:
                print("Can't go that way. Try a different direction.")
        elif action[0].lower() == "q":
            print("Thanks for playing!")
            sys.exit()
        elif action[0].lower() == "i" or "inventory":
            print(f"Player Inventory: {[item.name.title() for item in player.items]}")
        else:
            print("Not a valid action.\nTo move, type which direction you want to move (north, south, east, west).\nTo pick up an item, type 'get (item name)'.\nTo drop an item type 'drop (item name)'.\nTo quit the game, type 'q'.")
    elif len(action) == 2:
        act = action[0]
        item_name = action[1]
        if act.lower() == "get":
            if items[item_name.lower()] in room[player.room_key].items:
                player.get_item(items[item_name.lower()])
                room[player.room_key].item_taken(items[item_name.lower()])
            else:
                print(f"No {item_name} in this room.")
        elif act.lower() == "drop":
            player.drop_item(items[item_name.lower()])
            room[player.room_key].item_dropped(items[item_name.lower()])
        else:
            print("Not a valid action.\nTo move, type which direction you want to move (north, south, east, west).\nTo pick up an item, type 'get (item name)'.\nTo drop an item type 'drop (item name)'.\nTo quit the game, type 'q'.")
    else:
        print("Not a valid action.\nTo move, type which direction you want to move (north, south, east, west).\nTo pick up an item, type 'get (item name)'.\nTo drop an item type 'drop (item name)'.\nTo quit the game, type 'q'.")
        

        