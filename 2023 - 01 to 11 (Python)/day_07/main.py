def process(filename: str, part: int) -> list[int]:
    
    symbols_orders_1: list[str] = ['A', 'K', 'Q', 'J', 'T'] + [str(i) for i in range(9, 1, -1)]
    
    symbols_orders_2: list[str] = ['A', 'K', 'Q', 'T'] + [str(i) for i in range(9, 1, -1)] + ['J']

        
    def part1(input: list[str]) -> int:
        
        # Tuple is : (score, hand, bid)
        hand_scores: list[tuple(int, str, int)] = []
        
        # Score
        for l in input:
            
            hand, bid = l.split(' ')
            
            unique_symbols: set[str] = set([c for c in hand])
            max_cards = max([hand.count(x) for x in unique_symbols])
            
            score: int = 2**(5 - len(unique_symbols)) + max_cards

            hand_to_insert: tuple(int, str, int) = (score, hand, int(bid))
            inserted: bool = False
            
            for i in range(0, len(hand_scores)):
                if inserted:
                    break
                
                s2: int = hand_scores[i][0]
                if s2 < score:
                    hand_scores.insert(i, hand_to_insert)
                    inserted = True
                    break
                elif s2 == score:
                    for c1, c2 in zip(hand, hand_scores[i][1]):
                        c1_weight: int = symbols_orders_1.index(c1)
                        c2_weight: int = symbols_orders_1.index(c2)
                        if c1_weight < c2_weight:
                            hand_scores.insert(i, hand_to_insert)
                            inserted = True
                            break
                        elif c1_weight > c2_weight:
                            break
            
            if not inserted:
                hand_scores.append(hand_to_insert)
                
        return sum([(len(hand_scores) - i )*x[2] for i,x in enumerate(hand_scores)])
    
    
    # The part 2 is AWFUL, i need to rewrite it but at least it works lol                
    def part2(input: list[str]) -> int:
        
        # Tuple is : (score, hand, bid)
        hand_scores: list[tuple(int, str, int)] = []
        
        # Score
        for l in input:
            
            hand, bid = l.split(' ')            
            score: int = 0
                        
            if 'J' in hand: 
                occ_letter: tuple[int, str] = (0,'')
                for c in symbols_orders_2[:len(symbols_orders_2)-1]:
                    occ_letter = (hand.count(c), c) if hand.count(c) > occ_letter[0]  else occ_letter
                    
                new_hand: str = ''
                if occ_letter[0] != 0:
                    new_hand = hand.replace('J', occ_letter[1])
                else:
                    new_hand = hand
                
                unique_symbols: set[str] = set([c for c in new_hand])
                max_cards = max([new_hand.count(x) for x in unique_symbols])
                score = 2**(5 - len(unique_symbols)) + max_cards   
            else:
                unique_symbols: set[str] = set([c for c in hand])
                max_cards = max([hand.count(x) for x in unique_symbols])
                score = 2**(5 - len(unique_symbols)) + max_cards            

            hand_to_insert: tuple(int, str, int) = (score, hand, int(bid))
            inserted: bool = False
            
            for i in range(0, len(hand_scores)):
                if inserted:
                    break
                
                s2: int = hand_scores[i][0]
                if s2 < score:
                    hand_scores.insert(i, hand_to_insert)
                    inserted = True
                    break
                elif s2 == score:
                    for c1, c2 in zip(hand, hand_scores[i][1]):
                        c1_weight: int = symbols_orders_2.index(c1)
                        c2_weight: int = symbols_orders_2.index(c2)
                        if c1_weight < c2_weight:
                            hand_scores.insert(i, hand_to_insert)
                            inserted = True
                            break
                        elif c1_weight > c2_weight:
                            break
            
            if not inserted:
                hand_scores.append(hand_to_insert)
                
       #print(hand_scores)
                
        return sum([(len(hand_scores) - i )*x[2] for i,x in enumerate(hand_scores)])
                    
    # Opening files and parts

    with open(filename, encoding="utf-8") as f:
        input = f.read().split("\n")

    if(part == 1) :
        return part1(input)

    elif(part == 2):
        return part2(input)


if __name__ == "__main__":
    input_path = "./input.txt"
    print("Problem 1:")
    print(process(input_path, 1))

    print("Problem 2:")
    print(process(input_path, 2))
