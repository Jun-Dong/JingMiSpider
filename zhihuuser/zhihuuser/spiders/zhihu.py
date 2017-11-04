# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Spider, Request

from zhihuuser.items import UserItem


class ZhihuSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    start_user = 'excited-vczh'

    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'

    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    #start_requests:做了三件事
    #1.获取自己本身的基本信息,请求parse_user,请求关注列表,请求粉丝列表
    def start_requests(self):
        yield Request(self.user_url.format(user=self.start_user, include=self.user_query), self.parse_user)
        yield Request(self.follows_url.format(user=self.start_user, include=self.follows_query, offset=0, limit=20), callback=self.parse_follows)
        yield Request(self.followers_url.format(user=self.start_user, include=self.followers_query, offset=0, limit=20), callback=self.parse_followers)

    # 解析详细信息赋值给item,得到有用的信息,分别获取关注列表和粉丝列表,进行下一步的递归调用
    def parse_user(self, response):
        # 返回用户信息
        # JSON对象
        result = json.loads(response.text)
        item = UserItem()
        # 以集合返回item的所有名称(即Field())
        for field in item.fields:
            # 如果这个属性属于返回结果,我们就对它进行赋值
            if field in result.keys():
                item[field] = result.get(field)
        yield item

        yield Request(self.follows_url.format(user=result.get('url_token'), include=self.follows_query, limit=20, offset=0), self.parse_follows)
        yield Request(self.followers_url.format(user=result.get('url_token'), include=self.followers_query, limit=20, offset=0), self.parse_followers)

    #1.解析关注列表,获取每个用户的url_token,再重新对用户发起请求,解析用户信息,进行递归调用
    #2.递归分页
    def parse_follows(self, response):
        # 做2件事情:
        # 1.解析follows列表,获得关注列表的信息,重新请求pare_user
        # 2.翻页,
        results = json.loads(response.text)
        # 用户关注列表的解析,(获取url_token)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query), self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, self.parse_follows)

    # 1.解析关注列表,获取每个用户的url_token,再重新对用户发起请求,解析用户信息,进行递归调用
    # 2.递归分页
    def parse_followers(self, response):
        # 做2件事情:
        # 1.解析follows列表,获得关注列表的信息,重新请求pare_user
        # 2.翻页,
        results = json.loads(response.text)
        # 用户关注列表的解析,(获取url_token)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query), self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, self.parse_followers)
