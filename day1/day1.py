with open("input.txt", "r") as input_file:
    data = input_file.readlines()
    curr_freq = 0
    for freq in map(lambda x: int(x.replace("\n", "")), data):
        curr_freq += freq
    print("Curr freq:", curr_freq)
    