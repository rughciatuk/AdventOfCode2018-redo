from collections import Counter

INPUT = "input.txt"

def part_1(input_name):
    with open(input_name, "r") as input_file:
        data = list(map(lambda x: x.replace("\n", ""),input_file.readlines()))
    
    two_letters = 0
    three_letters = 0

    for word in data:
        freqencies = Counter(word).values()
        if 2 in freqencies:
            two_letters += 1
        if 3 in freqencies:
            three_letters += 1

    return two_letters * three_letters
    
if __name__ == "__main__":
    print("Part 1: ",part_1(INPUT))
    