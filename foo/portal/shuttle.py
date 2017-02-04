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


class ShuttleIndexHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/index.html')


class ShuttleIndexSlicedHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/index-sliced.html')


class ShuttleIndexSliderHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/index-slider.html')


class ShuttleIndexDrawerHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/index-drawer.html')


class ShuttleIndexWalkthroughHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/index-walkthrough.html')


class Shuttle404Handler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/404.html')


class ShuttleActivityHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/activity.html')


class ShuttleArticleHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/article.html')


class ShuttleBlankHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/blank.html')


class ShuttleBlogMasonryHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/blog-masonry.html')


class ShuttleBlogHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/blog.html')


class ShuttleCalendarHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/calendar.html')


class ShuttleCategoryHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/category.html')


class ShuttleChartHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/chart.html')


class ShuttleChatHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/chat.html')


class ShuttleCheckoutHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/checkout.html')


class ShuttleComingSoonHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/coming-soon.html')


class ShuttleContactHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/contact.html')


class ShuttleDualSidebarHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/dual-sidebar.html')


class ShuttleEventHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/event.html')


class ShuttleFaqHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/faq.html')


class ShuttleForgotHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/forgot.html')


class ShuttleGalleryCardHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/gallery-card.html')


class ShuttleGalleryFilterHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/gallery-filter.html')


class ShuttleGalleryMasonryHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/gallery-masonry.html')


class ShuttleLeftSidebarHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/left-sidebar.html')


class ShuttleLockscreenHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/lockscreen.html')


class ShuttleLoginHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/login.html')


class ShuttleMaterialHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/material.html')


class ShuttleNewsHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/news.html')


class ShuttlePlayerHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/player.html')


class ShuttlePortfolioCardHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/portfolio-card.html')


class ShuttlePortfolioFilterHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/portfolio-filter.html')


class ShuttlePortfolioMasonryHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/portfolio-masonry.html')


class ShuttleProductHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/product.html')


class ShuttleProfileHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/profile.html')


class ShuttleProjectHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/project.html')


class ShuttleRightSidebarHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/right-sidebar.html')


class ShuttleSearchHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/search.html')


class ShuttleShopHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/shop.html')


class ShuttleSignupHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/signup.html')


class ShuttleTimelineHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/timeline.html')


class ShuttleTodoHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info(self.request)
        self.render('shuttle/todo.html')
