import re
import inspect

check = lambda r , line: "Success" if (r) else ("Fail at: line %d") % (line)


#%%%%%%%%%%%%%%%%%%%

#====================================================================
'''  
# [Case] regex_1
# Instruction : 
#   Guess search result
#
str = 'an example word:cat!! word:dog!! word:zebra!!'
match = re.search(r'word:\w\w\w', str)

# Add your code bellow
guess_result = 

# [Check]
print "======================================="
print check(guess_result == match.group(), inspect.currentframe().f_lineno)
'''
#====================================================================


 
#====================================================================
'''  
# [Case] regex_2
# Instruction : 
#   Guess search result
#
match = re.search(r'iii', 'piiig')
# Add your code bellow
guess_result =  ""

# [Check]
print "======================================="
print check(guess_result == match.group(), inspect.currentframe().f_lineno)
'''
#====================================================================

#====================================================================
'''  
# [Case] regex_3
# Instruction : 
#   Guess search result  -- "" stand for can't find
#
match = re.search(r'igs', 'piiig')
# Add your code bellow
guess_result = ""

# [Check]
print "======================================="
print check(guess_result == "", inspect.currentframe().f_lineno)
'''
#====================================================================

#====================================================================
'''  
# [Case] regex_4
# Instruction : 
#   Guess search result  -- "" stand for can't find
#
match = re.search(r'..g', 'piiig')
# Add your code bellow
guess_result =  ""

# [Check]
print "======================================="
print check(guess_result == match.group(), inspect.currentframe().f_lineno)
'''
#====================================================================

#====================================================================
'''  
# [Case] regex_5
# Instruction : 
#   Guess search result  -- "" stand for can't find
#
match = re.search(r'\d\d\d', 'p123g')
# Add your code bellow
guess_result =   ""

# [Check]
print "======================================="
print check(guess_result == match.group(), inspect.currentframe().f_lineno)
'''
#====================================================================


#====================================================================
'''  
# [Case] regex_6
# Instruction : 
#   Guess search result  -- "" stand for can't find
#
match = re.search(r'\w\w\w', '@@abcd!!')
# Add your code bellow
guess_result =   ""

# [Check]
print "======================================="
print check(guess_result == match.group(), inspect.currentframe().f_lineno)
'''
#====================================================================

#====================================================================
'''  
# [Case] regex_7
# Instruction : 
#   Guess search result  -- "" stand for can't find
#
match = re.search(r'pi+', 'piiig')
# Add your code bellow
guess_result = ""

# [Check]
print "======================================="
print check(guess_result == match.group(), inspect.currentframe().f_lineno)
'''
#====================================================================

#====================================================================
'''  
# [Case] regex_8
# Instruction : 
#   Guess search result  -- "" stand for can't find
#      \s* = zero or more whitespace chars
#      Here look for 3 digits, possibly separated by whitespace.
#
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')
# Add your code bellow
guess_result =  ""

# [Check]
print "======================================="
print check(guess_result == match.group(), inspect.currentframe().f_lineno)
'''
#====================================================================


#====================================================================
'''  
# [Case] regex_9
# Instruction : 
#   Guess search result  -- "" stand for can't find
#
match = re.search(r'\d\s*\d\s*\d', 'xx123xx')
# Add your code bellow
guess_result =  ""
# [Check]
print "======================================="
print check(guess_result == match.group(), inspect.currentframe().f_lineno)
'''
#====================================================================

#====================================================================
'''  
# [Case] regex_10
# Instruction : 
#   Guess search result  -- "" stand for can't find
#
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
# Add your code bellow
guess_result = ""

# [Check]
print "======================================="
print check(guess_result == match.group(), inspect.currentframe().f_lineno)
'''
#====================================================================


#====================================================================
'''  
# [Case] regex_12
# Instruction : 
#   Guess search result  -- () is used for group
#
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search('([\w.-]+)@([\w.-]+)', str)
# Add your code bellow

#  Guess match.group()
guess_result =   ""

#  Guess match.group(1)
guess_result1 =   ""

#  Guess match.group(2)
guess_result2 =  ""

# [Check]
print "======================================="
print check(guess_result == match.group(), inspect.currentframe().f_lineno)
print check(guess_result1 == match.group(1), inspect.currentframe().f_lineno)
print check(guess_result2 == match.group(2), inspect.currentframe().f_lineno)
'''
#====================================================================


#====================================================================
'''  
# [Case] regex_13
# Instruction : 
#   Guess search result  -- findall
#
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
result = re.findall(r'[\w\.-]+@[\w\.-]+', str)
# Add your code bellow
guess_result = []
 
# [Check]
print "======================================="
print check(guess_result == result, inspect.currentframe().f_lineno)
'''
#====================================================================


#====================================================================
'''  
# [Case] regex_14
# Instruction : 
#   Guess search result  -- findall
#
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
result = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
# Add your code bellow
guess_result = []

# [Check]
print "======================================="
print check(guess_result == result, inspect.currentframe().f_lineno)
'''
#====================================================================

#====================================================================
'''  
# [Case] regex_15
# Instruction : 
#   Guess search result  --  
#       re.sub(pat, replacement, str) -- returns new string with all replacements,
#       \1 is group(1), \2 group(2) in the replacement
#
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
result = re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)
# Add your code bellow
guess_result = ""

# [Check]
print "======================================="
print check(guess_result == result, inspect.currentframe().f_lineno)
'''
#====================================================================



















'''
[Case] regex_13
guess_result = ["alice@google.com", "bob@abc.com"]

[Case] regex_14
guess_result = [('alice', 'google.com'), ('bob', 'abc.com')] 

[Case] regex_15
guess_result = "purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher"

'''


























































































