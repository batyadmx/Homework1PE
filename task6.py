import requests as re
from airium import Airium

data = re.get("https://api.waifu.im/search?many=true").json()

a = Airium()

a('<!DOCTYPE html>')
with a.html(lang="ru"):
    with a.head():
        a.meta(charset="utf-8")
        a.title(_t="Waifu")

    with a.body():
        for i, image in enumerate(data['images']):
            with a.div():
                with a.h3():
                    a(f"Waifu no.{i + 1}")
                a.img(src=image['url'], alt='Waifu', width = "500", height = "500")


with open("task6_answer.html", 'w') as file:
    file.write(str(a))

