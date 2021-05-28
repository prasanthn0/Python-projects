

from pages.quotes_page import QuotesPage

import requests


#quotes.toscrape.com

page_content= requests.get('http://quotes.toscrape.com').content

page=QuotesPage(page_content)

for quote in page.quotes:
    print(quote)
    print(quote.content)
    print(quote.author)




