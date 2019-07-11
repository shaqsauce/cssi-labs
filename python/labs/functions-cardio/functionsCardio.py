print("Welcome to Nalani's Function Cardio")

num1 = int(raw_input("Give me side 1 length: "))
num2 = int(raw_input("Give me side 2 length: "))
num3 = int(raw_input("Give me side 3 length: "))

def is_triangle(s1, s2, s3):
    sum1 = s1 + s2 #test if greater than s3
    sum2 = s2 + s3 #test if greater than s1
    sum3 = s3 + s1 #test if greater than s2
    if sum1> s3 and sum2> s1 and sum3> s2:
        print("You have a triangle")
        return True #I have a is triangle
    else:
        print("You don't have a triangle")
        return False #not a Triangle

is_triangle(num1, num2, num3)
