"""
views.py

URL route handlers

"""

from flask import render_template, flash, url_for, redirect, json
from flask import render_template


def index():
	return render_template('index.html')

def teamMetricsStaticImage(team, metric):
	d=dict();
	d["team"]=team;
	d["metric"]=metric;
	return render_template('chart.html',data=d)

def teamMetricsDynamicImage(team, metric):
	d=dict();
	d["team"]=team;
	d["metric"]=metric;
	return render_template('dchart.html',data=d)
