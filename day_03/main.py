def process_engine(filename: str, part: int) -> list[int]:

    def get_line_sum(lines: list[str], i: int) -> int:

        valid_numbers: List[int] = []
        tmp_num: str = ""

        for x, c in enumerate(lines[i]):

            if c.isdigit():
                tmp_num+=c

            if (not c.isdigit() and tmp_num != "") or (c.isdigit() and x == len(lines[i]) - 1):
                is_valid: bool = False

                # That line is awfull but i'm to lazy to start again
                start_x = x - len(tmp_num) if x == len(lines[i]) - 1 and c.isdigit() else x - len(tmp_num) -1

                for dx in range(start_x, x + 1):
                    for dy in [-1, 0, 1]:
                        if 0 <= i + dy < len(lines) and 0 <= dx < len(lines[i]) and lines[i + dy][dx] != "." and not lines[i + dy][dx].isdigit():
                            is_valid = True

                if is_valid:
                    valid_numbers.append(int(tmp_num))
                
                tmp_num = ""

        return sum(valid_numbers)

    def get_gears_ratio(lines: list[str]) -> int:

        ratios: List[int] = []

        gears: Dict[Tuple, List[int]] = {}

        tmp_gear: int = 0
        tmp_num: str = ""


        for y, line in enumerate(lines):
            for x, c in enumerate(line):

                if c.isdigit():
                    tmp_num+=c

                if (not c.isdigit() and tmp_num != "") or (c.isdigit() and x == len(lines[y]) - 1):

                    # That line is awfull but i'm to lazy to start again
                    start_x = x - len(tmp_num) if x == len(lines[y]) - 1 and c.isdigit() else x - len(tmp_num) -1

                    stop : bool = False
                    for dx in range(start_x, x + 1):
                        for dy in [-1, 0, 1]:
                            if 0 <= y + dy < len(lines) and 0 <= dx < len(lines[y]) and lines[y + dy][dx] == "*":
                                if (dx, y+dy) in gears:
                                    gears[(dx, y+dy)].append(int(tmp_num))
                                else: 
                                    gears[(dx, y+dy)] = [int(tmp_num)]
                                stop = True
                                break
                        if stop:
                            break
                    
                    tmp_num = ""

        sum_of_gears: int =0
        for gs in gears.values():
            if len(gs) > 1:
                mult: int = 1
                for g in gs:
                    mult *= g
                sum_of_gears += mult
        return sum_of_gears

    with open(filename, encoding="utf-8") as f:
        engine = f.read().split("\n")

    # Opening file and sum

    if(part == 1) :
        return sum([get_line_sum(engine, i) for i in range(0, len(engine))])

    elif(part == 2):
        return get_gears_ratio(engine)


if __name__ == "__main__":
    input_path = "./input.txt"
    print("Problem 1:")
    print(process_engine(input_path, 1))

    print("Problem 2:")
    print(process_engine(input_path, 2))
