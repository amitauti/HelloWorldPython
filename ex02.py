# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# Ask the user for a number. Depending on whether the number is even or
# odd, print out an appropriate message to the user.

import sys

def main():
    askuser ()

def askuser():
    #part one
    str = input("Enter a number: ")
    num = int(float(str))
    newnum = num % 2
    if newnum == 0:
        print ("It is even number")
    else:
        print ("It is odd number")

    #part two
    num = num % 4
    if num == 0:
        print (" and divisible by 4 as well!")

    #part three
    str1 = input("Give me a number as numerator ")
    str2 = input("Give me a number as denomitor ")
    num_one = int(float(str1))
    num_two = int(float(str2))

    if num_two == 0:
        print("We can not devide by zero")
        sys.exit()
    else:
        if num_one % num_two == 0:
            print("It is a even number")
        else:
            print ("It is a odd number")


if __name__ == '__main__':
    main()
