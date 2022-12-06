# Read data from file line by line and add to list in one line
data = [line.strip() for line in open('input_day1.txt', 'r')]

# Part 1
def ex1():
    max_calories = 0 
    tmp_calories = 0 
    for value in data:
        if value == '':
            if(tmp_calories > max_calories):
                max_calories = tmp_calories
            tmp_calories = 0
        else:
            tmp_calories += int(value)

    print(max_calories)

# Part 2
def ex2():
    calories_list = []
    tmp_sum = 0
    for value in data:
        if value == '':
            calories_list.append(tmp_sum)
            tmp_sum = 0
        else:
            tmp_sum += int(value)

    calories_list.sort()
    print(calories_list[-1] + calories_list[-2] + calories_list[-3])

#main
ex1()
ex2()