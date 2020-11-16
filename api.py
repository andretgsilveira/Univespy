from urllib.request import urlopen
from html.parser import HTMLParser

def getSource(url):
    response = urlopen(url)
    html = response.read()
    return html.decode()


html = getSource('https://www.uol.com.br')

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])

    '''def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)'''

    '''def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)'''

parser = MyParser()
parser.feed(html)