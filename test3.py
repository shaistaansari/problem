import bs4
import urllib2
import requests
import testcrawl
import json




def url2_to_soup(): #get the asn numbers from the second page
	results = [] #array for storing the asn
	country_codes = [] #This will be the link to tags that are links
	asn_number = []


	req  = urllib2.Request("http://bgp.he.net/country/US", headers={'User-Agent': 'Mozilla/5.0'})
	html = urllib2.urlopen(req).read() #open the file to read
	soup = bs4.BeautifulSoup(html, "lxml") #Get the html from the web page using beautiful soup
	countries = soup.tbody.find_all('a') #find all the links

	

	for country in countries:
		country_code = country['href']  #get the asn numbers
		results.append(country_code) #add the asn number to the array
		

	return results #send the asn numbers 

file = open("savedata", "w") #open file to read json
data = (url2_to_soup(), testcrawl.url1_to_soup()) #assign vlaue of data to the countery codes and asn numbers
json.dump(data, file) #save all the code in json
file.close #close the file

print testcrawl.url1_to_soup() #print country codes	
print url2_to_soup() #print Asn numbers


