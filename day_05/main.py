def process_seeds(filename: str, part: int) -> list[int]:
    
    def get_lowest_destination_2(seeds: list[str]) -> int:
        
        parsing: list[list[str]] = [s.split("\n") for s in seeds]
        seeds : list[int] = [int(x) for x in parsing[0][0].split(':')[1].strip().split()]
        seed_pairs = list(zip(seeds[::2], seeds[1::2]))
        categories = parsing[1:]
        
        minimums: list[int] = []
        
        for pair in seed_pairs:
            # [pair_start; pair_start + pair_range [
            # [section_start; section_start + section_range [
            # If pair_start < section_start : Skip until section_start
            # If pair_start + pair_range > section_start + section_range : Skip above section_start + section_range
            # We need to search inside intersection to avoid operations as much as possible
            
            intervals: list[tuple[int, int]] = []
            intervals = [(pair[0], pair[0] + pair[1])]
            
            for category in categories:
                
                local_intervals: list[tuple[int, int]] = []

                for zone in category[1:]:
                                        
                    movements: list[int] = [int(x) for x in zone.split()]

                    for interval in intervals:
                        min_int = max(movements[1], interval[0])
                        max_int = min(movements[1] + movements[2], interval[1])                    
                    
                        if max_int < min_int:
                            pass
                        else:
                            offset = movements[0] - movements[1]
                            local_intervals.append((min_int + offset, max_int + offset))
                      
                intervals = local_intervals          
            
            minimums.append(min([ x[0] for x in intervals]))   
                           
        return min(minimums)
    
    def get_lowest_destination(seeds: list[str]) -> int:
        
        parsing: list[list[str]] = [s.split("\n") for s in seeds]
        seeds_coordinates : list[int] = [int(x) for x in parsing[0][0].split(':')[1].strip().split()]
        categories = parsing[1:]
                
        seeds_destinations: list[int] = []
                        
        for coords in seeds_coordinates:
            local_coords = coords
            for category in categories:
                for zone in category[1:]:
                    
                    movements: list[int] = [int(x) for x in zone.split()]
                    
                    if movements[1] <= local_coords < movements[1] + movements[2]:
                        local_coords = local_coords + movements[0] -  movements[1]
                        break
                        
            seeds_destinations.append(local_coords)
                                
        return min(seeds_destinations)
            
                    
    with open(filename, encoding="utf-8") as f:
        seeds = f.read().split("\n\n")

    # Opening file and sum

    if(part == 1) :
        return get_lowest_destination(seeds)

    elif(part == 2):
        return get_lowest_destination_2(seeds)


if __name__ == "__main__":
    input_path = "./input.txt"
    print("Problem 1:")
    print(process_seeds(input_path, 1))

    print("Problem 2:")
    print(process_seeds(input_path, 2))
