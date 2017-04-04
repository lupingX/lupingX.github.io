import urllib.request
import re
from bs4 import BeautifulSoup
# scripter for norvel book<<fanren xiuxian>> by using beautifulSoup.
def load_page(page):
    url = "http://m.shushu8.com/book/frxxz/"
    url = url + str(page) + '.html'
    webPage = urllib.request.urlopen(url)
    data = webPage.read()
    return data

if __name__ == "__main__":
    # get web page
    fp = open('fanren.txt', 'w', encoding='utf-8')
    for i in range(1504,2449):
        data=load_page(i)
        try:
            data = data.decode('GBK')
            # write to file
            soup = BeautifulSoup(data, 'html.parser')
            # print(soup.prettify())
            tag=soup.find('div',id='content')
            title=soup.find('h1',id='nr_title').string
            a=str(tag)
            # print(a)
            a=re.sub('<br>|<br/>|</br>|</div>',' ',a)
            a=re.sub('<div id="content">',' ',a)
            # print(b)
            a.encode('utf-8')
            title.encode('utf-8')
            # print(a)
            fp.write('\n'+title+'\n')
            fp.write(a)
        except:
            pass
    fp.flush()
    fp.close()