# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-23 05:42:56
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-23 05:46:01


from flask_login import current_user
from flask import abort


class Authenticated():
    """
    Authentication helper
    """

    def __init__(self):
        if not current_user.is_authenticated:
            abort(403)
