import xml.dom.minidom
import urllib.request

def main():

    webUrl = urllib.request.urlopen("https://www.docker.com/blog/feed/")
    responseCode = webUrl.getcode()

    if (responseCode == 200 ):
        data = webUrl.read()

        doc = xml.dom.minidom.parseString(data)

        print(doc.nodeName)
        print(doc.firstChild.tagName)

        site = doc.getElementsByTagName("site")

        newItenDom = doc.createElement("skill")
        newItenDom.setAttribute("name", "Python")

        site.append(newItenDom)

        if site != None and site.length > 0:
            for childNodes in site:
                print(childNodes.getAttribute("xmlns"))

if __name__ == "__main__":
    main()