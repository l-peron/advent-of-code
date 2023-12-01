def process_calibrations(filename: str, part: int) -> list[int]:

    def get_digits_1(calibration: str) -> int:
        digit = ""

        for i in range(0, len(calibration), 1):
            if calibration[i].isnumeric():
                digit+=calibration[i]
                break
        for j in range(len(calibration)-1, -1, -1):
            if calibration[j].isnumeric():
                digit+=calibration[j]
                break
        
        return int(digit)

    def get_digits_2(calibration: str) -> int:

        digits: List[str] = ["" for _ in calibration]

        translations: Dict[str, str] = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }
        
        for key in translations:
            if key in calibration:
                search_sub = calibration
                mem_index = 0

                for i in range(calibration.count(key)):
                    index = search_sub.index(key)
                    digits[mem_index + index] = translations[key]
                    mem_index += index + len(key)
                    search_sub = search_sub[index+len(key):]

        for i in range(0, len(calibration), 1):
            if calibration[i].isnumeric():
                digits[i] = calibration[i]
                break
        for j in range(len(calibration)-1, -1, -1):
            if calibration[j].isnumeric():
                digits[j] = calibration[j]
                break
            
        filtered = list(filter(lambda x: x != "", digits))
        return int(filtered[0] + filtered[len(filtered) - 1])

    # Opening file and sum

    with open(filename, encoding="utf-8") as f:
        calibrations = f.read().split("\n")

    if(part == 1) :
        return sum([get_digits_1(x) for x in calibrations])

    elif(part == 2):
        return sum([get_digits_2(x) for x in calibrations])


if __name__ == "__main__":
    input_path = "./input.txt"
    print("Problem 1:")
    print(process_calibrations(input_path, 1))

    print("Problem 2")
    print(process_calibrations(input_path, 2))
