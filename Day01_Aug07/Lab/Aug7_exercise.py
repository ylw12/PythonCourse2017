# Practice 1
def has_no_e(word):
	"""return true or false if there is no e in 'word"""

# Patrick_S
def has_letter_e(self):
    letter = [letter for letter in self]
    if "e" in letter:
      return True
    else:
      return False
x = "home"
y = "car"
z = "University"

print has_letter_e(x)
print has_letter_e(y)
print has_letter_e(z)

# Patrick_R
def test_has_no_e(x):
    if "e" not in x:
        print "TRUE"
    else:
        print "FALSE"

# Practice 2
"""convert positive integer to base 2"""
def binarify(num):
    if num <= 0: return "0" 
    s = ''
    while num:
        if num % 2 == 1:
            s = "1" + s
        else:
            s = "0" + s
        num /= 2
    return s

# Why this does not work?
def binarify(num):
	digits = [str(num%2)]
	while num > 0: 
	    num /= 2
	    digits.append(str(num%2))
	return ''.join(digits[::-1])

"""convert positive integer to a string in any base"""
def int_to_base(num, base):
    if num <= 0: return "0"
    s = ''
    while num:
        if num % base == 1:
            s = "1" + s
        else:
            s = "0" + s
        num /= base
    return s

"""take a string-formatted number and its base and return the base-10 integer"""
def base_to_int(string, base):
    if string=="0" or base <= 0 : return 0 
    result = 0
    for i in range(1, len(string)+1):
    	result += int(string[-i]) * base ** (i-1)
    return result

"""add two numbers of different bases and return the sum"""
def flexibase_add(str1, str2, base1, base2):
	result = base_to_int(str(str1), base1) + base_to_int(str(str2), base2)
	return result

"""multiply two numbers of different bases and return the product"""
def flexibase_multiply(str1, str2, base1, base2):
	result = base_to_int(str(str1), base1) * base_to_int(str(str2), base2)
	return result

"""given an integer, return the Roman numeral version"""
num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def romanify(num):
    roman = ''
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i
    return roman

# test 
romanify(2242)
'MMCCXLII'



