"""
Defines various API's to access the project data. Only supports JSON data format now.
API Version is ignored in the prototype.
"""

from flask import render_template, flash, url_for, redirect, json
from flask import jsonify
import models
from teamlist import teams


def team(api_version, team):
	"""
	Links all the available metrics of a team, as defined in teamlist.py and
	returns a combined JSON of all the available data.
	Only supports the 'teammetrics' project now.
	"""
	if team == "teammetrics":
		return jsonify(	results={	"authorstats" : models.extractMetrics(teams[team]["authorstats"],"authorstat"),
									"commitstats" : models.extractMetrics(teams[team]["commitstats"],"commitstat"),
									"commitlines" : models.extractMetrics(teams[team]["commitlines"],"commitlines")
								})
	else:
		return jsonify(results="No data available. Try 'teammetrics' as team name.")

def teamMetrics(api_version, team, metric):
	"""
	Given a team and a particular metric, the available data is returned in JSON format.
	"""
	return jsonify(results=models.extractMetrics(team,metric))

