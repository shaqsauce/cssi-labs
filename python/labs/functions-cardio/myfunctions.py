print("My calcc")
def count_spaces(s):
    return s.count(" ")

def count_vowels(s):
    numA = s.count("a")
    numE = s.count("e")
    numI = s.count("i")
    numO = s.count("o")
    numU = s.count("u")
    numY = s.count("y")
    sumVowels = numA + numE + numO + numI + numU + numY

    return sumVowels

def count_total(s):
    return count_spaces(s) + count_vowels(s)

print(count_vowels("Aye u, u suck bruh."))

countNum = count_vowels("Aye u, u suck bruh.")
print(countNum)
