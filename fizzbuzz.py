"""
// Project requirements:

-Have a hard-coded upper line, n.

-Print "Fizz buzz counting up to n", substituting in the number 
we'll be counting up to.

-Print out each number from 1 to n, replacing with Fizzes and 
Buzzes as appropriate.

-Print the digits rather than the text representation of the number 
(i.e. print 13 rather than thirteen).

-Each number should be printed on a new line.

""" 

print("Fizz buzz counting up to 100") 
numbers = range(1, 101)
for number in numbers:
     if number % 15 == 0:
          print("Fizz Buzz")
     elif number % 3 == 0:
          print("Fizz")
     elif number % 5 == 0:
          print("Buzz")
     else:
          print(number)