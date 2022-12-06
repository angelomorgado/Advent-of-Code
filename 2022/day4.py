# Get data
data = [line.strip() for line in open('input_day4.txt', 'r')]

def part1():
    total = 0
    for line in data:
        elf1, elf2 = line.split(",")[0], line.split(",")[1]
        if (int(elf1.split("-")[0]) <= int(elf2.split("-")[0]) and int(elf1.split("-")[1]) >= int(elf2.split("-")[1])) \
        or (int(elf2.split("-")[0]) <= int(elf1.split("-")[0]) and int(elf2.split("-")[1]) >= int(elf1.split("-")[1])):
            total += 1
    print(total)

def part2():
    total = 0
    for line in data:
        elf1, elf2 = line.split(",")[0], line.split(",")[1]
        range1 = range(int(elf1.split('-')[0]), int(elf1.split('-')[1]) + 1)
        range2 = range(int(elf2.split('-')[0]), int(elf2.split('-')[1]) + 1)

        if int(elf1.split('-')[0]) in range2 or int(elf1.split('-')[1]) in range2 \
            or int(elf2.split('-')[0]) in range1 or int(elf2.split('-')[1]) in range1:
            total += 1
    print(total)

part1()
part2()