#!/usr/bin/env python
# _*_ coding: utf-8_*_
#
# Copyright 2016 7x24hs.com
# thomas@7x24hs.com
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
import hashlib
import json as JSON # 启用别名，不会跟方法里的局部变量混淆
from bson import json_util
import requests

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../dao"))

from tornado.escape import json_encode, json_decode
from tornado.httpclient import *
from tornado.httputil import url_concat
from bson import json_util

from comm import *
from global_const import *

class WebappLoginNextHandler(BaseHandler):
    def get(self):
        login_next = self.get_secure_cookie("login_next")
        if login_next:
            self.redirect(login_next)
        else:
            self.redirect("/")

class AuthLoginHandler(BaseHandler):
    def get(self):
        logging.info(self.request)
        self.render('auth/login.html',err_msg="")

    def post(self):
        logging.info(self.request)
        logging.info(self.request.body)
        phone = self.get_argument("lg_phone", "")
        pwd = self.get_argument("lg_pwd", "")
        remember = self.get_argument("lg_remember", "")
        logging.info("try login as phone:[%r] pwd:[%r] remember:[%r]", phone, pwd, remember)

        code = self.get_code()

        # login
        try:
            url = "http://api.7x24hs.com/api/auth/tokens"
            http_client = HTTPClient()
            headers={"Authorization":"Bearer "+code}
            data = {"action":"login",
                    "login_type":"phone",
                    "phone":phone,
                    "pwd":pwd}
            _json = json_encode(data)
            logging.info("request %r body %r", url, _json)
            response = http_client.fetch(url, method="POST", headers=headers, body=_json)
            logging.info("got response %r", response.body)
            rs = json_decode(response.body)
            session_ticket = rs['rs']

            # 添加此帐号到俱乐部的普通用户帐号表中
            url = "http://api.7x24hs.com/api/clubs/"+CLUB_ID+"/signup"
            http_client = HTTPClient()
            _json = json_encode({"role":"user"})
            headers={"Authorization":"Bearer "+session_ticket['access_token']}
            response = http_client.fetch(url, method="POST", headers=headers, body=_json)
            logging.info("got response %r", response.body)

            self.set_secure_cookie("access_token", session_ticket['access_token'])
            self.set_secure_cookie("expires_at", str(session_ticket['expires_at']))
        except:
            err_title = str( sys.exc_info()[0] );
            err_detail = str( sys.exc_info()[1] );
            logging.error("error: %r info: %r", err_title, err_detail)
            if err_detail == 'HTTP 404: Not Found':
                err_msg = "手机号码或密码不正确!"
                self.render('auth/login.html', err_msg=err_msg)
                return
            else:
                err_msg = "系统故障, 请稍后尝试!"
                self.render('auth/login.html', err_msg=err_msg)
                return

        login_next = self.get_secure_cookie("login_next")
        if not login_next:
            login_next = "/"
        self.redirect(login_next)



class AuthRegistHandler(BaseHandler):
    def get(self):
        logging.info(self.request)
        self.render('auth/regist.html')

    # def post(self):


class AuthForgotPwdHandler(BaseHandler):
    def get(self):
        logging.info(self.request)
        self.render('auth/forget.html')

    # def post(self):
