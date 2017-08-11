# Create the following functions: with exceptions, errors, and such
# Create a test for those functions

#Hello. to HELLO!
def shout(txt):
	if type(txt) == str:
		if str.isalpha(txt[-1]):
			new_txt = txt.upper()
			new_txt += '!'
			return new_txt
		else:
			new_txt = txt[:-1].upper()
			new_txt += '!'
			return new_txt
	else:
		raise TypeError, "Please enter a string."

	
# Name to emaN  
def reverse(txt):
	if type(txt) == str:
		try:
			if len(txt.split()) != 1:
				raise Exception
			else:
				new_txt = txt[::-1]
				return new_txt
		except:
			raise Exception, "Please use function reversewordletters()"
	else:
		raise TypeError, "Please enter a string."

# Hello world! to world! Hello  
def reversewords(txt):
	if type(txt) == str:
		s = txt.split() # split the string
		s.reverse() # reverse the words
		return " ".join(s)
	else:
		raise TypeError, "Please enter a string."
  
# Hello world! to !dlrow olleH 
def reversewordletters(txt):
	if type(txt) == str:
		try:
			if len(txt.split()) == 1:
				raise Exception
			else:
				new_txt = txt[::-1]
				return new_txt
		except:
			raise Exception, "Please use function reverse()"
	else:
		raise TypeError, "Please enter a string."

# Take a word and transfer to pig latin 

