import selenium_base
from selenium_base import Page

class Crawling():
    def __init__(self,website):
        self.website = website
    
    def page_build(self):
        page = Page(self.website)
        return page
    

cr = Crawling()
page = cr.page_build()
page.perform()
        