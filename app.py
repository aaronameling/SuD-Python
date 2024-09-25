#   10 (Numbers) can be in(10) or float(10.1)
#   "Mosh" (Strings)
#   True/False (Booleans)
from itertools import count

#   birth_year = input("Enter your birth year: ")
#   age = 2024 - int(birth_year)
#   print(age)
#
#   int(10)
#   float(10.1)
#   bool(True/False)
#   str(sum/second/first)

first = input("Enter First number between 0-30: ")
second = input("Enter Second number between 0-30: ")
sum = float(first) + float(second)
print(sum)


#   first = float(input("Enter First number: "))
#   second = float(input("Enter Second number: "))
#   sum = first + second
#   print("Sum: " + str(sum))

#   course = 'Python for Beginners'
#   print('Python' in course)


#   Operators:
#   >
#   >=
#   <
#   <=
#   ==
#   !=

#   price = 5
#   print(price > 10 or price < 30)

#   and (both)
#   or (at least one)
#   not (inverses any value when be given)


temperature = sum

if temperature > 30:
  print("It's a hot day")
  print("Drink plenty of water")
elif temperature > 20:
  print("It's a nice day")
elif temperature > 10:
  print("It's a bit cold")
else:
  print("It's cold")
print("Done")


weight = float(input("Enter your weight: ")) # Das input wird in ein float(number) element gepackt damit ist als number wahrgenommen wird und nicht als str(string)
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45 # Hier wird das weight geteilt durch die zahl: 0.45(welche eine [float] number ist). das geht nur weil weigth auch zu einer number gemacht wurde und kein str(string) mehr ist.
    print("Weight in Lbs: " + str(converted)) # print ist die ausgabe in der console. hier soll "Weight in Lbs: " was ein str(string) ist, mit der zahl die mkt converted gleichgestzt ist ausgegeben werden,
else:                                         # aber converted ist eine number und numbers und strings sind nicht kompatible deswegen wird converted in ein str() tag gepackt.
    converted = weight * 0.45
    print("Weight in Kg: " + str(converted))



# i = 1
# while i <= 10:
#     print(i * '*')
#     i = i + 1

# names = ["John", "Bob", "Mosh", "Sam", "Mary"]
# names[0] = "Jon"
# print(names[0:3])
# print(names)

# numbers = range(0, 50, 5)
# for number in numbers:
#     print(number)


# numbers = (1, 2, 3, 3)
# print(numbers.count(3))



    