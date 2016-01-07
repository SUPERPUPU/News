from __future__ import absolute_import

import requests
from bs4 import BeautifulSoup
from celery.decorators import task
import sendgrid
from django.conf import settings
from micro_admin.models import User

from parse.models import News
from celery import shared_task


@shared_task
def add():
    print("1")
    return 1


@task()
def mul(x, y):
    return x * y


@task()
def xsum(numbers):
    return sum(numbers)

@task()
def par():
    res = requests.get(
            "https://news.google.com.tw/news/section?pz=1&ned=tw&topic=n&siidp=6ad8de07654b451fe8d2bb5fecb5c32affe3&ict=ln&sdm=EXPANDO&authuser=0")

    soup = BeautifulSoup(res.text, "html.parser")
    # title =[]


    # initialize table
    # con = lite.connect('db.sqlite3')
    # cur = con.cursor()
    # cur.execute (delete)

    News.objects.all().delete()

    for item in soup.select('.esc-body'):
        # News.objects.create(title = item.select('span')[0].text.encode('utf-8'))
        # title.append(item.select('span')[0].text)
        # title.append(json.dumps(item.select('span')[0].text,ensure_ascii=False))
        title = json.dumps(item.select('span')[0].text, ensure_ascii=False).strip('""')
        content = json.dumps(item.select('.esc-lead-snippet-wrapper')[0].text, ensure_ascii=False).strip('"')
        url = item.find_all("a", {'href': True})[0].get('href')
        source = json.dumps(item.find_all("span", class_="al-attribution-source")[0].text, ensure_ascii=False).strip(
                '"')
        photo = item.find_all("img", class_="esc-thumbnail-image")

        if not photo:
            photo = 1
        else:
            photo1 = photo
            photo = photo[0].get('imgsrc')
            if not photo:
                photo = photo1[0].get('src')

        # txt = json.dumps(bfsoup.find_all('.story_content', "p")[0].text,ensure_ascii=False)
        if photo == 1:
            photo = "//upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/275px-Cat03.jpg"
        # add to database
        # cur.execute (sql, data)
        News.objects.create(title=title, content=content, source=source, url=url, photo=photo)