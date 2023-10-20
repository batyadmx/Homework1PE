from bs4 import BeautifulSoup
import pandas as pd

with open("задания/5/text_5_var_100", encoding="UTF-8") as file:
    html = ''.join(file.readlines())

table = BeautifulSoup(html, "html.parser").findChildren("table")[0]

rows = table.findChildren('tr')
names = list(map(lambda x: x.string, rows[0].findChildren('th')))

df = pd.DataFrame(columns = names)

for row in rows[1:]:
    cells = row.findChildren('td')
    df.loc[len(df)] = list(map(lambda x: x.string, cells))

df.to_csv("task5_answer.csv")