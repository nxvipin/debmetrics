"""
views.py

URL route handlers

"""

from flask import render_template, flash, url_for, redirect, json
from flask import jsonify


def index():
	return "Test Flask App"

def teamMetrics(team, metric):
	return "<img src=http://blends.debian.net/liststats/"+metric+"_"+team+".png>"
