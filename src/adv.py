from room import Room
from player import Player
import sys

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
earlier adventurers. The only exit is to the south."""),
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

player = Player("Ken", "outside")

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
    print(room[player.room_key].name)
    print(room[player.room_key].description)
    action = input("Which direction do you want to go? Enter north, south, east, or west (q to quit): ")
    if action == "north":
        try:
            player.room_key = room[player.room_key].n_to
        except AttributeError:
            print("Can't go that way. Try a different direction.")
    if action == "south":
        try:
            player.room_key = room[player.room_key].s_to
        except AttributeError:
            print("Can't go that way. Try a different direction.")
    if action == "east":
        try:
            player.room_key = room[player.room_key].e_to
        except AttributeError:
            print("Can't go that way. Try a different direction.")
    if action == "west":
        try:
            player.room_key = room[player.room_key].w_to
        except AttributeError:
            print("Can't go that way. Try a different direction.")
    if action == "q":
        print("Thanks for playing!")
        sys.exit()