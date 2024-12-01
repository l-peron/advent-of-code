def process(filename: str, part: int) -> list[int]:
    
    def part1(input: list[str]) -> int:
        
        map = [list(line) for line in input]
        
        for y, line in enumerate(map):
            if set(line) == set("."):
                print("allo")
                raw_array: list[str] = ["." for i in range(0, len(line))]
                map.insert(y, raw_array)
                print(map)

            #for x, c in enumerate(line):
        print(map)
        raw_array: list[str] = ["." for i in range(0, len(line))]
        map.insert(y, raw_array)
        pass
        
    def part2(input: list[str]) -> int:
        pass
                    
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
