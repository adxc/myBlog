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

from flask import render_template, request, redirect, url_for
from . import admin
from .form import RegisterForm, EditForm, LoginForm
from myBlog import db
from app.models import User, Post
from flask_login import login_required, login_user, logout_user
import re


@admin.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember_me.data
        user = User.query.filter_by(username=username).first()
        if user is not None and user.verify_password(password):
            login_user(user, remember)
            if request.args.get('next') and re.match('/admin', request.args.get('next')) is not None:
                return redirect(request.args.get('next'))
            else:
                return redirect(url_for('admin.index'))
    return render_template('admin/login.html', form=form)


@admin.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('admin/index.html')


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
        return redirect('admin.login')
    return render_template('admin/sign-up.html', form=form)


@admin.route('/edit', methods=['GET', 'POST'])
@login_required
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


@admin.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('main.index'))
