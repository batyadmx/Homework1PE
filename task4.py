import pandas as pd

names = ['id', 'name', "surname", 'age', 'salary', 'phone_number']
df = pd.read_csv("задания/4/text_4_var_100", names=names)

ageFilter = df['age'] > 20
df = df[ageFilter]

df['numSalary'] = list(map(lambda x: int(x[:-1]), df['salary']))
mean = df['numSalary'].mean()
salaryFilter = df['numSalary'] > mean
df = df[salaryFilter]

df = df.drop(['phone_number', 'numSalary'], axis=1)
df = df.sort_values(by=['id'])

df.to_csv("task4_answer.csv", )




