with open("задания/3/text_3_var_100") as file:
    lines = file.readlines()

res = []
for line in lines:
    nums = line.split(',')

    for i, num in enumerate(nums):
        if num == "NA":
            val = (int(nums[i - 1]) if i != 0 else 0) + (int(nums[i + 1]) if i < len(nums) - 1 else 0)
            val /= 2
            nums[i] = str(val)

    nums = list(filter(lambda x: x ** 0.5 > 150, map(float, nums)))
    res.append(nums)

with open('task3_answer.txt', 'w') as file:
    for r in res:
        file.write(','.join(map(str, r)) + "\n")