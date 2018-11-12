import requests
from requests.exceptions import RequestException
import re
import time
import json
import os
import sys
import urllib.request
def get_one_photo(url):
	try:
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
		response = requests.get(url,headers = headers)
		if response.status_code==200:
			return response.text
		return None
	except  RequestException:
		return None
def  parse_onr_photo(html):
	pattern = re.compile('data-original="(.*?)" alt=',re.S)
	items = re.findall(pattern,html)
	return items

def main(offest):
	url = 'http://www.win4000.com/meinvtag4_'+str(offest)+'.html'
	html=get_one_photo(url)
	lml = parse_onr_photo(html)
	path = 'E:\\图片'
	x = 1
	for item in lml:
		pathnew = path + '//妹儿'+str(offest)+str(x) + '.jpg'
		urllib.request.urlretrieve(item,pathnew)
		x=x+1
if __name__=='__main__':
	for i in range(1,6):
		main(i)
		time.sleep(1)