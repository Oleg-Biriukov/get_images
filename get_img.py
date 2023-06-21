from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, URLError
from tqdm import tqdm
import requests
import string
import random
import time 

tag_f=open('tags.txt', 'a+')
tags=tag_f.read().split('\n')

HEADER={
	'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
}
ZN=6
statistics={}

def binary_search(list, item):
    low=0
    high=len(list)-1

    while low < high:
        mid=(low+high)
        guess = list[mid]   
        if guess == item:
            return mid
        if guess > item:
            high=mid - 1
        else:
            low = mid+1
    return None

def proverka(copy):
    #2

    if binary_search(tags, copy) == None:
        pass
    else:

        copy=randomStringDigits(ZN)
    return copy

def unpacking(d, quantity):
	if d is not {}:
		for i in d: print(d[i])
	time.sleep(10)

def randomStringDigits(zn):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(zn))

def get_urlopen(url, num):
	try:
		img = urlopen(Request(url, headers=HEADER)).read()
	except ValueError:
		return False
	out = open(f"images/img{num+1}.jpg", "wb")
	out.write(img)
	out.close
	return True

def get_url_img(url, i):
	r=requests.get(url, headers=HEADER)
	soup=BeautifulSoup(r.text, 'html.parser')
	try:
		url_img=soup.find('div', class_='image-constrain js-image-wrap').find('img', class_='no-click screenshot-image')
	except Exception as e:
		return ['//st.prntscr.com/2021/02/09/0221/img/0_173a7b_211be8ff.png',False]
	return [url_img['src'], r]

def main():
	if len(tags) >= 1947792:
		tag_f = open("tags.txt", "w")
		tag_f.close()
		return 0
	quantity=int(input('Input Quantity Images==> '))
	for i in tqdm(range(quantity)):
		try:
			tag = randomStringDigits(ZN)
			url_main = f"https://prnt.sc/{proverka(tag)}"
			img_scr=get_url_img(url_main, i)
			urlop=get_urlopen(img_scr[0], i)
			tag_f.write(tag+'\n')		
			statistics[i]=f'{False if urlop == False or img_scr[1] == False else True }, {img_scr[1]}'
		except Exception as e:
			quantity += 1
			continue
	otvet=input('Do you want see statistics ?(<Yes> or <No>) ==> ' )
	if otvet == 'Yes':
		unpacking(statistics, quantity)	
	
if __name__ == '__main__':
	main()

tag_f.close()