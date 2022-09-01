"""
Executive class to run the boardgame interactions and used to store the 2d list info from file
"""

from boardgame import Boardgame

class Executive:
#menu method to run interactions and take in user input
    def menu(self, list_games, __name__):
        while input != 6:
            print("1. Print all games")
            print("2. Print all games from a year")
            print("3. Print ranking range")
            print("4. People VS Dr. Gibbons")
            print("5. Print play time")
            print("6. Exit the program")
            choice = input("Select option: ")
            if choice == "1":
                Boardgame.printGames(self, list_games, __name__)

            if choice == "2":
                x = input("Select a year: ")
                Boardgame.printYear(self, list_games, x, __name__)

            if choice == '3':
                x = input("Select a ranking range, number 1: ")
                y = input('Number 2: ')
                Boardgame.rankingRange(self, list_games, x, y, __name__)

            if choice == '4':
                x = input("Select a number where the difference between the people's rating and Dr. Gibbons rating are seperated by that much or more: ")
                Boardgame.peopleGibbons(self, list_games, x, __name__)

            if choice == '5':
                x = input("Select a minimum play time: ")
                Boardgame.playTime(self, list_games, x, __name__)

            if choice == '6':
                print('Good bye!')
                break
#file input method to take store the info from file into a 2d list and pass it onto other methods and classes
    def file_name(self, __name__):
        input_file = open(__name__, 'r')
        list_games = []  # main variable to store the entire file information(each line)
        for index, game in enumerate(input_file.readlines()):
            gameLinesList = []  # variable to store the each attribute in each game
            for pieceIndex, eachLine in enumerate(game.split(" ")):
                gameLinesList.append(eachLine.rstrip('\n'))
            list_games.append(gameLinesList)
        my_boardgames = Boardgame(list_games, __name__)
        self.menu(list_games, __name__)


