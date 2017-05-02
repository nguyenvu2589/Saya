# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from Foodie.models import Category
from Foodie.models import Page
from Foodie.form import CategoryForm
from Foodie.form import PageForm 
from Foodie.form import UserForm, UserProfileForm
from django.shortcuts import render
import requests
from populate import populate1
from geopy.geocoders import Nominatim


import json

# working on item.special
### try to convert from unicode to list. 
### might need some picture
def index(request):
	context_dict = {}

	#a =requests.get('http://nguyenvu2589-test.apigee.net/hw5/movie')
	#b = a.json()
	page_list = Page.objects.all()
	store = Category.objects.all()

	###########avg price
	avg_reg_price = []
	for item in page_list:
		if str(item.category) == 'gas':	
		 	avg_reg_price.append(item.regularprice)

	avg_reg_price_result = round(sum(avg_reg_price)/len(avg_reg_price),2) 
	print avg_reg_price_result


	avg_prem_price = []
	for item in page_list:
		if str(item.category) == 'gas':
			avg_prem_price.append(item.premiumprice)

	avg_prem_price_result = round(sum(avg_prem_price)/len(avg_prem_price),2)

	avg_mid_price = []
	for item in page_list:
		if str(item.category) == 'gas':
			avg_mid_price.append(item.midprice)

	avg_mid_price_result = round(sum(avg_mid_price)/len(avg_mid_price),2)

	############min price
	reg_price = []
	for item in page_list:
		if str(item.category) == 'gas':
			if str(item.regularprice) != 'None':
		 		reg_price.append(item.regularprice)
	min_reg_price = min(reg_price)
	print min_reg_price

	

	context_dict = {'store': store, 'pages': page_list, 'average_reg_price': avg_reg_price_result, 'average_prem_price': avg_prem_price_result, 'average_mid_price': avg_mid_price_result}

	return render(request, 'Saya/index.html', context_dict)

def contact(request):
	context_dict = {}

	
	return render(request, 'Saya/contact.html', context_dict)

def get_location():
	send_url = 'http://freegeoip.net/json'
	r = requests.get(send_url)
	j = json.loads(r.text)
	lat = j['latitude']
	lon = j['longitude']
	return float(lat),float(lon) 

def privacy(request):
	context_dict = {}

	return render(request, 'Saya/privacy.html', context_dict) 

def about(request):
	context_dict = {}
	
	return render(request, 'Saya/about.html', context_dict) 
def location(request):
	context_dict = {}
	local = []
	geolocator = Nominatim()
	page_list = Page.objects.all()
	for item in page_list:
		l = geolocator.geocode(item.address)
		local.append(l)

	lat,lon = get_location()
	page = zip(page_list,local)
	context_dict = {'pages':page, 'lat':lat, 'lon':lon}
	
	return render(request, 'Saya/location1.html', context_dict)


def special(request):
	context_dict = {}
	page_list = Page.objects.all()[:5]

	for item in page_list:
		item.special = item.special.split("!")
	lat, lon = get_location()
	context_dict= {'pages':page_list,'lat':lat, 'lon': lon }

	return render(request, 'Saya/special_offer.html', context_dict)

def page(request, page_name_slug):

	context_dict ={}
	try:
		print (page_name_slug)
		page =Page.objects.get(slugP = page_name_slug)
		context_dict['item'] = page

		page.special = page.special.split("!")

	except Page.DoesNotExist:
		print "cant find this page."

	return render(request, 'Saya/page.html', context_dict)

# DONE !!!!
def upload(request):
	context_dict = {}
	
	if request.method == 'POST':
		link = request.POST
		if 'http' in link['APIlink']:
			populate1(link['APIlink'])
		else:
			return HttpResponse("It's not a link....!!!")

	return render(request, 'Saya/upload.html', context_dict)