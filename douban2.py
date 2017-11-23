import requests
from bs4 import BeautifulSoup
import codecs
URL='https://movie.douban.com/top250'

def downloadpage(url):
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
    }
    data=requests.get(url,headers=headers).text
    return data
def parsehtml(html):
    movelist=[]
    soup=BeautifulSoup(html,'lxml')
    souplist=soup.find('ol',attrs={'class':'grid_view'})
    for li in souplist.find_all('li'):
        detail=li.find('div',attrs={'class':'hd'})
        moviename=detail.find('span',attrs={'class':'title'}).getText()
        movelist.append(moviename)
    nextpage=soup.find('span',attrs={'class':'next'}).find('a')
    if nextpage:
        return movelist,URL+nextpage['href']
    return movelist,None

def main():
    url=URL
    with codecs.open('movies.txt','wb',encoding='utf-8') as fp:
        while url:
            html=downloadpage(url)
            movies,url=parsehtml(html)
            fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))
if __name__ == '__main__':
    main()
