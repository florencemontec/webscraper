from django.shortcuts import render
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from scraper.models import Lotto

def home(request):
	lotto_url = 'https://lottonijuan.com/pcso/642-lotto-result/page/1/'
	url = lotto_url
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	div_result = soup.find_all('div', class_='front-view-content full-post')
	lotto_result = []
	for result in div_result:
		lotto = result.p.text
		lotto_result.append(lotto)
	return render(request, 'scraper/home.html', {'lotto_result': lotto_result})
