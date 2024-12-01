def process_games(filename: str, part: int) -> list[int]:

    # Opening file and sum

    def is_game_possible_1(game: str) -> int:

        colors_max = {
            'red': 12,
            'green': 13,
            'blue': 14
        }

        # Could have done it with regex but i only want to use native python
        game_id = int("".join([i for i in game.split(":")[0].split() if i.isdigit()]))
        rounds = game.split(":")[1].split("; ")

        for round in rounds:

            colors = round.split(', ')

            for color in colors:
                for color_max_key in colors_max:
                    if color_max_key in color:
                        res = [i for i in color.split() if i.isdigit()]
                        num = int("".join(res))
                        if num > colors_max[color_max_key]:
                            return 0

        return game_id

    def is_game_possible_2(game: str) -> int:

        colors_max = {
            'red': 1,
            'green': 1,
            'blue': 1
        }
        
        rounds = game.split(":")[1].split("; ")

        for round in rounds:

            colors = round.split(', ')

            for color in colors:
                for color_max_key in colors_max:
                    if color_max_key in color:
                        res = [i for i in color.split() if i.isdigit()]
                        num = int("".join(res))
                        if num > colors_max[color_max_key]:
                            colors_max[color_max_key] = num

        return colors_max['red']*colors_max['green']*colors_max['blue']

    with open(filename, encoding="utf-8") as f:
        games = f.read().split("\n")

    if(part == 1) :
        return sum([is_game_possible_1(x) for x in games])

    elif(part == 2):
        return sum([is_game_possible_2(x) for x in games])


if __name__ == "__main__":
    input_path = "./input.txt"
    print("Problem 1:")
    print(process_games(input_path, 1))

    print("Problem 2")
    print(process_games(input_path, 2))
