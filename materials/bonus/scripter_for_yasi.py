import urllib.request
import re
from bs4 import BeautifulSoup
# scripter for norvel book<<fanren xiuxian>> by using beautifulSoup.
def load_page(page):
    #url = "http://www.51pigai.com/tofel-essay?s=0&y=0&t=18&p="+str(page)
    url = "http://www.51pigai.com/ielts-essay?s=0&y=0&t=71&p=" + str(page)
    #url = url + str(page) + '.html'
    webPage = urllib.request.urlopen(url)
    data = webPage.read()
    return data
def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False
if __name__ == "__main__":
    # get web page
    fp = open('yasi.txt', 'w', encoding='utf-8')
    for page in range(1):
        data=load_page(page)

        try:
            data = data.decode('utf-8')#utf-8  GB2312 GBK
                # write to file
            soup = BeautifulSoup(data, 'html.parser')
                # print(soup.prettify())
            tag=soup.find_all('ul')
            tag2=tag[3].find_all('li')
            pages = soup.find('div', attrs={"class": "page ft14 tac fl"}).find_all('a')
            max_pages=int(pages[-2].get_text())
            index=0
            for kk in range(max_pages):
                if index>0:
                    data = load_page(kk)
                    data = data.decode('utf-8')  # utf-8  GB2312 GBK
                    # write to file
                    soup = BeautifulSoup(data, 'html.parser')
                    # print(soup.prettify())
                    tag = soup.find_all('ul')
                    tag2 = tag[3].find_all('li')
                index+=1
                for i in range(len(tag2)):
                    page=tag2[i]['qid']
                    title=tag2[i].find('a')['title']
                    data2=tag2[i].find('a')['href']
                    #index=data2.find('independent')+16
                    #time=data2[index:-1]+data2[-1]
                    #index=data2.find('independent')+12
                    time=data2[-8:-1]+data2[-1]
                    if int(time[0:4])>=2015:
                        new_web = 'http://www.51pigai.com/act/essay?qid='+page
                        webPage = urllib.request.urlopen(new_web)
                        new_data = webPage.read()
                        new_data = new_data.decode('utf-8')  # utf-8  GB2312 GBK
                        new_soup = BeautifulSoup(new_data, 'html.parser')
                        content2=new_soup.find('div',attrs={"class": "dt_bx1 ft14"}).find_all('p')
                        fp.write(time+':\n')
                        for j in range(len(content2)):
                            sub_content=str(content2[j].get_text())
                            if check_contain_chinese(sub_content)==False:
                                sub_content = re.sub('\r\n\t|\r\n|</p>|\[|\]|<p>|\'|\n', ' ', sub_content)
                                sub_content.encode('utf-8')
                                fp.write(sub_content)
                        fp.write('\n\n')
        except:
                 pass
    fp.flush()
    fp.close()