#Go to https://polisci.wustl.edu/faculty/specialization
#Go to the page for each of the professors.
#Create a .csv file with the following information for each professor:
# 	-Specialization
# 	-Name
# 	-Title
# 	-E-mail
# 	-Web page
	
from bs4 import BeautifulSoup
import urllib2
import csv
import pdb

# Make the soup
web_address='https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)

# Parse the soup
soup = BeautifulSoup(web_page.read())
soup.prettify()

# Find the each professor
faculty = soup.find_all('strong')

# Define some empty lists for later use.
webpages = []
names = []
emails = []
websites = []
All_faculty = []
Fields = ['American'] * 11 + ['Comparative'] * 13 + ['Formal Theory'] * 5 + ['International Conflict'] *2 + ['International Political Economy'] * 2 + ['Methodology'] * 4 + ['Political Theory'] * 5

# In the "main" page, collect all the titles.
for i in range(0,len(faculty)):
	temp_key = faculty[i].a.text
	names.append(temp_key)
	# find the title
	rawTitle1 = soup.find_all('div', {'class':'view-content'})
	rawTitle2 = rawTitle1[0].find_all('div')
	profs = [x.text for x in rawTitle2]
	titles = [x.split('\n')[2] for x in profs]
	# save individual webpages for each faculty
	if (i == 16) or (i == 32):
		webpages.append("https://polisci.wustl.edu/matthew_gabel")
	else:
		webpages.append("https://polisci.wustl.edu"+faculty[i].a['href'])

# Collect the emails and websites.
for j in webpages:
	temp_page = urllib2.urlopen(j)
	temp_soup = BeautifulSoup(temp_page.read())
	all_as = temp_soup.find_all("a", href= True)
	for a in all_as:
		if "mailto" in a["href"]:
			emails.append(a.get_text())
			break
	else:
		emails.append("NA")
	try:
		useful_block = temp_soup.find('div', {'class':"field field-name-field-person-website field-type-link-field field-label-inline clearfix"})
		websites.append(useful_block.find("a", href = True)['href'])
	except:
		websites.append("NA")

# Put everthing together in the dictionaries.
for i in range(0,len(faculty)):
	temp_key = faculty[i].a.text
	temp_key = {"Name": temp_key, "Specialization": Fields[i], "Title": titles[i], "Email": emails[i], "Website": websites[i]}
	All_faculty.append(temp_key)

# Save everthing to a .csv file.
with open('Faculty_PS_wustl.csv', 'wb') as f:
  my_writer = csv.DictWriter(f, fieldnames=("Name", "Specialization", "Title", "Email", "Website"))
  my_writer.writeheader()
  for i in range(0, len(faculty)):
    my_writer.writerow({"Name": names[i], "Specialization": Fields[i], "Title": titles[i], "Email": emails[i], "Website": websites[i]})