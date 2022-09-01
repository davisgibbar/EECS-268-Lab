"""
Boardgame class that takes in the received info from the 2d list and
uses it for each interaction
"""
class Boardgame:
    def __init__(self, games, file_name):
        self.game = games
        self.file_name = file_name

#Prints all the games from the file
    def printGames(self, list_games, file_name):
        input_file = open(file_name, 'r')
        value = 0
        for line in input_file.readlines():
            print(f"{list_games[value][0]} ({list_games[value][1]}) [GR={list_games[value][2]}, PR={list_games[value][3]}, MP={list_games[value][4]}, MT={list_games[value][5]}]")
            value += 1
#User selects a year to see which games are in that year from file and prints the game
    def printYear(self, list_games, input, file_name):
        input_file = open(file_name, 'r')
        value = 0
        count = 0
        for line in input_file.readlines():
            if input == list_games[value][1]:
                print(f"{list_games[value][0]} ({list_games[value][1]}) [GR={list_games[value][2]}, PR={list_games[value][3]}, MP={list_games[value][4]}, MT={list_games[value][5]}]")
                count += 1
            value +=1
        if count == 0:
            print(f"No games found for year: {input}")
#User selects a ranking range of the Mr. Gibbons rating of the game and prints any games from the file within that range
    def rankingRange(self, list_games, rank1, rank2, file_name):
        input_file = open(file_name, 'r')
        count = 0
        value = 0
        for line in input_file.readlines():
            if float(list_games[value][2]) >= float(rank1) and float(list_games[value][2]) <= float(rank2):
                print(f"{list_games[value][0]} ({list_games[value][1]}) [GR={list_games[value][2]}, PR={list_games[value][3]}, MP={list_games[value][4]}, MT={list_games[value][5]}]")
                count +=1
            value +=1
        if count == 0:
            print(f"No games in this ranking range")
#takes number from user where if the difference between the general public rating and Mr. Gibbons rating
#are different from each other by the user's input or more, it will print those games
    def peopleGibbons(self, list_games, input, file_name):
        input_file = open(file_name, 'r')
        value = 0
        count = 0
        for line in input_file.readlines():
            if float(input) >= abs(float(list_games[value][2]) - float(list_games[value][3])):
                print(f"{list_games[value][0]} ({list_games[value][1]}) [GR={list_games[value][2]}, PR={list_games[value][3]}, MP={list_games[value][4]}, MT={list_games[value][5]}]")
                count += 1
            value += 1
        if count == 0:
            print(f"No games found")
#User selects a desired minimim playtime of a game and prints all games of that minimum playtime or lower
    def playTime(self, list_games, input, file_name):
        input_file = open(file_name, 'r')
        count = 0
        value = 0
        for line in input_file.readlines():
            if input >= list_games[value][5]:
                print(f"{list_games[value][0]} ({list_games[value][1]}) [GR={list_games[value][2]}, PR={list_games[value][3]}, MP={list_games[value][4]}, MT={list_games[value][5]}]")
                count += 1
            value +=1
        if count == 0:
            print(f"No games found")