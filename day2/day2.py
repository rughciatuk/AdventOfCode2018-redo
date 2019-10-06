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

def check_char_diff(word1, word2,wanted=1):
    if len(word1) != len(word2):
        return False
    
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
            if count > wanted:
                return False
    return True

def part_2(input_name):
    with open(input_name, "r") as input_file:
        data = list(map(lambda x: x.replace("\n", ""), input_file.readlines()))
    
    for i in range(len(data) -1):
        for j in range(i+1, len(data)):
            word1 = data[i]
            word2 = data[j]
            if (check_char_diff(word1, word2)):
                word1_letters = set(word1)
                word2_letters = set(word2)
                return word1.replace(word1_letters.difference(word2_letters).pop(), "")


if __name__ == "__main__":
    print("Part 1:", part_1(INPUT))
    print("Part 2:", part_2(INPUT))
    