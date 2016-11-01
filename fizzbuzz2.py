print("Fizz buzz counting up to your number") 
user_number = input("Give me a number: ")
numbers = range(1, (int(user_number) + 1))
for number in numbers:
     if number % 15 == 0:
          print("Fizz Buzz")
     elif number % 3 == 0:
          print("Fizz")
     elif number % 5 == 0:
          print("Buzz")
     else:
          print(number)