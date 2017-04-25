import os
import sys
import requests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Saya.settings')

import django
import random
from Foodie.models import Category, Page

#### FOOD for thought: 
#### pass user input link for auto API generate. ....
#### fix main function take in 1 argument as arg[1]
#### if stament : take arg[1] eles .... generic link. 

def populate1(link):
	print "Here we go "
	#### need to change this to  actual GET function from API. NOT DATABASE>.....
	if link is None:
		link = 'https://apibaas-trial.apigee.net/melaniewoe/sandbox/woegasstations'
	fullMenu =requests.get(link)
	fullMenu = fullMenu.json()
	catList = set()

	for item in fullMenu['entities']:
		catList.add(item['store'])
	for cat in catList:
		for item in fullMenu['entities']:
			cat1 = add_cat(cat)
			if cat == item['store']:
				if cat =='gas':
					add_page(category = cat1, 
							name = item['name'],
							views = 0,
							midprice = item['midprice'],
							premiumprice = item['premiumprice'],
							regularprice = item['regularprice'],
							special= (x.encode('UTF8') for x in item['special']),
							address = item['address'],
							)
				else : 
					add_page(category = cat1, 
							name = item['name'],
							views = 0,
							midprice = None,
							premiumprice = None,
							regularprice = None,
							special= item['special'],
							address = item['address'],
							)
					
def printResult ():
	for c in Category.objects.all():
		for p in Page.objects.filter(category =c):
			print " - {0} - {1}". format(str(c), str(p))

def add_page(category, name,views, midprice, premiumprice, regularprice,special,address):
	p = Page.objects.get_or_create(category=category, name=name, special = special, address =address)[0]
	p.views=views
	p.midprice = midprice
	p.premiumprice = premiumprice
	p.regularprice = regularprice
	p.save()
	return p

def add_cat(name):
	if (Category.objects.filter(name =name).exists()):
		c=Category.objects.get(name=name)

	c= Category.objects.get_or_create(name= name)[0]
	c.save()
	return c

if __name__ == '__main__':
	print "Start populating script ..."
	
	populate1(link)
	#printResult()

