from pprint import pprint as print
from bs4.element import SoupStrainer
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urlparse, urljoin
import re
import csv
import pandas as pd
url = 'https://xakep.ru/'
headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
           "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
           "sec-ch-ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
           "sec-ch-ua-mobile": "?0",
           "sec-ch-ua-platform": "\"Windows\"",
           "sec-fetch-dest": "document",
           "sec-fetch-mode": "navigate",
           "sec-fetch-site": "same-origin",
           "sec-fetch-user": "?1",
           "upgrade-insecure-requests": "1",
           "cookie": "_ga=GA1.2.737393603.1634229632; __gads=ID=8f33bcf4f46c6739:T=1634229641:S=ALNI_MamWgAseKX7uBYtPWn-A7fpsXAY1Q; _ym_uid=1634229749562852097; _ym_d=1634229749; wordpress_logged_in_95a2ce14874d444647baa643165aaf19=Doctor_wHo_Try%7C1637264911%7CrRX7rfJMO5U2cpBYsboiWgrCgyYJQGqYmCVrWg72aVY%7C080f019e9f45e3d770bef2f97b063c7c145d0e17095481cc29ab15ae2ed27b09; _gid=GA1.2.144395574.1636783796; _gat=1",
           "Referer": "https://xakep.ru/",
           "Referrer-Policy": "strict-origin-when-cross-origin"
           }

int_url = set()
ext_url = set()


def get_article(url):

    r = requests.get(url, headers=headers)
    article = dict()
    article['soup'] = BeautifulSoup(r.content, 'html.parser')
    article['title'] = article['soup'].title
    title = article['title']
    article['subscribe'] = False
    body = article['soup'].find(
        "div", id="content")
    if body:
        article['body'] = body.text
    else:
        article['body'] = None
    article['href'] = url
    if title:
        article['title'] = article['soup'].title.text
    else:
        article['title'] = None
    return article


def website_links(url):
    urls = set()
    if url:
        r = requests.get(url, headers=headers)
        article = dict()
        soup = BeautifulSoup(r.content, 'html.parser')
        body = soup.find(
            "div class", id="content")
        if body:
            article['body'] = body.text
        else:
            article['body'] = None
        article_hrefs = soup.find_all('a')
        for tag in article_hrefs:
            href = tag['href']
            urls.add(href)

    return urls


links = website_links(url)
int_links = []
visited_urls = 0


def checker(link):
    if not 'http' in link:
        int_links.append(link)
        links.remove(link)
    elif re.search('/issues', link):
        int_links.append(link)
        links.remove(link)

    return int_links


auto = []


def auto_det(link):
    if 'wp-admin' in link and 'http' in link:
        auto.append(link)
        links.remove(link)
    elif 'wp-login' in link and 'http' in link:
        auto.append(link)
        links.remove(link)
    return auto


for link in list(links):
    checker(link)
    auto_det(link)

u_links = []
links_l = list(links)


# def u(massiv):
#     for link in links_l:
#         massiv.append((get_article(link)))

#     return massiv


# linkss = u(u_links)

# for el in linkss:
#     del el['soup']
#     del el['body']
# records = []
# for el in linkss:
#     records.append(tuple(el.values()))

# print(records)

lin_d = []
rec = []

# for elem in int_links:
#     keyz = ['href', 'subscribe', 'title']
#     values = [elem, True, elem]
#     dic = dict(zip(keyz, values))
#     lin_d.append(dic)

# for el in lin_d:
#     rec.append(tuple(el.values()))
# print(rec)

for elem in auto:
    keyz = ['href', 'subscribe', 'title']
    values = [elem, True, elem]
    dic = dict(zip(keyz, values))
    lin_d.append(dic)

for el in lin_d:
    rec.append(tuple(el.values()))
    print(rec)
