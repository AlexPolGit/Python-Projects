#strings_test.py
#Testing out string functions Python

string = "python is a programming language"

print "\nOriginal string:"
print string

print "\nAs a sentence:"
print string.capitalize() + "!"

print "\nLength of string:"
print len(string)

print "\nNumber of g's: "
print string.count("g")

print "\nIs alphabetic? Is numeric? Is alphanumeric?"
print string.isalpha(), string.isdigit(), string.isalnum()

print "\nUppercase all:"
print string.upper()

print "\nTitle-cased:"
print string.title()

print "\nBack to lower:"
print string.lower()

print "\nSplit into words:"
for word in string.split(" "):
    print word