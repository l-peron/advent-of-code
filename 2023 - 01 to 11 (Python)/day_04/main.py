def process_games(filename: str, part: int) -> list[int]:

    def get_game_points(game: str) -> int:

        all_numbers: List[str] = [part.strip() for part in game.split(':')[1].split('|')]
        winning_numbers: List[int] = [int(num) for num in filter(lambda x: x.isdigit(), all_numbers[0].split(' '))]
        drew_numbers: List[int] = [int(num) for num in filter(lambda x: x.isdigit(), all_numbers[1].split(' '))]

        count: int = -1
        for winning_number in winning_numbers:
            if winning_number in drew_numbers:
                count += 1
                
        return 2**count if count > -1 else 0

    def get_scratchcards_total(games: list[str]) -> int:

        winned_cards: Dict[int, int] = {}

        for game in games:

            card_id: int = int(game.split(':')[0].replace("Card", "").strip())
            if card_id not in winned_cards:
                winned_cards[card_id] = 1

            all_numbers: List[str] = [part.strip() for part in game.split(':')[1].split('|')]
            winning_numbers: List[int] = [int(num) for num in filter(lambda x: x.isdigit(), all_numbers[0].split(' '))]
            drew_numbers: List[int] = [int(num) for num in filter(lambda x: x.isdigit(), all_numbers[1].split(' '))]

            count = 1
            for drew_number in drew_numbers:
                if drew_number in winning_numbers:
                    if card_id + count in winned_cards:
                        winned_cards[card_id + count] += winned_cards[card_id]
                    elif card_id in winned_cards:
                        winned_cards[card_id + count] = 1 + winned_cards[card_id]
                    count += 1
                
        return sum(winned_cards.values())

    with open(filename, encoding="utf-8") as f:
        games = f.read().split("\n")

    # Opening file and sum

    if(part == 1) :
        return sum([get_game_points(game) for game in games])

    elif(part == 2):
        return get_scratchcards_total(games)


if __name__ == "__main__":
    input_path = "./input.txt"
    print("Problem 1:")
    print(process_games(input_path, 1))

    print("Problem 2:")
    print(process_games(input_path, 2))
