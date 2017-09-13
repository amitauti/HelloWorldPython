# This is tutorial from http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Create a program that asks the user to enter their name and their age. Print out a message addressed
#  to them that tells them the year that they will turn 100 years old.

from datetime import date
from time import time

def main():
    name = get_name()
    age = get_age()
    bday_yet = birtday_yet()
    year = get_year(int(age), bday_yet)

    if year == 'greater':
        print("You are already 100 years old")
    else:
        print("Hello" )
