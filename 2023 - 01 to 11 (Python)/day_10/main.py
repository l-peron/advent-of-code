class Node:
    def __init__(self, key, left = (-1, -1), right = (-1, -1)):
        self.key = key
        self.left = left
        self.right = right
        

def process(filename: str, part: int) -> list[int]:
    
    directions: dict[str, list[tuple[int, int]]] = {
        # Key: [(Y, X), (Y, X)]
        "|": [(1, 0), (-1, 0)],
        "-": [(0,1), (0, -1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
        ".": []
    }
    
    neighbors: list[tuple[int,int]] = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]
    
    def add_tuples(tuple1: tuple[int,int], tuple2: tuple[int, int]):
        return tuple(sum(x) for x in zip(tuple1, tuple2))
    
    def parcours_largeur_iter(root_coords: tuple[int, int], map: list[list[str]]) -> int:
        # Structure is [((Y,X), distance),...]
        node_file: list[tuple[tuple[int, int], int]] = []
        done_nodes: set(tuple[int, int]) = set()
        max_dist: int = 0
        
        node_file.append((root_coords, 0))
        done_nodes.add(root_coords)
        
        while len(node_file):
            node, distance = node_file.pop(0)
            symbol: str = map[node[0]][node[1]]
            for dir in directions[symbol]:
                new_node = add_tuples(node, dir)
                if new_node not in done_nodes:
                    new_distance = distance + 1
                    if new_distance > max_dist:
                        max_dist = new_distance
                    node_file.append((add_tuples(node, dir), new_distance))
                    done_nodes.add(new_node)
        
        return max_dist
    
    def parcours_profondeur_rec(root_coords: tuple[int, int], map: list[list[str]], nodes: list[tuple[int, int]] = []) -> set[tuple[int, int]]:
        # Structure is [((Y,X), distance),...]
        done_nodes: set(tuple[int, int]) = set()
        
        done_nodes.add(root_coords)
        
        symbol: str = map[root_coords[0]][root_coords[1]]
        for dir in directions[symbol]:
            new_node = add_tuples(root_coords, dir)
            if new_node not in done_nodes:
                done_nodes |= parcours_profondeur_rec(new_node, map, done_nodes)
                done_nodes.add(new_node)            
        
        return done_nodes
    
    def part1(input: list[str]) -> int:
        
        # We need to convert to a list of char because python can't modify a specific character in a string lol
        map: list[list[str]] = [list(line) for line in input]
        
        initial_coordinates: tuple[int,int] = (0,0)
        initial_symbol: str = ""
        distances: dict[tuple[int,int], int] = {}
        
        # Finding "S" coordinates
        for i, line in enumerate(map):
            finded: bool = False
            for j, character in enumerate(line):
                if character == "S":
                    initial_coordinates = (i ,j)
                    break
            if finded:
                break
            
        # Finding "S" real symbol
        s_directions: list[tuple[int, int]] = []
        for n in neighbors:
            coords = add_tuples(initial_coordinates, n)
            symbol: str = map[coords[0]][coords[1]]
            for dir in directions[symbol]:
                if add_tuples(dir, coords) == initial_coordinates:
                    s_directions.append(tuple([ -x for x in dir]))
        
        # Replace "S" by its real symbol
        for k, v in directions.items():
            if set(v) == set(s_directions):
                map[initial_coordinates[0]][initial_coordinates[1]] = k
                break
            
        # Searching global maximum
        result = parcours_largeur_iter(initial_coordinates, map)                
                                                    
        return result
        
    def part2(input: list[str]) -> int:
        
        # We need to convert to a list of char because python can't modify a specific character in a string lol
        map: list[list[str]] = [list(line) for line in input]
        corners: list[str] = ['J', 'F', '7', 'L']
        straight: list[str] = ['|', '-']
        counter: int = 0
        
        def is_straight(c: str) -> bool:
            return c in straight
        
        def is_corner(c: str) -> bool:
            return c in corners
        
        # Finding "S" coordinates
        for i, line in enumerate(map):
            finded: bool = False
            for j, character in enumerate(line):
                if character == "S":
                    initial_coordinates = (i ,j)
                    break
            if finded:
                break
            
        # Finding "S" real symbol
        s_directions: list[tuple[int, int]] = []
        for n in neighbors:
            coords = add_tuples(initial_coordinates, n)
            symbol: str = map[coords[0]][coords[1]]
            for dir in directions[symbol]:
                if add_tuples(dir, coords) == initial_coordinates:
                    s_directions.append(tuple([ -x for x in dir]))
        
        # Replace "S" by its real symbol
        for k, v in directions.items():
            if set(v) == set(s_directions):
                map[initial_coordinates[0]][initial_coordinates[1]] = k
                break
            
        print(parcours_profondeur_rec(initial_coordinates, map))
        
        
        for i, line in enumerate(map):
            border_finded: bool = False
            corner_finded: bool = False
            inner_counter: int = 0
            
            for j, c in enumerate(line):
                if is_corner(c) and not corner_finded:
                    pass
                if is_straight(c) and not border_finded:
                    border_finded = True
                    inner_counter = 0
                elif is_straight(c):
                    border_finded = False
                    counter += inner_counter
                    if inner_counter > 0:
                        print(f"{j}:{inner_counter}")
                elif is_corner(c) and not border_finded:
                    if j < len(line) - 1 and is_corner(line[j+1]):
                        border_finded = True
                        inner_counter = 0
                elif is_corner(c) and border_finded:
                    border_finded = False
                    counter += inner_counter
                elif border_finded:
                    inner_counter +=1
                    print(f"({i},{j})")                    
        return counter
                    
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
