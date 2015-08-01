import bs4
import urllib2
import requests


base_url = 'http://bgp.he.net'

def url1_to_soup(): #this will get the country codes from the main page
	results = []
	country_codes = [] # array of country codes
	


	req  = urllib2.Request("http://bgp.he.net/report/world", headers={'User-Agent': 'Mozilla/5.0'})
	html = urllib2.urlopen(req).read() #open the web page to read
	soup = bs4.BeautifulSoup(html, "lxml") #use beautiful soup to get html
	countries = soup.tbody.find_all('a') #find all the links that are countries

	

	for country in countries:
		country_code = country['href'] #find the links to countries
		results.append(country_code) # add country codes to the array
		

	return results #return results

	
print url1_to_soup() #show all the country codes

	
