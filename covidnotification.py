from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyme(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon =r"C:/Users/heemangi/Desktop/covidnotifier/cov.ico",
        timeout=3
    )
def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    #notifyme("Dear User"," Let's stop the spread of coronavirus together")
    myHtmldata=getData("https://www.mohfw.gov.in/")

    print (myHtmldata)
    soup=BeautifulSoup(myHtmldata,'html.parser')
    #print(soup.prettify())
    mydatastr = ""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        #print(tr.get_text())
        mydatastr += tr.get_text()
    mydatastr= mydatastr[1:]
    itemlist=mydatastr.split("\n\n")

    states = ['Uttar Pradesh','Karnataka','West Bengal']
    for item in itemlist[0:35]:
        #print(item.split('\n'))
        datalist= item.split('\n')
        if datalist[1] in states:
            print(datalist)
            ntitle='Cases of Covid-19'
            ntext=f"State {datalist[1]}\nIndian:{datalist[2]} and Foreign:{datalist[3]}\nCured:{datalist[4]}\nDeaths:{datalist[5]}"
            notifyme(ntitle,ntext)
            time.sleep(5)
    time.sleep(20)