
import urllib.request
import json

def main():
    webUrl = urllib.request.urlopen("http://newsapi.org/v2/everything?q=docker&from=2020-02-01&sortBy=published&apiKey=46e1510b7ff94efcad3ef49517d2fd0b")
    responseCode = webUrl.getcode()

    if (responseCode == 200 ):
        data = webUrl.read()
        print("result code : " + str( webUrl.getcode()  ) )
        try:
            theJsonObject = json.loads(data)
            articles = theJsonObject["articles"]
            for article in articles:
                if article != None:
                    source = article["source"]
                    print( article["author"] if(article["author"] != None) else "" )            
                    print( article["title"] if (article["title"] != None) else "" )
                    print( article["url"] if (article["url"] != None) else "")
                    print( article["urlToImage"] if (article["urlToImage"] != None) else "")
                    print( article["content"] if (article["content"] != None) else "")
                    print( article["description"] if (article["description"] != None) else "")
                    print( source["name"] if (source["name"] != None)  else "" )
                    print("\n-----------------------------------------------------------------------------\n")
        except ValueError as e:
            print("Json data has sintax error")
    else:
        print("Response error " + str(responseCode) )
 
if __name__ == "__main__":
    main()