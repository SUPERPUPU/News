from django.shortcuts import render
from datetime import datetime
# Create your views here.

import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse

def hello_world(request):

    return render(request,
                  'parse.html',
                  {'current_time': datetime.now()})


def parse(request):
    # get all the posts

	res = requests.get ("https://news.google.com.tw/news/section?pz=1&ned=tw&topic=n&siidp=6ad8de07654b451fe8d2bb5fecb5c32affe3&ict=ln&sdm=EXPANDO&authuser=0")

	soup = BeautifulSoup (res.text, "html.parser")
	title =[]
	n=0
	for item in soup.select('.esc-body'):
		title.append(item.select('span')[0])
    #news_list = News.objects.all()
	return render(request,
                  'parse.html',
                  {'title': title})