#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Rooms import Room
from TextUI import TextUI
from bookshelf  import bookshelf
from Items import Bag



"""
"In the summer of 1992, Hugh and Olivia Crain and their five
children—Steven, Shirley, Theodora (Theo), Luke, and Eleanor
(Nell)—move into Hill House to renovate the mansion in order
to sell it and build their own house, designed by Olivia.
However, due to unexpected repairs, they have to stay longer,
and they begin to experience increasing paranormal phenomena,
resulting in a tragic loss and the family fleeing from the house.
Twenty-six years later, the Crain siblings and their estranged father
reunite after another tragedy strikes them, and they are forced to 
confront how their time in Hill House has affected each of them."
N'Duka, Amanda (October 17, 2017).
 
"""

class Game:

    def __init__(self):
        """
        Initialises the game.
        """
        self.create_rooms()
        self.current_room = self.myroom
        self.textUI = TextUI()

        self.bookshelf = bookshelf()
        self.bookshelf.setup_bookshelf()

    def create_rooms(self):
        """
            Sets up all room assets.
        :return: None
        """
        self.myroom= Room("You are in your room","open")
        self.corridor = Room("you are in the corridor","open")
        self.basement = Room("you are in the basement, look after your self","open")
        self.lobby= Room("finally you get into the lobby","open")
        self.woods = Room("you entry in the dark woods, there is an item in this room","open")
        self.lake = Room("Do not swim in the lake, please","open")
        self.greenhouse = Room("there are a lot of plants in here, green house","open")
        self.red_door_room = Room("you are almost done! just open the red door to scape from ghost, and BE FREE","closed")
        self.dolls_room = Room("in the playroom","open")
        self.cursed_cemetery = Room("a ghost caught you and took you into the coursed cementery, GAME OVER","open")

        self.myroom.set_exit("east", self.corridor)
        self.corridor.set_exit("west", self.myroom)
        self.corridor.set_exit("north", self.lake)
        self.corridor.set_exit("east", self.basement)
        self.basement.set_exit("west", self.corridor)
        self.lake.set_exit("south", self.corridor)
        self.lake.set_exit("west", self.greenhouse)
        self.lake.set_exit("east", self.woods)
        self.lake.set_exit("teleport", self.dolls_room)
        self.woods.set_exit("west", self.lake)
        self.woods.set_exit("east", self.lobby)
        self.lobby.set_exit("east", self.dolls_room)
        self.greenhouse.set_exit("east", self.lake)
        self.red_door_room.set_exit("west", self.dolls_room)
        self.dolls_room.set_exit("teleport", self.lake)
        self.dolls_room.set_exit("south", self.cursed_cemetery)
        self.dolls_room.set_exit("east", self.red_door_room)


    def play(self):
        """
            The main play loop.
        :return: None
        """
        self.print_welcome()
        finished = False
        while not finished:  # while (finished == False):
            command = self.textUI.get_command()  # Returns a 2-tuple
            finished = self.process_command(command)
        print("someone is looking at you... bye")

    def print_welcome(self):
        """
            Displays a welcome message.
        :return:
        """
        self.textUI.print_to_textUI("you are lost, and something is staring at you")
        self.textUI.print_to_textUI("dont look behind your back")
        self.textUI.print_to_textUI("")
        self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}')

    def show_command_words(self):
        """
            Show a list of available commands.
        :return: None
        """
        return ['help', 'go', 'quit', 'bag', 'obtain', 'opendoor']

    def process_command(self, command):
        """
            Process a command from the TextUI.
        :param command: a 2-tuple of the form (command_word, second_word)
        :return: True if the game has been quit, False otherwise
        """
        command_word, second_word = command
        if command_word != None:
            command_word = command_word.upper()

        want_to_quit = False
        if command_word == "HELP":
            self.print_help()
        elif command_word == "GO":
            self.do_go_command(second_word)
        elif command_word == "QUIT":
            want_to_quit = True
        elif command_word == "BAG":
            self.SeeItems()
        elif command_word == "OBTAIN":
            self.keys()
            #print("take item")
        elif command_word == "OPENDOOR":
            self.opendoor()
        else:
            # Unknown command...
            self.textUI.print_to_textUI("where???? try to write it again")

        return want_to_quit

    def SeeItems(self):
        for item in self.bookshelf.get_item_list():
            print(item.name)

    def keys(self):

        inventory = self.bookshelf.get_item_list()
        key = Bag("Red door key", "old key")

        if self.current_room == self.masterroom:
            inventory.append(key)
            return print('you have got the red door room key')

    def opendoor(self,):
        """
            Performs the USE command.
        :param second_word: the item wich will be used
        :return: None
        """
        next_room = self.current_room.get_exit("east")
        if [item.name for item in self.bookshelf.get_item_list()].count("red door key")==1 and next_room.door_position() == "closed":
            self.red_door_room.doorposition = "open"

            self.textUI.print_to_textUI("The door is now open")




    def print_help(self):
        """
            Display some useful help text.
        :return: None
        """
        self.textUI.print_to_textUI("you are lost, and something is staring at you")
        self.textUI.print_to_textUI("dont look behind your back.")
        self.textUI.print_to_textUI("")
        self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}.')

    def do_go_command(self, second_word):
        """
            Performs the GO command.
        :param second_word: the direction the player wishes to travel in
        :return: None
        """
        if second_word == None:
            # Missing second word...
            self.textUI.print_to_textUI("where???? try to write it again")
            return

        next_room = self.current_room.get_exit(second_word)
        if next_room == None:
            self.textUI.print_to_textUI("There is no door!")

        elif next_room != None and next_room.door_position() == "closed":
            self.textUI.print_to_textUI("this door is closed")

        else:
            self.current_room = next_room
            self.textUI.print_to_textUI(self.current_room.get_long_description())

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()

