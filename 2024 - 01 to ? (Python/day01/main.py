from typing import Dict, List


def part1(filename: str) -> int:
    
    with open(filename, encoding="utf-8") as f:
        input = f.read().split("\n")
        
    leftList: List[int] = []
    rightList: List[int] = []
     
    for row in input:
        left, right = row.split()
        leftList.append(int(left))
        rightList.append(int(right))
        
    leftList.sort()
    rightList.sort()
    
    result: int = sum([ abs(left - right) for left, right in zip(leftList, rightList)])
    
    return result

def part2(filename: str) -> int:
    
    with open(filename, encoding="utf-8") as f:
        input = f.read().split("\n")
        
    numbers: List[int] = []
    occurences: Dict[int, int] = {}
     
    for row in input:
        left, right = [int(x) for x in row.split()]
                
        numbers.append(int(left))
        occurences[right] = 1 if occurences.get(right) == None else occurences[right] + 1 
        
    
    result: int = sum([ number * (occurences[number] if occurences.get(number) != None else 0) for number in numbers])
    
    return result

if __name__ == "__main__":
    input_path = "./input.txt"
    print("Problem 1:")
    print(part1(input_path))

    print("Problem 2")
    print(part2(input_path))