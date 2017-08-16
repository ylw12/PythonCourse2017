# Go to https://petitions.whitehouse.gov/petitions
# Go to the petition page for each of the petitions.
# Create a .csv file with the following information for each petition:
# - Title
# - Published date
# - Issues
# - Number of signatures
	
from bs4 import BeautifulSoup
import urllib2
import csv
import pdb

# Find the main website page by page
web_address=["https://petitions.whitehouse.gov/petitions?page=" + str(i) for i in range(0, 3)]

# Make and parse the soup; Extract the url for each of the petitions
petitions0 = []
petitions = []
for i in web_address:
	web_page = urllib2.urlopen(i)
	soup = BeautifulSoup(web_page.read())
	soup.prettify()
	petitions0.append(soup.find_all('h3'))
	flat = [item for sublist in petitions0 for item in sublist] # Make a flat list here
	for j in range(0,len(flat)):
		try:
			petitions.append("https://petitions.whitehouse.gov"+flat[j].a['href'])
		except: # Get rid of <h3>Create a Petition</h3>, <h3>Gather Signatures</h3> ...
			pass 

# For each petitions, gether their title, published date, 
# issues, number of signatures in their individual webpages.
Titles = []
Dates = []
Issues = []
Signatures = []
for i in range(0, len(petitions)):
	# Visit the webpage and make the soup
	temp_page = urllib2.urlopen(petitions[i])
	temp_soup = BeautifulSoup(temp_page.read())
	# Get the titles
	title = temp_soup.find('h1', {"class": "title"}).text
	Titles.append(title.encode("utf8"))
	# Get the dates
	attribution = temp_soup.find('h4', {"class": "petition-attribution"}).text
	Dates.append(" ".join(attribution.split(" ")[-3:]))
	# Get the issues
	tags4pet = [] # Create a sublist for each petition's issues.
	tags = temp_soup.find('section', {"id": "content"}).find_all('h6')
	for elem in tags:
		tags4pet.append(elem.text.encode("utf8"))
	Issues.append(tags4pet)
	# Get the signatures
	Signatures.append(temp_soup.find('span', {"class": "signatures-number"}).text)

All_petitions = [] # A list for all the dictionaries.
# Put everthing together in the dictionaries
for i in range(0, len(petitions)):
	All_petitions.append({"Title": Titles[i], "Published date": Dates[i], "Issue": Issues[i], "Number of signatures": Signatures[i]})

# Write the .csv file
with open('Petitions.csv', 'wb') as f:
  my_writer = csv.DictWriter(f, fieldnames=("Title", "Published date", "Issue", "Number of signatures"))
  my_writer.writeheader()
  for i in range(0, len(petitions)):
    my_writer.writerow({"Title": Titles[i], "Published date": Dates[i], "Issue": Issues[i], "Number of signatures": Signatures[i]})
