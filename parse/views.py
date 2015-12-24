from django.shortcuts import render
from datetime import datetime
# Create your views here.

import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from parse.models import News
import json
import sqlite3 as lite

sql = "insert into NewsDB(title, content) values(?, ?)"
dellete = "DELETE FROM NewsDB"


def hello_world(request):

    return HttpResponse("Hello World!")


def parse(request):
    # get all the posts
	res = requests.get ("https://news.google.com.tw/news/section?pz=1&ned=tw&topic=n&siidp=6ad8de07654b451fe8d2bb5fecb5c32affe3&ict=ln&sdm=EXPANDO&authuser=0")

	soup = BeautifulSoup (res.text, "html.parser")
	#title =[]
	

	#initialize table
	con = lite.connect('db.sqlite3')
	cur = con.cursor()
	cur.execute (dellete)


	for item in soup.select('.esc-body'):
		#News.objects.create(title = item.select('span')[0].text.encode('utf-8'))
		#title.append(item.select('span')[0].text)
		#title.append(json.dumps(item.select('span')[0].text,ensure_ascii=False))
		tt = json.dumps(item.select('span')[0].text,ensure_ascii=False)
		#News.objects.create(title = 'tt')
    	#news_list = News.objects.all()

    	
		#photo = json.dumps(item.select('img')[0].text,ensure_ascii=False)
		content = json.dumps(item.select('.esc-lead-snippet-wrapper')[0].text,ensure_ascii=False)
		#source = json.dumps(item.select('.esc-thumbnail-image-wrapper')[0].text,ensure_ascii=False)
		data = [tt, content]
			
    	#add to database
		cur.execute (sql, data)

		#News.objects.create(title = tt, content = content)
	
	con.commit()
	
	#news_list = NewsDB.objects.all()

	con.close()

	#return HttpResponse('Hi')

	return render(request,
                  'parse.html',
                 )

def home(request):
    # get all the posts

	news_list = NewsDB.objects.all()

	return render(request,
					'parse.html',
					{'news_list': news_list})



