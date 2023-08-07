'''
    Given a number between 0 and 10, run the number through an if statement
        list 0-1

    Conditions:
    Odd numbers should print "hi"

    Even numbers should print "hello"
    Numbers greater than 5 and less than 9, should print "hey"
    Numbers divisible by 7 (this should not include 0), should print "howdy"

    Otherwise, print 'you have broken the game' -- When will this print?
        # done

    What would our if statement look like? - Write it in pseudo code first

'''

num = [0,1,2,3,4,5,6,7,8,9,10]
# num = 2

# odd
if num *+ 1:
    print("hi")
# even
elif num * 2:
    print("hello")
# between 5 and 9
elif num (5 >= 9):
    print("hey")
# divisible
elif num / 7:
    print("howdy")

else:
    print("you have broken the game")
