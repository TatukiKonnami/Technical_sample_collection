import requests
from bs4 import BeautifulSoup
import re
class ScraoingPage():

    def __init__(self, url):
        self.url = url 

    def get_soup(self):
        try:
            url = requests.get(self.url)
            self.soup = BeautifulSoup(url.content, "html.parser")
            return True
        except Exception as e:
            return False

    def is_soup(self):
        return self.soup is not None

    def get_html(self):
        if self.is_soup():
            return soup.prettify()
        else:
            return ''

    def get_title(self):
        if self.is_soup():
            return soup.title.string
        else:
            return '' 

    def get_tag(self, tag):
        if self.is_soup():
            return soup.find_all(tag)
        else:
            return '' 

    def get_class(self, className):
        if self.is_soup():
            return soup.find_all(class_=className)
        else:
            return '' 
    
    def get_class_and_tag(self, tag, className):
        if self.is_soup():
            return soup.find_all(tag, class_=className)
        else:
            return ''       

    def get_id(self, idName):
        if self.is_soup():
            return soup.find_all(id=idName)
        else:
            return ''   

def main():
    urlName = ""
    scraoing = ScraoingPage(urlName)
    scraoing.get_soup()
    print(scraoing.get_html())
    print(scraoing.get_title())
    a_items = scraoing.get_tag('a')
    for item in a_items:
      print (item)
    class_items = scraoing.get_class('test class')

if __name__ == '__main__':
    main()
    