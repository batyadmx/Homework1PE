with open("задания/2/text_2_var_100") as file:
    lines = file.readlines()

sums = []

for line in lines:
    nums = map(int, line.split('.'))
    sums.append(sum(nums))

with open("task2_answer.txt", 'w') as file:
    for sum in sums:
        file.write(f"{sum} \n")