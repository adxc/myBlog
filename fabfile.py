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
from fabric.api import local, lcd, cd, run
from fabric.colors import *


def local_upload(msg):
    with lcd('./'):
        local('pip3 freeze>requirements.txt')
        local('git add .')
        local('git commit -m:'+msg)
        local('git push')