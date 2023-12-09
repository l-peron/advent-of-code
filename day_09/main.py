def process(filename: str, part: int) -> list[int]:
    
    def part1(line: str) -> int:

        nodes: list[list[int]] = [[int(num) for num in line.split()]]
            
        # Creating Tree
        i: int = 0
        while not nodes[len(nodes) -1].count(0) == len(nodes[len(nodes) -1]):
            diff_list: list[int] = []
            for n in range(0, len(nodes[i]) - 1):
                diff_list.append(nodes[i][n+1] - nodes[i][n])
            nodes.append(diff_list)
            i += 1
            
        # Finding last lnumber
        final_num: int = 0
        for h in range(len(nodes) - 2, -1, -1):
            new_num: int = nodes[h][len(nodes[h]) -1] + final_num
            final_num = new_num
         
        return(final_num)
        
    def part2(line: str) -> int:
        
        nodes: list[list[int]] = [[int(num) for num in line.split()]]
            
        # Creating Tree
        i: int = 0
        while not nodes[len(nodes) -1].count(0) == len(nodes[len(nodes) -1]):
            diff_list: list[int] = []
            for n in range(0, len(nodes[i]) - 1):
                diff_list.append(nodes[i][n+1] - nodes[i][n])
            nodes.append(diff_list)
            i += 1
            
        # Finding last lnumber
        final_num: int = 0
        for h in range(len(nodes) - 2, -1, -1):
            new_num: int = nodes[h][0] - final_num
            final_num = new_num
         
        return(final_num)
                    
    # Opening files and parts

    with open(filename, encoding="utf-8") as f:
        input = f.read().split("\n")

    if(part == 1) :
        return sum([part1(line) for line in input])

    elif(part == 2):
        return sum([part2(line) for line in input])


if __name__ == "__main__":
    input_path = "./input.txt"
    print("Problem 1:")
    print(process(input_path, 1))

    print("Problem 2:")
    print(process(input_path, 2))
