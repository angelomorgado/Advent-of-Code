# Get data
data = [line.strip() for line in open('input_day2.txt', 'r')]

'''
A, X : Rock (1)
B, Y : Paper (2)
C, Z : Scissors (3)
'''

score_dict = dict.fromkeys( ["A", "X"], 1) \
            | dict.fromkeys(["B", "Y"] , 2) \
            | dict.fromkeys(["C", "Z"] , 3)

#Ex 1 dict
#Victory 6 \ Draw 3\ Defeat 0
pontuation_dict_ex1 = dict.fromkeys(["A Y", "B Z", "C X"] , 6) \
                | dict.fromkeys( ["A X", "B Y", "C Z"], 3) \
                | dict.fromkeys(["A Z", "B X", "C Y"] , 0) \

# Part 1
def ex1():
    total_points = 0
    for line in data:
        my_play = line.split(" ")[1]
        total_points += score_dict[my_play] + pontuation_dict_ex1[line]
    
    print(f"Total points: {total_points}")

'''
X : Lose
Y : Draw
Z : Win

A : Rock
B : Paper
C : Scissors

A beats C, C beats B, and B beats A
'''
# Key beats value
outcome_dict = {
    "A" : "C",
    "C" : "B",
    "B" : "A"
}

# Part 2
def ex2():
    total_points = 0
    for line in data:
        outcome = line.split(" ")[1]
        adversary_play = line.split(" ")[0]

        # Loss
        if outcome == "X":
            total_points += score_dict[outcome_dict[adversary_play]]
        # Draw
        elif outcome == "Y":
            total_points += score_dict[adversary_play] + 3
        # Win
        else:
            total_points += score_dict[list(outcome_dict.keys())[list(outcome_dict.values()).index(adversary_play)]] + 6
    print(f'Total points: {total_points}')

ex1()
ex2()