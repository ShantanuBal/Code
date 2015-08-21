import urllib2, time

for i in range(18898,26287):
	response = urllib2.urlopen('http://nunki.usc.edu:8088/cgi-bin/gradesJSON.pl?ssn=' + str(i))
	html = response.read()
	print i, "---", html
	time.sleep(2)
