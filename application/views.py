"""
views.py

URL route handlers

"""


from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError
from flask import render_template, flash, url_for, redirect


def index():
    return "Test Flask App"

