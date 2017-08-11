#Write a function that takes an integer as an input and returns a script with the ordinal number
#For example, for 1, it should give "1st"
#Write a test for your function

def myfunction(entry):
	if type(entry) == int:
	    if len(str(entry)) == 1:
	    	if entry == '1': 
	    		return '1st'
	        elif entry == '2': 
	        	return '2nd'
	        elif entry == '3': 
	        	return '3rd'
	        else: 
	        	return '%sth' %(entry)
	    else:
	    	entry = str(entry)
   		    if entry[-2] == '1':
  			    return "%sth" %(entry)
   		    elif entry[-1] == '1':
   			    return "%sst" %(entry)
   		    elif entry[-1] == '2':
   			    return "%snd" %(entry)
   		    elif entry[-1] == '3':
   			    return "%srd" %(entry)
   		    else:
   			    return  "%sth" %(entry)
    else:
        return "Please enter an integer."


print myfunction(1)	
