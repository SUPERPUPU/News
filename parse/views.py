from django.shortcuts import render
from datetime import datetime
# Create your views here.

import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from parse.models import News
import json

def hello_world(request):

    return HttpResponse("Hello World!")


def parse(request):
    # get all the posts
	res = requests.get ("https://news.google.com.tw/news/section?pz=1&ned=tw&topic=n&siidp=6ad8de07654b451fe8d2bb5fecb5c32affe3&ict=ln&sdm=EXPANDO&authuser=0")

	soup = BeautifulSoup (res.text, "html.parser")
	title =[]
	n=0
	for item in soup.select('.esc-body'):
		#News.objects.create(title = item.select('span')[0].text.encode('utf-8'))
		#title.append(item.select('span')[0].text)
		title.append(json.dumps(item.select('span')[0].text,ensure_ascii=False))
		News.objects.create(title = json.dumps(item.select('span')[0].text,ensure_ascii=False))
    #news_list = News.objects.all()
	return render(request,
                  'parse.html',
                  {'News': News})



