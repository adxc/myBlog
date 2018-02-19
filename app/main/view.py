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

from flask import jsonify, make_response, render_template, request
from . import main
from myBlog import db
from ..models import User, Post, Type


@main.route('/', methods=['get', 'post'])
def index():
    return render_template('index.html')


@main.route('/front/api/all', methods=['get', 'post'])
def all_data():
    """
    :argument:首页数据获取
    :param pageNum: 页数 默认 1
    :param pageSize: 每页显示数量 默认 10
    :return:首页所有数据
    """
    #pageNum = request.args.get("pageNum") if request.args.get("pageNum") else 1
    pageSize = request.args.get("pageSize") if request.args.get("pageNum") else 10
    articles = Post.query.order_by(Post.timestamp.desc()).limit(pageSize)
    articles_list = []
    for article in articles:
        item = {
            "id": article.id,
            "title": article.title,
            "content": article.article_body_html,
            "author": article.author,
            "tag": article.article_tag,
            "time": article.timestamp,
            "type": article.type.type
        }
        articles_list.append(item)
    data = {
        "code": 0,
        "data": articles_list,
        "msg": "success"
    }
    response = make_response(jsonify(data))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


@main.route("/front/api/articleType/<type>", methods=['get', 'post'])
def article_list(type):
    """
    :argument:根据文章分类获取文章列表
    :param type: 文章分类
    :param pageNum: 页数 默认 1
    :param pageSize: 每页显示数量 默认 10
    :return: 所有文章内容
    """
    article_type = Type.query.filter_by(type=type).first()
    # pageNum = request.args.get("pageNum") if request.args.get("pageNum") else 1
    pageSize = request.args.get("pageSize") if request.args.get("pageNum") else 10
    articles = Post.query.filter(Post.article_type == article_type.id).order_by(Post.timestamp.desc()).limit(pageSize)
    articles_list = []
    for article in articles:
        item = {
            "id": article.id,
            "title": article.title,
            "content": article.article_body_html,
            "author": article.author,
            "tag": article.article_tag,
            "time": article.timestamp,
            "type": article.type.type
        }
        articles_list.append(item)
    data = {
        "code": 0,
        "data": articles_list,
        "msg": "success"
    }
    response = make_response(jsonify(data))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


@main.route('/front/api/articleDetails/<id>', methods=['get', 'post'])
def article_details(id):
    """
    :argument:获取文章详情
    :param id: 文章ID
    :return: 文章详情
    """
    article = Post.query.filter_by(id=id).first()
    details = {
        "id": article.id,
        "title": article.title,
        "content": article.article_body_html,
        "author": article.author,
        "tag": article.article_tag,
        "time": article.timestamp,
        "type": article.type.type
    }
    data = {
        "code": 0,
        "data": details,
        "msg": "success"
    }
    response = make_response(jsonify(data))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response
