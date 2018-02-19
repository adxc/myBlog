#! /usr/bin/env python3
import os
from app import create_app, db
from app.models import User, Post, Type
from flask_script import Manager, Shell

app = create_app()
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Type=Type)


manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()


