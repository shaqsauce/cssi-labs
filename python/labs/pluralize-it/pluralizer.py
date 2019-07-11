print("Whats Good, Welcome to my Pluralizer")
word1 = raw_input("Enter a Word: ")
number1= int(raw_input("Enter Number: "))

if number1 > 1:
    print(str(number1) + " " +word1 + "s")
elif number1 == 0:
    print(str(number1) + " " +word1 + "s")

else:
    print(str(number1) + " " +word1)
