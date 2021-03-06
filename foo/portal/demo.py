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

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../dao"))

from comm import *
from global_const import *


class DemoIndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/webapp/clubs/"+CLUB_ID+"/index")


class DemoClubIndexHandler(tornado.web.RequestHandler):
    def get(self,club_id):
        logging.info(self.request)
        logging.info("got club_id %r--------", club_id)

        # multimedia
        params = {"filter":"club", "club_id":club_id, "idx":0, "limit":3}
        url = url_concat("http://api.7x24hs.com/api/multimedias", params)
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        multimedias = rs['rs']

        # articles
        params = {"filter":"club", "club_id":club_id, "status":"publish", "idx":0, "limit":20}
        url = url_concat("http://api.7x24hs.com/api/articles", params)
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        articles = rs['rs']
        logging.info("got articles=[%r]", articles)

        # lastest comments(最新的评论)
        params = {"filter":"club", "club_id":club_id, "idx":0, "limit":3}
        url = url_concat("http://api.7x24hs.com/api/last-comments", params)
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        lastest_comments = rs['rs']

        self.render('demo/index.html',
                club_id=club_id,
                multimedias=multimedias,
                lastest_comments=lastest_comments,
                articles=articles)


class DemoAddMomentHandler(AuthorizationHandler):
    @tornado.web.authenticated  # if no session, redirect to login page
    def get(self,club_id):
        logging.info(self.request)

        self.render('demo/add-moment.html',
                club_id=club_id)


class DemoMomentsHandler(tornado.web.RequestHandler):
    def get(self,club_id):
        logging.info(self.request)

        # moments(精彩瞬间)
        params = {"filter":"club", "club_id":club_id, "idx":0, "limit":20}
        url = url_concat("http://api.7x24hs.com/api/moments", params)
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        moments = rs['rs']
        for article in moments:
            article['publish_time'] = timestamp_friendly_date(article['publish_time'])
        logging.info("got moments=[%r]", moments)

        self.render('demo/moments.html',
                club_id=club_id,
                moments=moments)


class DemoArticlesHandler(tornado.web.RequestHandler):
    def get(self,club_id):
        logging.info(self.request)

        # all articles of club
        params = {"filter":"club", "club_id":club_id, "idx":0, "limit":20}
        url = url_concat("http://api.7x24hs.com/api/articles", params)
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        articles = rs['rs']
        for article in articles:
            article['publish_time'] = timestamp_friendly_date(article['publish_time'])

        self.render('demo/articles.html',
                club_id=club_id,
                articles=articles)


class DemoArticleHandler(tornado.web.RequestHandler):
    def get(self, club_id, article_id):
        logging.info(self.request)
        logging.info("got article_id %r in uri", article_id)

        # article
        url = "http://api.7x24hs.com/api/articles/"+article_id
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got article response %r", response.body)
        rs = json_decode(response.body)
        article = rs['rs']
        article['publish_time'] = timestamp_friendly_date(article['publish_time'])

        # update read_num
        read_num = article['read_num']
        url = "http://api.7x24hs.com/api/articles/"+article_id+"/read"
        http_client = HTTPClient()
        _body = {"read_num": read_num+1}
        _json = json_encode(_body)
        response = http_client.fetch(url, method="POST", body=_json)
        logging.info("got update read_num response %r", response.body)

        self.render('demo/article.html',
                club_id=club_id,
                article=article)
