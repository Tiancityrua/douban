import requests
from bs4 import BeautifulSoup
url='https://movie.douban.com/top250'

def downloadpage(url):
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
    }
    data=requests.get(url,headers=headers).text
    return data
def parsehtml(html,movielist=[]):

    soup=BeautifulSoup(html,'lxml')
    souplist=soup.find('ol',attrs={'class':'grid_view'})
    for li in souplist.find_all('li'):
        detail=li.find('div',attrs={'class':'hd'})
        moviename=detail.find('span',attrs={'class':'title'}).getText()
        movielist.append(moviename)
    nextpage=soup.find('span',attrs={'class':'next'}).find('a')
    if nextpage:
        parsehtml(downloadpage(url+nextpage['href']),movielist)
    return movielist

def main():
    a=parsehtml(downloadpage('https://movie.douban.com/top250'))
    with open('movie.txt','w') as f:
        for aa in a:
            f.write(aa+'\n')
if __name__ == '__main__':
    main()
