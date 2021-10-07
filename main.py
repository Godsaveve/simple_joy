import requests
import lxml
from bs4 import BeautifulSoup
import re
from requests.api import get


def search_tags(search):#поиск тегов
    fsearch = re.sub(" ", "+",search)
    search_list = requests.get("http://joyreactor.cc/search?q="+fsearch)
    soup = BeautifulSoup(search_list.text, "html.parser")
    quotes = soup.find_all('div', class_="blog_pic_result")
    tag_list = []
    for i in range(len(quotes)):
        tag_list.append(quotes[i].find("a", href=True)["href"])
    return tag_list

def pages_list(link): # количество страниц
    html_doc = requests.get(link)
    soup = BeautifulSoup(html_doc.text, "html.parser")
    quotes = soup.find('div', class_="pagination_expanded")
    page_num = quotes.find("span", class_="current").text 
    if page_num == '1':
        lem = quotes.find_all("a", class_="")
        page_num = len(lem)
        return page_num
    else:
        return int(page_num)

def get_pic_links(link,number_pages = 1):# получение ссылок на картинки с одной страницы
    html_doc = requests.get(link)
    soup = BeautifulSoup(html_doc.text, "html.parser")
    quotes = soup.find_all('div', class_="image")
    pic_link = []
    for i in range(len(quotes)):
        if quotes[i].img:
           pic_link.append(quotes[i].img['src'])
    return pic_link

def get_pic_links_pages(link,pages_count=2):
    pl = pages_list(link)
    pic_link = []
    for i in  range(0,pages_count):
        page = str(pl-i)
        link_new = link+page
        pic_link = pic_link + get_pic_links(link_new)
    return pic_link

def post_pic(link):
    pic_list = get_pic_links(link)
    s = len(link)
    links = []
    return links

pic = 'http://joyreactor.cc/'
p = post_pic(pic)
for i in range(0,len(p)):
    print(p[i])
print(len(p))

