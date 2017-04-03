#!/usr/bin/env python
# _*_ coding: utf-8_*_
#
# Copyright 2016 planc2c.com
# thomas@time2box.com
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.web
import logging
import time
import sys
import os
import uuid
import smtplib
import json as JSON # 启用别名，不会跟方法里的局部变量混淆
from bson import json_util
import re

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../dao"))

from comm import *
from global_const import *


class WxHomeHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)

        self.redirect("/wx/clubs/"+CLUB_ID+"/index")


class WxIndexHandler(tornado.web.RequestHandler):
    def get(self, club_id):
        logging.info(self.request)
        logging.info("got club_id %r--------", club_id)

        tab = self.get_argument("tab", "1")
        logging.debug("get tab=[%r] from argument", tab)

        # club
        url = "http://api.7x24hs.com/api/clubs/"+club_id
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        club = rs['rs']

        self.render('wx/index.html',
                club=club,
                tab=tab)


class WxBlogHandler(tornado.web.RequestHandler):
    def get(self, club_id):
        logging.info(self.request)
        logging.info("got club_id %r--------", club_id)

        # club
        url = "http://api.7x24hs.com/api/clubs/"+club_id
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        club = rs['rs']

        # articles
        params = {"filter":"club", "club_id":club_id, "status":"publish", "idx":0, "limit":10}
        url = url_concat("http://api.7x24hs.com/api/articles", params)
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        articles = rs['rs']
        for article in articles:
            article['publish_time'] = timestamp_friendly_date(article['publish_time'])
        logging.info("got articles=[%r]", articles)

        self.render('wx/blog.html',
                club=club,
                articles=articles)


class WxProductIndexHandler(tornado.web.RequestHandler):
    def get(self, club_id):
        logging.info(self.request)
        logging.info("got club_id %r--------", club_id)

        # club
        url = "http://api.7x24hs.com/api/clubs/"+club_id
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        club = rs['rs']

        # articles
        params = {"filter":"club", "club_id":club_id, "status":"publish", "idx":0, "limit":10}
        url = url_concat("http://api.7x24hs.com/api/articles", params)
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        articles = rs['rs']
        for article in articles:
            article['publish_time'] = timestamp_friendly_date(article['publish_time'])
        logging.info("got articles=[%r]", articles)

        self.render('wx/products.html',
                club=club,
                articles=articles)


class WxMultimediaIndexHandler(tornado.web.RequestHandler):
    def get(self, club_id):
        logging.info(self.request)
        logging.info("got club_id %r--------", club_id)

        # club
        url = "http://api.7x24hs.com/api/clubs/"+club_id
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        club = rs['rs']

        # multimedia
        params = {"filter":"club", "club_id":club_id, "idx":0, "limit":20}
        url = url_concat("http://api.7x24hs.com/api/multimedias", params)
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        multimedias = rs['rs']
        for multimedia in multimedias:
            multimedia['publish_time'] = timestamp_friendly_date(multimedia['publish_time'])

        self.render('wx/multimedias.html',
                club=club,
                multimedias=multimedias)


class WxArticleHandler(tornado.web.RequestHandler):
    def get(self, club_id, article_id):
        logging.info(self.request)
        logging.info("got article_id %r in uri", article_id)

        # club
        url = "http://api.7x24hs.com/api/clubs/"+club_id
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        club = rs['rs']

        # update read_num
        url = "http://api.7x24hs.com/api/articles/"+article_id+"/read"
        http_client = HTTPClient()
        _body = {"read_num": 1}
        _json = json_encode(_body)
        response = http_client.fetch(url, method="POST", body=_json)
        logging.info("got update read_num response %r", response.body)

        self.render('wx/article.html',
                club=club,
                article_id=article_id)


class WxProductHandler(tornado.web.RequestHandler):
    def get(self, club_id, article_id):
        logging.info(self.request)
        logging.info("got article_id %r in uri", article_id)

        # club
        url = "http://api.7x24hs.com/api/clubs/"+club_id
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        club = rs['rs']

        # article
        url = "http://api.7x24hs.com/api/articles/"+article_id
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got article response %r", response.body)
        rs = json_decode(response.body)
        article = rs['rs']
        article['publish_time'] = timestamp_friendly_date(article['publish_time'])

        html = article['paragraphs']
        # 为图片延迟加载准备数据
        # <img alt="" src="http://bighorn.b0.upaiyun.com/blog/2016/11/2/758f7478-d406-4f2e-9566-306a963fb979" />
        # <img data-original="真实图片" src="占位符图片">
        ptn="(<img src=\"http[s]*://[\w\.\/\-]+\" />)"
        img_ptn = re.compile(ptn)
        imgs = img_ptn.findall(html)
        for img in imgs:
            logging.info("got img %r", img)
            ptn="<img src=\"(http[s]*://[\w\.\/\-]+)\" />"
            url_ptn = re.compile(ptn)
            urls = url_ptn.findall(html)
            url = urls[0]
            logging.info("got url %r", url)
            #html = html.replace(img, "<img class=\"lazy\" data-original=\""+url+"\" src=\"/static/images/weui.png\" width=\"100%\" height=\"480\" />")
            html = html.replace(img, "<img width='100%' src='"+url+"!794w' />")
        logging.info("got html %r", html)
        article['paragraphs'] = html

        # article's last comments
        params = {"idx":0, "limit":10}
        url = url_concat("http://api.7x24hs.com/api/articles/"+article_id+"/comment", params)
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got article response %r", response.body)
        rs = json_decode(response.body)
        comments = rs['rs']

        # update read_num
        read_num = article['read_num']
        url = "http://api.7x24hs.com/api/articles/"+article_id+"/read"
        http_client = HTTPClient()
        _body = {"read_num": read_num+1}
        _json = json_encode(_body)
        response = http_client.fetch(url, method="POST", body=_json)
        logging.info("got update read_num response %r", response.body)

        self.render('wx/product.html',
                club=club,
                article=article,
                comments=comments)
