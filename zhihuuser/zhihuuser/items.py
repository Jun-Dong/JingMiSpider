# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    name = Field()
    avatar_url = Field()
    headline = Field()
    description = Field()
    url = Field()
    url_token = Field()
    gender = Field()
    cover_url = Field()
    type = Field()
    badge = Field()
