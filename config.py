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


class Config(object):
    SECRET_KEY = 'beautifulMan'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/myblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    JSON_AS_ASCII = False
    DEBUG = True
