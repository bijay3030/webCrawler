from html.parser import HTMLParser
from urllib import parse

#we need base url and page url
#super is using the main function of class
class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    #handle starttag will fetch the starttag of the html
    #a tag contain href and url will join the baseurl with page url  by taking value of attribute
    #that url will be added to self .links set
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

#it gonna return the self.links set
    def page_links(self):
        return self.links

    def error(self, message):
        pass
