import time
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

address = 'https://www.cars.com/for-sale/searchresults.action/?&zc=18974&rd=30&stkTypId=28881&searchSource=RESEARCH_SHOP_INDEX'

#using pythons built-in request engine to get the site
page_html = uReq(address).read()
page_soup = BeautifulSoup(page_html, 'html.parser')
#print(page_soup.prettify())

option_tags = page_soup.find_all('div')
for tag in option_tags:
    print(tag,
          #tag.name,
          tag.attrs,
          #tag.text,
          sep='\n',end='\n\n')

#for i in page_soup.find_all('option'):
    #print(i)




