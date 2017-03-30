# _*_ coding: utf-8_*_
#
# genral application route config:
# simplify the router config by dinamic load class
# by lwz7512
# @2016/05/17

import tornado.web

from foo import comm
from foo.auth import auth_email
from foo.auth import auth_phone
from foo.portal import shuttle
from foo.portal import demo
from foo.portal import wx


def map():

    config = [

        (r'/wx', getattr(wx, 'WxHomeHandler')),
        (r'/wx/clubs/([a-z0-9]*)/index', getattr(wx, 'WxIndexHandler')),
        (r'/wx/clubs/([a-z0-9]*)/blogs', getattr(wx, 'WxBlogHandler')),
        (r'/wx/clubs/([a-z0-9]*)/products', getattr(wx, 'WxProductIndexHandler')),
        (r'/wx/clubs/([a-z0-9]*)/multimedias', getattr(wx, 'WxMultimediaIndexHandler')),
        (r'/wx/clubs/([a-z0-9]*)/articles/([a-z0-9]*)', getattr(wx, 'WxArticleHandler')),
        (r'/wx/clubs/([a-z0-9]*)/products/([a-z0-9]*)', getattr(wx, 'WxProductHandler')),

        # homepage
        (r'/', getattr(demo, 'DemoIndexHandler')),
        (r'/webapp/clubs/([a-z0-9]*)/index', getattr(demo, 'DemoClubIndexHandler')),
        (r'/webapp/clubs/([a-z0-9]*)/articles', getattr(demo, 'DemoArticlesHandler')),
        (r'/webapp/clubs/([a-z0-9]*)/articles/([a-z0-9]*)', getattr(demo, 'DemoArticleHandler')),
        (r'/webapp/clubs/([a-z0-9]*)/moments', getattr(demo, 'DemoMomentsHandler')),
        (r'/webapp/clubs/([a-z0-9]*)/add-moment', getattr(demo, 'DemoAddMomentHandler')),

        (r'/webapp/auth/login', getattr(auth_phone, 'AuthLoginHandler')),
        (r'/webapp/auth/regist', getattr(auth_phone, 'AuthRegistHandler')),
        (r'/webapp/auth/forget', getattr(auth_phone, 'AuthForgotPwdHandler')),
        (r'/webapp/login-next', getattr(auth_phone, 'WebappLoginNextHandler')),

        (r'/webapp', getattr(shuttle, 'ShuttleIndexHandler')),
        (r'/webapp/index', getattr(shuttle, 'ShuttleIndexHandler')),
        (r'/webapp/index-sliced', getattr(shuttle, 'ShuttleIndexSlicedHandler')),
        (r'/webapp/index-slider', getattr(shuttle, 'ShuttleIndexSliderHandler')),
        (r'/webapp/index-drawer', getattr(shuttle, 'ShuttleIndexDrawerHandler')),
        (r'/webapp/index-walkthrough', getattr(shuttle, 'ShuttleIndexWalkthroughHandler')),
        (r'/webapp/404', getattr(shuttle, 'Shuttle404Handler')),
        (r'/webapp/activity', getattr(shuttle, 'ShuttleActivityHandler')),
        (r'/webapp/article', getattr(shuttle, 'ShuttleArticleHandler')),
        (r'/webapp/blank', getattr(shuttle, 'ShuttleBlankHandler')),
        (r'/webapp/blog-masonry', getattr(shuttle, 'ShuttleBlogMasonryHandler')),
        (r'/webapp/blog', getattr(shuttle, 'ShuttleBlogHandler')),
        (r'/webapp/calendar', getattr(shuttle, 'ShuttleCalendarHandler')),
        (r'/webapp/category', getattr(shuttle, 'ShuttleCategoryHandler')),
        (r'/webapp/chart', getattr(shuttle, 'ShuttleChartHandler')),
        (r'/webapp/chat', getattr(shuttle, 'ShuttleChatHandler')),
        (r'/webapp/checkout', getattr(shuttle, 'ShuttleCheckoutHandler')),
        (r'/webapp/coming-soon', getattr(shuttle, 'ShuttleComingSoonHandler')),
        (r'/webapp/contact', getattr(shuttle, 'ShuttleContactHandler')),
        (r'/webapp/dual-sidebar', getattr(shuttle, 'ShuttleDualSidebarHandler')),
        (r'/webapp/event', getattr(shuttle, 'ShuttleEventHandler')),
        (r'/webapp/faq', getattr(shuttle, 'ShuttleFaqHandler')),
        (r'/webapp/forgot', getattr(shuttle, 'ShuttleForgotHandler')),
        (r'/webapp/gallery-card', getattr(shuttle, 'ShuttleGalleryCardHandler')),
        (r'/webapp/gallery-filter', getattr(shuttle, 'ShuttleGalleryFilterHandler')),
        (r'/webapp/gallery-masonry', getattr(shuttle, 'ShuttleGalleryMasonryHandler')),
        (r'/webapp/left-sidebar', getattr(shuttle, 'ShuttleLeftSidebarHandler')),
        (r'/webapp/lockscreen', getattr(shuttle, 'ShuttleLockscreenHandler')),
        (r'/webapp/login', getattr(shuttle, 'ShuttleLoginHandler')),
        (r'/webapp/material', getattr(shuttle, 'ShuttleMaterialHandler')),
        (r'/webapp/news', getattr(shuttle, 'ShuttleNewsHandler')),
        (r'/webapp/player', getattr(shuttle, 'ShuttlePlayerHandler')),
        (r'/webapp/portfolio-card', getattr(shuttle, 'ShuttlePortfolioCardHandler')),
        (r'/webapp/portfolio-filter', getattr(shuttle, 'ShuttlePortfolioFilterHandler')),
        (r'/webapp/portfolio-masonry', getattr(shuttle, 'ShuttlePortfolioMasonryHandler')),
        (r'/webapp/product', getattr(shuttle, 'ShuttleProductHandler')),
        (r'/webapp/profile', getattr(shuttle, 'ShuttleProfileHandler')),
        (r'/webapp/project', getattr(shuttle, 'ShuttleProjectHandler')),
        (r'/webapp/right-sidebar', getattr(shuttle, 'ShuttleRightSidebarHandler')),
        (r'/webapp/search', getattr(shuttle, 'ShuttleSearchHandler')),
        (r'/webapp/shop', getattr(shuttle, 'ShuttleShopHandler')),
        (r'/webapp/signup', getattr(shuttle, 'ShuttleSignupHandler')),
        (r'/webapp/timeline', getattr(shuttle, 'ShuttleTimelineHandler')),
        (r'/webapp/todo', getattr(shuttle, 'ShuttleTodoHandler')),

        (r'/club/auth/login', getattr(auth_email, 'AuthEmailLoginHandler')),
        (r'/club/auth/register', getattr(auth_email, 'AuthEmailRegisterHandler')),
        (r'/club/auth/forgot-pwd', getattr(auth_email, 'AuthEmailForgotPwdHandler')),
        (r'/club/auth/reset-pwd', getattr(auth_email, 'AuthEmailResetPwdHandler')),
        (r'/club/auth/register/into-league', getattr(auth_email, 'AuthRegisterIntoLeagueXHR')),
        (r'/club/auth/logout', getattr(auth_email, 'AuthLogoutHandler')),

        # comm
        ('.*', getattr(comm, 'PageNotFoundHandler'))

    ]

    return config
