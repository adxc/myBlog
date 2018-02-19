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
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from flask_pagedown.fields import PageDownField


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 64), Regexp('^(?!_)(?!.*?_$)[a-zA-Z0-9_'
                                                                                    '\u4e00-\u9fa5]+$', 0,
                                                                                    message='非法用户名')])
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[DataRequired(), EqualTo('cfm_password', message='密码必须一致')])
    cfm_password = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('注册')


class EditForm(FlaskForm):
    article = PageDownField("Your post", validators=[DataRequired()])
    title = StringField('标题', validators=[DataRequired()])
    pythonTag = BooleanField('Python')
    JsTag = BooleanField('JavaScript')
    MachineTag = BooleanField('机器学习')
    CssTag = BooleanField('Css')
    articleType = SelectField('文章类型', choices=[('1', 'Python'), ('2', '随笔'), ('3', '小说'),('4', '前端')], validators=[DataRequired()])
    submit = SubmitField('保存')
