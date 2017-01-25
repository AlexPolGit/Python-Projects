#operators_test.py
#Testing out some of the basic operators in Python

numbers = (45.7, 32.5)
print "\nMy numbers:", numbers
print "Operations are to be done as num1 [operator] num2...\n"

#Mathematical
print "Added:", numbers[0] + numbers[1]
print "Subtracted:", numbers[0] - numbers[1]
print "Multiplied:", numbers[0] * numbers[1]
print "Divided:", numbers[0] / numbers[1]
print "Powered:", numbers[0] ** numbers[1]
print "Modulus-ed:", numbers[0] % numbers[1]
print "Floor Divided:", numbers[0] // numbers[1]

numbers2 = (15, 84)
print "\nMy second numbers:", numbers2, "\n"

#Bitwise
print "ANDed:", numbers2[0] & numbers2[1]
print "ORed:", numbers2[0] | numbers2[1]
print "XORed:", numbers2[0] ^ numbers2[1]
print "Left Bitshifted num1:", numbers2[0] << 1
print "Right Bitshifted num1:", numbers2[0] >> 1