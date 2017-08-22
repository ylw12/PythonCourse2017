import re

# open text file of 2008 NH primary Obama speech
file = open("obama-nh.txt", "r")
text = file.readlines()
file.close()

# compile the regular expression
keyword = re.compile(r"the ")

# search file for keyword, line by line
for line in text:
  if keyword.search(line):
    print line 

# TODO: print all lines that DO NOT contain "the "
for line in text:
  if not keyword.findall(line):
    print line 

# TODO: print lines that contain a word of any length starting with s and ending with e
pattern = re.compile(r'\b[Ss]\w*e\b') 
for line in text:
	if pattern.findall(line):
		print line

date = raw_input("Please enter a date in the format MM.DD.YY: ")
pattern = re.compile(r'(\d\d)\.(\d\d)\.(\d\d)')
print 'Month: %s \nDay: %s \nYear: %s' %(pattern.search(date).group(1), pattern.search(date).group(2), pattern.search(date).group(3))


# Print the date input in the following format:
# Month: MM
# Day: DD
# Year: YY


