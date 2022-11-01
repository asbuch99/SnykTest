# Math helper -- evaluates complex mathematical expressions
 string = input('\nPlease type an expression such as (5* (6+1)) => ')
if not string:
print ("You didn't type anything!")
else:
	print (string," = ", eval(string))
