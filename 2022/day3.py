# Get data
data = [line.strip() for line in open('input_day3.txt', 'r')]

def convert_char_to_int(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 26 + 1
    
def part1():
    total = 0
    for line in data:
        first, second = line[:len(line)//2], line[len(line)//2:]
        outlier = list(set(first) & set(second))[0]
        total += convert_char_to_int(outlier)
    print(total)

def part2():
    total = 0
    for i in range(0, len(data), 3):
        first_elve, second_elve, third_elve = data[i], data[i+1], data[i+2]
        badge = list(set(first_elve) & set(second_elve) & set(third_elve))[0]
        total += convert_char_to_int(badge)
    print(total)

part1()
part2()