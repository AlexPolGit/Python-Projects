#loops_test.py
#Testing out loops Python

from random import randint

print "Pick your type of loop:"
print "(1) Count from -> to loop"
print "(2) Count from -> to backwards loop"
print "(3) Guess a random number loop"
print "(4) Iterate a list loop"

choice = 0
while 1:
    choice = int(raw_input("Choice: "))
    if (choice < 1 or choice > 4):
        print "Pick an integer between 1 and 4 please"
    else:
        break

if (choice == 1):

    print "You chose option (1)"
    num_start = int(raw_input("Choose starting number: "))
    num_end = int(raw_input("Choose ending number: "))
    count = int(raw_input("Choose interval size to count by: "))

    for num in range(num_start, num_end + 1, count):
        print num

elif (choice == 2):

    print "You chose option (2)"
    num_start = int(raw_input("Choose a bottom number: "))
    num_end = int(raw_input("Choose a top number: "))
    count = int(raw_input("Choose interval size to count by: "))

    for num in range(num_end, num_start - 1, -count):
        print num

elif (choice == 3):

    print "You chose option (3)"
    num_min = int(raw_input("Pick a min random number: "))
    num_max = int(raw_input("Pick a max random number: "))
    tries = int(raw_input("Pick a number of tries (<1 for infinite): "))
    guess = 0
    rand_num = randint(num_min, num_max)

    if (tries >= 1):
        for attempt in range(0, tries):
            print "Attempt", attempt + 1
            guess = int(raw_input())
            if (guess == rand_num):
                print "You got it!"
                break
    else:
        attempt = 1
        while 1:
            print "Attempt", attempt
            guess = int(raw_input())
            if (guess == rand_num):
                print "You got it!"
                break
            else:
                attempt += 1

elif (choice == 4):

    print "You chose option (4)"
    print "Please enter names into the list and blank to stop"
    name_list = []

    while 1:
        input = raw_input()
        if (input == ""):
            break
        else:
            name_list.append(input)

    name_list.sort()
    print "Sorted name list:"
    for name in name_list:
        print name