"""

Try to extract the same information (a tuple of quote, author, and tags) from https://quotes.toscrape.com/

Links to an external site. as we did with Beautiful soup.

At this time, you need to do it with 2 different modules.

1. Seleium

2. Scrapy

For each module, provide a code and capture of the execution result."""
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from scrapy.crawler import CrawlerProcess

SCRAPE_URL = 'https://quotes.toscrape.com/'

ff_options = Options()
ff_options.add_argument("--headless") # wont open a GUI browser window

    # Selenium
driver = webdriver.Firefox(options=ff_options)     # set our webscraper to use my default browser (firefox)
driver.get(SCRAPE_URL)           # have selenium open a browser and navigate to the URL

# Extracting the data
# Qoutes from this website are held in a <span> tag with class="text"
# we will scrape all span tags on this page with that class name
selenium_qoutes_elements = driver.find_elements(By.CSS_SELECTOR, '.quote') # getting every qoute object (text, author, etc.)

qoute_dict = dict()

# creating a dict of qoutes by author
for q_element in selenium_qoutes_elements:
    qoute = q_element.find_element(By.CLASS_NAME, 'text').text  # text of the qoute
    author = q_element.find_element(By.CLASS_NAME, 'author').text # author of the qoute

    # if author exists, append qoute to their list of qoutes (stored in value)
    if author in qoute_dict:
        qoute_dict[author].append(qoute)
    else:   # otherwise create a new k,v pair and add the author
        qoute_dict[author] = [qoute]


# printing the qoutes
print("-------------- Selenium --------------")

for author,qoutes in qoute_dict.items():
    for q in qoutes:
        print(f'\n{ q }\n\t--{ author }')

# ------------------ Scrapy ------------------
"""This class will be passed to scrapy crawler to be used internally"""
class QouteCrawler(scrapy.Spider):
    name = "qoutes"

    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    # standard implementation of scrapy parse function to be used in the script
    def parse(self, response):
        for qoute in response.css('div.quote'):
            item = {
                'text': qoute.css('span.text::text').get(),
                'author': qoute.css('small.author::text').get(),
                'tags' : qoute.css('div.tags a.tag::text').getall()
            }

            # printing the qoutes
            print(f"\n{ item['text'] }\n\t--{ item['author'] }")
            yield item  # lazy-evaluation technique, doesnt invoke the above stuff until scrapy is ready to get the data

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 ...',  # You can customize the user agent
    'LOG_LEVEL': 'WARNING',  # dont output anything except warnings and the stuff we want
    'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7', # this was giving me an issue so i had to specify
})

print("\n\n-------------------- Scrapy --------------------")
process.crawl(QouteCrawler)
process.start()