#!/usr/bin/env python3

# Created by: Navin Balekomebole
# Created on: Jan 18 2022
# This program asks the user how many time to loop
# It then uses a loop to get more inputs, to calculate and display the
# sum of all numbers entered.

def main():
    # determine loop and sum variables
    sum = 0
    counter = 0
    display = ("")

    # get the user input
    user_number_string = input("How many numbers would you like to add: ")

    # check inputs
    try:
        user_number = int(user_number_string)
    except Exception:
        print("Invalid input, must be an integer.")
    else:
        # check if number is positive or 0
        if user_number < 0:
            print("Number can't be negative")
        elif user_number == 0:
            print("Sum = {}". format(sum))
        else:
            # calculate the sum of all numbers from 0 to user number
            while counter < user_number:
                user_addition_string = input("Add a number: ")
                # error checking
                try:
                    user_addition = int(user_addition_string)
                except Exception:
                    print("This is an invalid input")
                    continue
                else:
                    if user_addition <= 0:
                        print("number needs be positive")
                        continue
                    sum = sum + user_addition
                    display = user_addition_string + "+" + display
                    counter = counter + 1

            print("")
            print("{} = {}.". format(display, sum))


if __name__ == "__main__":
    main()