import math

def process(filename: str, part: int) -> list[int]:
    
    def part1(input: list[str]) -> int:
        
        nodes: dict[str, tuple[str,str]] = {}
        
        instructions: list[int] = [0 if c == "L" else 1 for c in input[0]]
        pos: str = "AAA"
        step: int = 0
        
        for l in input[2:]:
            key, direction = l.split(" = ")
            nodes[key] = tuple([dir for dir in direction[1: len(direction) - 1].split(', ')])
        
        i: int = 0   
        while not pos == 'ZZZ':
            step+=1
            pos = nodes[pos][instructions[i]]
            i = i+1 if i < len(instructions) - 1 else 0
        
        return step
        
    def part2(input: list[str]) -> int:
        
        nodes: dict[str, tuple[str,str]] = {}
        periods: list[int] = []
        
        instructions: list[int] = [0 if c == "L" else 1 for c in input[0]]
        
        step: int = 0
        
        for l in input[2:]:
            key, direction = l.split(" = ")
            nodes[key] = tuple([dir for dir in direction[1: len(direction) - 1].split(', ')])
            
        start_pos: set[str] = set(filter(lambda key: key[len(key) - 1] == "A", nodes.keys()))
                        
        i: int = 0
        for p in start_pos:
            step=0
            while not p[len(p)-1] == 'Z':
                step+=1
                p = nodes[p][instructions[i]]
                i = i+1 if i < len(instructions) - 1 else 0
            periods.append(step)
        
        # sorry i was too lazy
        return math.lcm(*periods)
                    
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
