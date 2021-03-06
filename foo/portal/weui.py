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


class WeuiHomeHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)

        self.redirect("/weui/clubs/"+CLUB_ID+"/index")


class WeuiIndexHandler(tornado.web.RequestHandler):
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

        self.render('weui/index.html',
                club=club,
                articles=articles,
                multimedias=multimedias)


class WeuiProductHandler(tornado.web.RequestHandler):
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

        self.render('weui/product.html',
                club=club,
                article=article)


class WeuiPlaceOrderHandler(tornado.web.RequestHandler):
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

        self.render('weui/place-order.html',
                club=club,
                article=article)


class WeuiPlaceOrderSuccessHandler(tornado.web.RequestHandler):
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

        self.render('weui/place-order-success.html',
                club=club,
                article=article)


class WeuiPcHandler(tornado.web.RequestHandler):
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

        self.render('weui/pc.html',
                club=club)
