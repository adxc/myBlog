#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
  Created by Xic on 2018/2/18.
      _              _              _
     / \   _ __   __| |_   _  __  _(_) ___
    / _ \ | '_ \ / _` | | | | \ \/ / |/ __|
   / ___ \| | | | (_| | |_| |  >  <| | (__
  /_/   \_\_| |_|\__,_|\__, | /_/\_\_|\___|
                       |___/ 
'''
from fabric.api import local, lcd, cd, run, task, env, execute, hide, sudo
from fabric.colors import red, green

env.hosts = ['pi@192.168.0.106']
env.password = 'xichen520'


@task
def local_upload(msg):
    with lcd('./'):
        local('pip3 freeze>requirements.txt')
        local('git add .')
        local('git commit -m:"%s"' % msg)
        local('git push')


@task
def server_upload():
        run('git pull')
        run('source ./venv/bin/activate')
        run('pip3 install -r requirements.txt')


@task
def check_command(cmd):
    rs = local('command -v %s' %cmd)
    return rs.return_code == 0


@task
def install_package(package):
    sudo('pip3 install %s' % package)
    print(green('%s 安装成功') % package)


@task
def server_start():
    with cd('~/work/myBlog'):
        execute(server_upload)
        with hide('stdout', 'stderr', 'aborts'):
            if not check_command('gunicorn'):
                install_package('gunicorn')
        print(green('运行成功'))

@task
def deploy(msg):
    local_upload(msg)
    execute(server_start)