def process(filename: str, part: int) -> list[int]:
    
    def part1(input: list[str]):
        times = [int(x) for x in  filter(lambda x: x.isdigit(), input[0].split(':')[1].strip().split())]
        records = [int(x) for x in  filter(lambda x: x.isdigit(), input[1].split(':')[1].strip().split())]
        
        solutions: int = 1
        
        for t, r in zip(times, records):
            count: int = 0
            for i in range(0, t):
                dist = i*(t-i)
                if dist > r:
                    count += 1
            solutions *= count
        
        return solutions
                    
    def part2(input: list[str]):
        time = int(input[0].split(':')[1].replace(' ', ''))
        record = int(input[1].split(':')[1].replace(' ', ''))
        
        count: int = 0
        
        for i in range(0, time):
            dist = i*(time-i)
            if dist > record:
                count += 1
                
        return count
                    
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
