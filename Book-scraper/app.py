
#books.toscrape.com


import requests
import logging
from pages.all_pages import AllBooksPage


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                            datefmt='%d-%m-%Y %H:%M:%S',
                            level=logging.DEBUG,
                            filename='logs.txt')

logger=logging.getLogger('scraping')

logger.info('Loading the books list.....')

page_content=requests.get('http://books.toscrape.com').content

page=AllBooksPage(page_content)

books=page.books

for book in books:
    pass
    #print(book)


#if there are multiple pages : toscrape.com/catalogue/page-2 etc..

for page_num in range(1,page.page_num):  #page 0 has different URL without page-0
    url=f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content=requests.get(url).content
    page=AllBooksPage(page_content)
    books.extend(page.books)
