import requests
from bs4 import BeautifulSoup,SoupStrainer
import time

h={
	"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

def find_price(URL):
	res=requests.get(URL,headers=h)
	s=BeautifulSoup(res.content,'html.parser')
	price=s.find("div",{"class":"_1vC4OE _3qQ9m1"})
	title1=s.find("span",{"class":"_2J4LW6"})
	title2=s.find("span",{"class":"_35KyD6"})
	if title1 is not None:
		print(title1.get_text())
	if title2 is not None:
		print(title2.get_text())
	if price is not None:
		pricet=price.get_text()
		print("the current price is"+pricet)
		ll=int(len(pricet))
		pricekk=pricet[1:ll]
		pricel=int(pricekk.replace(",",""))
		print(price.get_text())
	return pricel

def track():
	price=int(input("enter the price lim:"))
	if find_price(input("enter the url of the item you want to purchase:"))<price:
		print("Price is low go for the purchase")
	else:
		print("Price is still high, please wait for purchase")


track()
time.sleep(24*60*60)#updates for everyday
