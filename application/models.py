"""
Database Emulator for the teammetrics project
Temporarily the data is generated by accessing data available at http://blend.debian.org/liststats

"""
import urllib2

def extractMetrics(team, metric):
	"""
	Parses the data available at the url into a data structure.
	"""
	url = "http://blends.debian.net/liststats/"+metric+"_"+team+"_year.txt"
	lines = urllib2.urlopen(url).readlines()
	ll = len(lines)
	names = lines[0].split('\t')
	results = dict()
	for i in range (1,ll):
		data =  lines[i].split('\t')
		year = data[0]
		lw = len(data)
		yeardata=dict()
		for j in range(1,lw):
			yeardata[names[j]]=data[j]
		results[year]=yeardata
		del year
	results["source"] = url
	return results
