import inspect



frame = inspect.currentframe()

VarStr1 = 'Beautiful Soup is a Python library for pulling data out of HTML and XML files.'


#====================================================================
'''  
# [Case] basic_string_extract_first_char
# Instruction : 
#   Get FRIST char of var_str , stroe it in var 'answer'
#

var_str = 'Python Programming'
answer = ""
# Add your code bellow


# [Check]
print answer
print "======================================="
if 'P' == answer:
    print "Success"
else:
    print "Fail at: line %d" % (frame.f_lineno)
'''
#====================================================================


#====================================================================
'''  
# [Case] basic_string_subtract_string
# Instruction : 
#   Extract 'Python' from var_str, 
#
var_str = 'Python Programming'
answer = ""
# Add your code bellow
answer =  

# [Check]
print answer
print "======================================="
if 'Python' == answer:
    print "Success"
else:
    print "Fail at: line %d" % (frame.f_lineno)
'''
#====================================================================
 
 
#====================================================================
'''  
# [Case] basic_string_in_for_str
# Instruction : 
#   Test whether str 'brary' is in 'VarStr1'
#

# Add your code bellow
answer =  

# [Check]
print answer
print "======================================="
if  True == answer:
    print "Success"
else:
    print "Fail at: line %d" % (frame.f_lineno)
 
'''
#====================================================================
 

#====================================================================
'''  
# [Case] basic_string_not_in_for_str
# Instruction : 
#   Test whether str 'yuv' is NOT in 'VarStr1'
#
#Add your code bellow
answer =

# [Check]
print answer
print "======================================="
if  True == answer:
    print "Success"
else:
    print "Fail at: line %d" % (frame.f_lineno)
 
'''
#====================================================================
 
 
#====================================================================
'''  
# [Case] basic_string_triple_quotes
# Instruction : 
#   Try & See
#   When the above code is executed, it produces the following result. 
#   Note how every single special character has been converted to its 
#   printed form,

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""

print para_str
 
'''
#====================================================================
 
 
 
 
######################################################################
'''
1) basic_string_extract_first_char
answer = var_str[0]


2) basic_string_subtract_string
answer = var_str[:6]

3) basic_string_in_for_str
answer = 'brary' in VarStr1

3) basic_string_not_in_for_str
answer = 'brary' in VarStr1

'''







