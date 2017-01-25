#variables_test.py
#Testing out some of the basic variables in Python

integer = 5
floater = 5.0
stringer = "five"

print integer, floater, stringer
print "Integer and float fives added: ", (integer + floater), "(", integer, "+", floater, ")"

string2 = string3 = "This is a sentence instead of just a word"
exclaim = "!"; boring = "."

string2 = string2 + boring
string3 += exclaim

print string2
print string3

word1, word2, num1, num2 = "Hello", "World", (4 * 10), 2

print word1, (word2 + exclaim)
print (num1 + num2)

print "\nComplex Arithmetic: "

cnum1, cnum2, cnum3 = (1 + 1j), (2 + 5j), (-3 - 8j)
print "num 1:", cnum1, "num 2:", cnum2, "num 3:", cnum3
print "num1 + num2:", (cnum1 + cnum2)
print "num2 - num3:", (cnum2 - cnum3)
print "num1 * num3:", (cnum1 * cnum3)
print "num3 / num2:", (cnum3 / cnum2)

print "\nString Stuff: "

word = "Python is easy"
print word
print word[0], word[1], word[2]
print word[7:]
print word[0:6]
print word * 2

print "\nList Things: "

listOfNumbers = [1, 2.0, 3, 4, 5.0, 10, 20, 50.0, 100.0, 1000, 9999]
print listOfNumbers, "is my list of numbers"
print "Adding the first two:", (listOfNumbers[0] + listOfNumbers[1])

#tuples are read-only arrays, but who actually cares about performance in python
tupleOfStrings = ("much", "very", "I", "dogs", "like")
print "\n",tupleOfStrings[2], tupleOfStrings[4], tupleOfStrings[3], tupleOfStrings[1], tupleOfStrings[0]

print "\nDictionary Usage: "
dict = {1 : "one", 2 : "two", 3 : "three",  4 : "four", 5 : "five"}
print "My dictionary:", dict
print "My dictionary keys:", dict.keys()
print "My dictionary values:", dict.values()
print dict[1]
print dict[5]