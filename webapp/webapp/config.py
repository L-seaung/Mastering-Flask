#!/usr/bin/env python
# -*- coding:utf-8 -*-
from os import path

class Config(object):
    SECRET_KEY = 'JLKJDFJDJFIE'
    RECAPTCHA_PUBLIC_KEY = "6LdKkQQTAAAAAEH0GFj7NLg5tGicaoO7G 9Q5Uw"
    RECAPTCHA_PRIVATE_KEY = "6LdKkQQTAAAAAMYroksPTJ7pWhobYb88FTAcxYn"


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = "mysql://root:seaunglee7811@127.0.0.1:3306/webapp"
    SQLALCHEMY_DATABASE_URI = "sqlite://" + path.join(path.pardir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
