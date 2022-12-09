import numpy as np

# Get the data
# data = np.array([[*line.strip()] for line in open('input_day8.txt', 'r')])
data = np.array([[*line.strip()] for line in open('test.txt', 'r')])

def part1():
    total = 0
    # Horizontal
    for y in range(1, len(data) - 1):
        for x in range(1, len(data) - 1):
            top = list(map(int,data[:y, x]))
            bottom = list(map(int,data[y+1:, x]))
            left = list(map(int,data[y, :x]))
            right = list(map(int,data[y, x+1:]))

            if max(left) < int(data[y, x]): total += 1
            elif max(right) < int(data[y, x]): total += 1
            elif max(top) < int(data[y, x]): total += 1
            elif max(bottom) < int(data[y, x]): total += 1
                
    print(total + (len(data) - 1) * 4)

# TODO: This is not working correctly
def get_visible_trees_count(x, y, l):
    max_value = -1
    total = 0
    for v in l:
        if v > int(data[y, x]):
            break

        if v > max_value:
            max_value = v
            total += 1
    
    return total


def part2():
    score_list = np.ones((len(data), len(data)), dtype=int)
    for y in range(1, len(data) - 1):
        for x in range(1, len(data) - 1):
            top = list(map(int,data[:y, x]))[::-1]
            bottom = list(map(int,data[y+1:, x]))
            left = list(map(int,data[y, :x]))[::-1]
            right = list(map(int,data[y, x+1:]))

            # Top
            top_score = get_visible_trees_count(x, y, top)
            bottom_score = get_visible_trees_count(x, y, bottom)
            left_score = get_visible_trees_count(x, y, left)
            right_score = get_visible_trees_count(x, y, right)

            if y == 1 and x == 2 or y == 3 and x == 2:
                print(f'({x}, {y}):')
                print(top_score, left_score, right_score, bottom_score)

            score_list[y, x] = top_score * bottom_score * left_score * right_score
        
    print(np.max(score_list))
    print(data)
    print(score_list)
part1()
part2()