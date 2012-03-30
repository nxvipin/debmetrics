"""
Defines various API's to access the project data. Only supports JSON data format now.
API Version is ignored in the prototype.
"""

from flask import render_template, flash, url_for, redirect
import simplejson
import models
from teamlist import teams


def team(api_version, team):
	"""
	Links all the available metrics of a team, as defined in teamlist.py and
	returns a combined JSON of all the available data.
	Only supports the 'teammetrics' project now.
	"""
	if team == "teammetrics":
		return simplejson.dumps(	[ models.extractMetrics(teams[team]["authorstats"],"authorstat"),
						models.extractMetrics(teams[team]["commitstats"],"commitstat"),
						models.extractMetrics(teams[team]["commitlines"],"commitlines")]
								)
	else:
		return jsonify(results="No data available. Try 'teammetrics' as team name.")

def teamMetrics(api_version, team, metric):
	"""
	Given a team and a particular metric, the available data is returned in JSON format.
	"""
	r = models.extractMetrics(team,metric)
	return simplejson.dumps([r])

