import re

with open("задания/1/text_1_var_100") as file:
    text = file.readlines()

words = re.findall("([a-zA-z]+)", ''.join(text))

freqDict = {}

for word in words:
    if word not in freqDict:
        freqDict[word] = 0
    freqDict[word] += 1

with open("task1_answer.txt", "w") as file:
    for k, v in sorted(freqDict.items(), key=lambda x: x[1], reverse=True):
        file.write(f"{k}: {v}\n")
