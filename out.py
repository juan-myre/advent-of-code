f = open("games.txt", "r")

from functools import reduce

def processRounds(games):
    EMPTY_GAME = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    all_games = []
    for game in games:
        colors = game.split(", ")
        curr_game = EMPTY_GAME.copy()
        for color in colors:
            parts = color.split(" ")
            curr_game[parts[1].strip()] = int(parts[0])
        all_games.append(curr_game)

    return all_games

def getValidGames():
    max_red = 12
    max_green = 13
    max_blue = 14

    valid_games = []

    for line in f:
        parts = line.split(": ")
        game_number = int(parts[0].split(" ")[1])
        games = parts[1].split("; ")
        all_rounds = processRounds(games)

        valid = True

        for round in all_rounds:
            if round["red"] > max_red or round["green"] > max_green or round["blue"] > max_blue:
                valid = False
                break

        if valid:
            valid_games.append(game_number)


    print(sum(valid_games))


def getPowerGames():
    sum_of_powers = 0

    for line in f:
        parts = line.split(": ")
        game_number = int(parts[0].split(" ")[1])
        games = parts[1].split("; ")
        all_rounds = processRounds(games)

        max_red = 0
        max_green = 0
        max_blue = 0
        for round in all_rounds:
            if round["red"] > max_red:
                max_red = round["red"]
            if round["green"] > max_green:
                max_green = round["green"]
            if round["blue"] > max_blue:
                max_blue = round["blue"]

        valid_colors = list(filter(lambda x: x > 0, [max_red, max_green, max_blue]))

        sum_of_powers += reduce((lambda x, y: x * y), valid_colors)

    print(sum_of_powers)

getPowerGames()