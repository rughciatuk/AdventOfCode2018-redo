INPUT = "input.txt"

def part_1(input_name):
    with open(input_name, "r") as input_file:
        data = input_file.readlines()
        curr_freq = 0
        for freq in map(lambda x: int(x.replace("\n", "")), data):
            curr_freq += freq
        return curr_freq

def part_2(input_name):
    with open(input_name, "r") as input_file:
        data = list(map(lambda x: int(x.replace("\n", "")), input_file.readlines()))

    old_freqs = set()
    curr_freq = 0
    freq_index = 0
    while curr_freq not in old_freqs:
        old_freqs.add(curr_freq)
        curr_freq += data[freq_index % len(data)]
        freq_index += 1

    return curr_freq


if __name__ == "__main__":
    print("part 1:", part_1(INPUT))
    print("part 2:", part_2(INPUT))

