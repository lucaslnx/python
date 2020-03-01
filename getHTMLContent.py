import urllib.request
import html
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def run(self):
        print("running")
    
    def handle_comments(self,data):
        #print("data : " + data)
        pos = self.getpos()
        print("post " + str(pos[0]), "  ", str(pos[1]) )
        
    def handle_starttag(self, tag, attrs):
        if tag.isspace():
            return False
        pos = self.getpos()
        print("post " + str(pos[0]), "  ", str(pos[1]) )

        if attrs.__len__() > 0:
            for a in attrs:
                print( a[0], "=>", a[1] )

    def handle_endtag(self, tag):
        if tag.isspace():
            return False
        pos = self.getpos()
        print("post " + str(pos[0]), "  ", str(pos[1]), " =>",  tag[ pos[1]: 5 ] )

    def handle_data(self, data):
        if data.isspace():
            return False
        pos = self.getpos()
        print("post " + str(pos[0]), "  ", str(pos[1]) )

def main():
    webUrl = urllib.request.urlopen("https://www.uol.com")
    responseCode = webUrl.getcode()

    if (responseCode == 200 ):
        webHTMLData = webUrl.read()

        webHTMLData = str(webHTMLData)

        if isinstance(webHTMLData, str) and len(webHTMLData) > 0:
            #print(webHTMLData)
            parser = MyHTMLParser()
            parser.feed(webHTMLData)

if __name__ == "__main__":
    main()