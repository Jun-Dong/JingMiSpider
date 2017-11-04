from urllib.parse import urlencode

import requests
from lxml.etree import XMLSyntaxError
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq
import pymongo
from config import *

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

base_url = 'http://weixin.sogou.com/weixin?'

# 因为需要登录才能看到信息,所以构造字典,传入Cookie
headers = {
    'Cookie': 'SUV=000C6326DA11690A59DDD10671C7A993; IPLOC=CN4403; SUID=2CD3E9B75118910A0000000059F3E877; ABTEST=0|1509156986|v1; SNUID=CF360D52E5E0B8751AF266C8E5465C32; weixinIndexVisited=1; sct=2; JSESSIONID=aaa1HY6VWfvT-bjGwvv8v; ppinf=5|1509157574|1510367174|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1OkphZG9ufGNydDoxMDoxNTA5MTU3NTc0fHJlZm5pY2s6NTpKYWRvbnx1c2VyaWQ6NDQ6bzl0Mmx1TXBoMjhIM3hFcFhnWkl4bmdyR3R0VUB3ZWl4aW4uc29odS5jb218; pprdig=JoEUhTFSlO0VX_j9BiRijD7cDxSK7Mp-rEmLKRWlTJqvqmvGmG6J2ia3TVEUhisCCKYOKrRkXRCmGkVLUXzMzNxwojhLc9DjNSa5Ub0quKXR3eCwN1phbersxFA41SLEYQtrGI4G3qpeiZnZrZ021KIvIJWgHxgxbWcOczAQGU4; sgid=25-31662825-AVnz6sa35wqj1dicHvojhgCM; ppmdig=150915757500000065e49a86254f571a7433fbfbb9eaf8af',
    'Host': 'weixin.sogou.com',
    'Upgrade - Insecure - Requests': '1',
    'User - Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 61.0.3163.100Safari / 537.36'

}

proxy = None
MAX_COUNT = 5


def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None


def get_html(url, count=1):
    print('Crawling', url)
    print('Trying Count', count)
    global proxy
    if count >= MAX_COUNT:
        print('Tried Too Many Counts')
        return None
    try:
        # 如果有代理
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            # 因为有302判断,所以设置allow_redirects=False不让它自动处理跳转
            response = requests.get(url, allow_redirects=False, headers=headers)
        else:
            # 如果没使用代理,就用本机ip
            response = requests.get(url, allow_redirects=False, headers=headers)

        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            # Need Proxy
            print(302)
            proxy = get_proxy()
            if proxy:
                print('Using Proxy', proxy)
                return get_html(url)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError as e:
        print('Error Occurred', e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url, count)


def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html


def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')


def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None


def parse_detail(html):
    try:
        doc = pq(html)
        title = doc('.rich_media_title').text()
        content = doc('.rich_media_content').text()
        date = doc('#post-date').text()
        nickname = doc('#js_profile_qrcode > div > strong').text()
        wechat = doc('#js_profile_qrcode > div > p:nth-child(3) >span').text()
        return {
            'title': title,
            'content': content,
            'date': date,
            'nickname': nickname,
            'webchat': wechat

        }
    except XMLSyntaxError:
        return None


def save_to_mongo(data):
    if db['atrticles'].update({'title': data['title']}, {'$set': data}, True):
        print('Saved to Mongo', data['title'])
    else:
        print('Saved to Mongo Failed', data['title'])


def main():
    for page in range(1, 101):
        html = get_index(KEYWORLD, page)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                article_html = get_detail(article_url)
                if article_html:
                    article_data = parse_detail(article_html)
                    print(article_data)
                    if article_data:
                        save_to_mongo(article_data)


if __name__ == '__main__':
    main()
