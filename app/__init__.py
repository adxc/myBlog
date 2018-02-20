#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
  Created by Xic on 2018/1/28.
      _              _              _
     / \   _ __   __| |_   _  __  _(_) ___
    / _ \ | '_ \ / _` | | | | \ \/ / |/ __|
   / ___ \| | | | (_| | |_| |  >  <| | (__
  /_/   \_\_| |_|\__,_|\__, | /_/\_\_|\___|
                       |___/ 
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pagedown import PageDown
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
page_down = PageDown()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'admin.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    page_down.init_app(app)
    login_manager.init_app(app)

    # 注册蓝本
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


from app.main import view