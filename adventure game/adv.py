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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(currentRoom = room["outside"])


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

direction = ""

while(direction != "q"):
    print(player.currentRoom.name)
    print(player.currentRoom.description)

    direction = input("""Where do you want to go bitch? 
    w - west, 
    s - south, 
    n - north
    e - east
    Don't want to play my stupid game? Press q!""")

    if (player.currentRoom == room["outside"] and direction == "n"):
        player.currentRoom = room["outside"].n_to
    elif(player.currentRoom == room['foyer'] and direction == "s"):
        player.currentRoom = room["foyer"].s_to
    elif(player.currentRoom == room['foyer'] and direction == "n"):
        player.currentRoom = room["foyer"].n_to
    elif(player.currentRoom == room['foyer'] and direction == "e"):
        player.currentRoom = room["foyer"].e_to
    elif(player.currentRoom == room['overlook'] and direction == "s"):
        player.currentRoom = room["overlook"].s_to
    elif(player.currentRoom == room['narrow'] and direction == "w"):
        player.currentRoom = room["narow"].w_to
    elif(player.currentRoom == room['narrow'] and direction == "n"):
        player.currentRoom = room["narow"].n_to
    elif(player.currentRoom == room['treasure'] and direction == "s"):
        player.currentRoom = room["treasure"].s_to
        print("Hooray, you won and found gold!")
        sys.exit()
    else:
        print("Not here!")








