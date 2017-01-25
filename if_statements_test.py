#if_statements_test.py
#Testing out if, else, elif statements in Python, very simple

num = int(raw_input("Give me a number between 1 and 100: "))

if (num < 1):
    print "This is below 1, too low!"
elif (num > 100):
    print "This is above 100, too high!"
else:
    print "Your number was", num
    if (num == 1):
        print "This is the lowest you could have picked!"
    elif (num == 100):
        print "This is the highest you could have picked!"
    else:
        print "You actually picked something interesting congrats!"
