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


class EshopHomeHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)

        self.redirect("/webapp/eshop/clubs/"+CLUB_ID)


class EshopIndexHandler(tornado.web.RequestHandler):
    def get(self, club_id):
        logging.info(self.request)
        logging.info("got club_id %r--------", club_id)

        # club
        url = API_DOMAIN + "/api/clubs/" + club_id
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got club response %r", response.body)
        rs = json_decode(response.body)
        club = rs['rs']

        self.render('eshop/index.html',
                API_DOMAIN=API_DOMAIN,
                club=club)


class EshopArticleHandler(tornado.web.RequestHandler):
    def get(self, club_id, article_id):
        logging.info(self.request)
        logging.info("got article_id %r in uri", article_id)

        # club
        url = API_DOMAIN + "/api/clubs/"+club_id
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        club = rs['rs']

        # update read_num
        url = API_DOMAIN + "/api/articles/"+article_id+"/read"
        http_client = HTTPClient()
        _body = {"read_num": 1}
        _json = json_encode(_body)
        response = http_client.fetch(url, method="POST", body=_json)
        logging.info("got update read_num response %r", response.body)

        self.render('eshop/article.html',
                API_DOMAIN=API_DOMAIN,
                club=club,
                article_id=article_id)


class EshopProductHandler(tornado.web.RequestHandler):
    def get(self, club_id, article_id):
        logging.info(self.request)
        logging.info("got article_id %r in uri", article_id)

        # club
        url = API_DOMAIN + "/api/clubs/"+club_id
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        club = rs['rs']

        # update read_num
        url = API_DOMAIN + "/api/articles/"+article_id+"/read"
        http_client = HTTPClient()
        _body = {"read_num": 1}
        _json = json_encode(_body)
        response = http_client.fetch(url, method="POST", body=_json)
        logging.info("got update read_num response %r", response.body)

        self.render('eshop/product.html',
                API_DOMAIN=API_DOMAIN,
                club=club,
                article_id=article_id)


class EshopArticleAddCommentHandler(tornado.web.RequestHandler):
    def get(self, club_id, article_id):
        logging.info(self.request)
        logging.info("got article_id %r in uri", article_id)

        # club
        url = API_DOMAIN + "/api/clubs/"+club_id
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        club = rs['rs']

        self.render('eshop/add-comment.html',
                API_DOMAIN=API_DOMAIN,
                club=club,
                article_id=article_id)


class EshopProductPlaceOrderHandler(tornado.web.RequestHandler):
    def get(self, club_id, article_id):
        logging.info(self.request)
        logging.info("got article_id %r in uri", article_id)

        # club
        url = API_DOMAIN + "/api/clubs/"+club_id
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        club = rs['rs']

        # article
        url = API_DOMAIN + "/api/articles/"+article_id
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got article response %r", response.body)
        rs = json_decode(response.body)
        article = rs['rs']

        self.render('eshop/place-order.html',
                API_DOMAIN=API_DOMAIN,
                club=club,
                article=article)


class EshopProductPlaceOrderSuccessHandler(tornado.web.RequestHandler):
    def get(self, club_id, article_id):
        logging.info(self.request)
        logging.info("got article_id %r in uri", article_id)

        # club
        url = API_DOMAIN + "/api/clubs/"+club_id
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got response %r", response.body)
        rs = json_decode(response.body)
        club = rs['rs']

        # article
        url = API_DOMAIN + "/api/articles/"+article_id
        http_client = HTTPClient()
        response = http_client.fetch(url, method="GET")
        logging.info("got article response %r", response.body)
        rs = json_decode(response.body)
        article = rs['rs']

        self.render('eshop/place-order-success.html',
                API_DOMAIN=API_DOMAIN,
                club=club,
                article=article)
