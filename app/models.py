#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 *          __                                                __
 *   ____  / /_     ____ ___  __  __    ____  ____  ____     / /
 *  / __ \/ __ \   / __ `__ \/ / / /   / __ \/ __ \/ __ \   / /
 * / /_/ / / / /  / / / / / / /_/ /   / /_/ / /_/ / /_/ /  /_/
 * \____/_/ /_/  /_/ /_/ /_/\__, /    \__  /\__ _/_____/  __
 *                         /____/     /___/              /_/
 '''

from datetime import datetime
from markdown import markdown
import bleach
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute/ password 不是一个可读属性。')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):

    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_body = db.Column(db.Text, nullable=False)
    article_body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now(), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255))
    article_type = db.Column(db.Integer, db.ForeignKey('articleType.id'))
    article_tag = db.Column(db.String(255))
    type = db.relationship('Type', order_by='Type.type')

    def __init__(self, article_body, title, author, article_type, article_tag):
        self.article_body = article_body
        self.title = title
        self.author = author or 'xichen'
        self.article_type = article_type
        self.article_tag = article_tag

    @staticmethod
    def on_changed_article(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
        target.article_body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags,
                                                       strip=True))


db.event.listen(Post.article_body, 'set', Post.on_changed_article)


class Type(db.Model):
    __tablename__ = 'articleType'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(255), nullable=False)
    post_id = db.relationship('Post', backref='role')


