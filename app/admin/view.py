#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 *          __                                                __
 *   ____  / /_     ____ ___  __  __    ____  ____  ____     / /
 *  / __ \/ __ \   / __ `__ \/ / / /   / __ \/ __ \/ __ \   / /
 * / /_/ / / / /  / / / / / / /_/ /   / /_/ / /_/ / /_/ /  /_/
 * \____/_/ /_/  /_/ /_/ /_/\__, /    \__  /\__ _/_____/  __
 *                         /____/     /___/              /_/
 *  ━━━━━━神兽出没━━━━━━
 *     ┏ ┓    ┏ ┓
 *  ┏━━┛ ┻━━━━┛ ┻━━┓
 *  ┃              ┃
 *  ┃     ━━━      ┃
 *  ┃  ━┳┛   ┗┳━   ┃
 *  ┃              ┃
 *  ┃     ━┻━      ┃
 *  ┃              ┃
 *  ┗━┓          ┏━┛Code is far away from bug with the animal protecting
 *    ┃          ┃    神兽保佑,代码无bug
 *    ┃          ┃
 *    ┃          ┗━━━┓
 *    ┃              ┣┓
 *    ┃              ┏┛
 *    ┗━━━━┓┓┏━━━━┳┓┏┛
 *         ┃┫┫    ┃┫┫
 *         ┗┻┛    ┗┻┛
 *   ━━━━━━感觉萌萌哒━━━━━━
 '''

from flask import render_template
from . import admin
from .form import RegisterForm, EditForm
from myBlog import db
from app.models import User, Post


@admin.route('/login', methods=["GET", "POST"])
def login():
    # if request.form:
    #     account = request.form['account']
    #     password = request.form['password']
    #     if account == '9':
    #         return render_template('admin/index.html')
    return render_template('admin/login.html')


@admin.route('/', methods=['GET', 'POST'])
def index():
    return render_template('admin/index.html')


@admin.route('/front-end', methods=['GET', 'POST'])
def front_end():
    return render_template('admin/front-end.html')


@admin.route('/python', methods=['GET', 'POST'])
def python():
    return render_template('admin/python.html')


@admin.route('/fiction', methods=['GET', 'POST'])
def fiction():
    return render_template('admin/fiction.html')


@admin.route('/sign-up', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
    return render_template('admin/sign-up.html', form=form)


@admin.route('/edit', methods=['GET', 'POST'])
def edit():
    form = EditForm()
    tags = ['pythonTag', 'CssTag', 'JsTag', 'MachineTag']
    article_tag = []
    if form.validate_on_submit():
        article_body = form.article.data
        title = form.title.data
        article_type = form.articleType.data
        for tag in tags:
            if form.data[tag]:
                article_tag.append(tag[:-3])
        post = Post(title=title, article_body=article_body, article_type=article_type, author=None,
                    article_tag=','.join(article_tag))
        db.session.add(post)
        db.session.commit()
    return render_template('admin/edit.html', form=form)
