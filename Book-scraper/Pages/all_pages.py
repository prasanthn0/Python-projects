from bs4 import BeautifulSoup
import re
import logging
from locators.all_books_page import AllBooksPageLocator
from parsers.book_parser import BookParser


logger=logging.getLogger('scraping.all_pages')

class AllBooksPage:
    def __init__(self,page_content):
        logger.debug('Getting contents of the page with BeautifulSoup HTML parser')
        self.soup=BeautifulSoup(page_content,'html.parser')

    @property
    def books(self):
        logger.info(f'Getting all books using `{AllBooksPageLocator.BOOKS}`. ')
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocator.BOOKS)]


    @property
    def page_num(self):
        content=self.soup.select_one(AllBooksPageLocator.PAGER).string
        logger.info(f'Found number of catalogue pages `{content}`')
        pattern='Page [0-9]+ of ([0-9]+)'
        matcher=re.search(pattern,content)
        pages=int(matcher.group(1))
        return pages


        
