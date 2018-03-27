# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""


def loop_ranger(start, stop=None, step=1):
   
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    a_list = []
    counter = start
    while counter < stop:
            a_list.append(counter)
            counter += step
    return a_list


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    a_list = []
    counter = start
    while counter < stop:
            a_list.append(counter)
            counter += step
    return a_list


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    a_list = []
    counter = start
    while counter < stop:
            a_list.append(counter)
            counter += 2
    return a_list


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    while True: 
        a_number = int(input())
        if a_number < low or a_number > high:
            print ("Incorrect, Pick another Number")
        else:
            return a_number



def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    while True:
        try:
            a_number = int(input(message))
            return a_number
        except ValueError:
            print("That's not a number, Try again")
            continue
        except TypeError:
            print("That's not a number, Try again")
            continue


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    message = "Give me a number between {low}, and {high}:".format(low=low,high=high)
    while True:
        try:
            input_number = int(input(message))
            if low < input_number < high:
                print("{} looks good.".format(input_number))
                return input_number
        except Exception as e:
            print("try again ({})".format(e))
            
        else:
            print("{input} isn't between {low}, {high}".format(input=input_number, low=low, high=high))


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
