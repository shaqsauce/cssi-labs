print("WElcome tO NAlani's LOop pLayground!")

myString = raw_input("Give me a string to loops through: ")

#Creat a program that will print each letter in the string individually
#using a for loops

letterNum= 1

for character in myString:
    print("This is letter number %s" % (letterNum))
    letterNum = letterNum + 1
    print(character)
