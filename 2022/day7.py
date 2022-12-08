# Get data
data = [line.strip() for line in open('input_day7.txt', 'r')]
# data = [line.strip() for line in open('test.txt', 'r')]

from collections import defaultdict
size_dict = defaultdict(int)

def data_to_dict():
    current_dir = []

    for line in data:
        # Command
        if line.split()[0] == "$":
            if line.split()[1] == "cd":
                if line.split()[2] == "..":
                    current_dir.pop()
                else:
                    current_dir.append(line.split()[2])
            else:
                continue  
        # ls output       
        else:
            if line[0].isdigit():
                # Miguel
                size = line.split()[0]
                for i in range(len(current_dir)):
                    size_dict["".join(current_dir[:i + 1])] += int(size)
    
def part1():
    print(sum(f for f in size_dict.values() if f < 100_000))

def part2():
    print(min([f for f in size_dict.values() if size_dict['/'] - f <= 40_000_000]))

data_to_dict()
part1()
part2()