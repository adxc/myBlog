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
from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import view