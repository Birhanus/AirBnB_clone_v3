#!/usr/bin/python3
""" views """

from flask import Blueprint, render_template, abort
from api.v1.views.index import *

app_views = Blueprint('app_views', url_prefix='/api/v1')

