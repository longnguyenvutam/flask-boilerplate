# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-22 08:31:53
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-23 05:41:16


class Config(object):
    """
    Base Config class
    """

    ERR_LOG_LEVEL = 'ERROR'


class ConfigProduction(Config):
    """
    Production config set
    """

    SQLALCHEMY_DATABASE_URI = 'mysql://db_prod_user:db_prod_password@localhost/db_prod?use_unicode=1&charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfigDevelopment(Config):
    """
    Development config set
    --only for development and testing--
    """

    SQLALCHEMY_DATABASE_URI = 'mysql://db_dev_user:db_dev_password@localhost/db_dev?use_unicode=1&charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_dict = {
    'production': ConfigProduction,
    'development': ConfigDevelopment
}
