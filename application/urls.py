"""
urls.py
URL dispatch route mappings and error handlers

"""

from flask import render_template
from application import app
import views
import api


## URL dispatch rules
app.add_url_rule('/', 'index', view_func=views.index)
app.add_url_rule('/api/v<api_version>/<team>/', view_func=api.team)
app.add_url_rule('/api/v<api_version>/<team>/<metric>/', view_func=api.teamMetrics)

# Handle 404 error
@app.errorhandler(404)
def page_not_found(e):
	return "Page Not Found"

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
	return "Internal Server Error"

