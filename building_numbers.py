"""The given code is used to generate an n-digit number from a list of n-digits
    For example: for an input list of [8,3,1,0], the program outputs the integer number 8310"""


def build_number(number_of_digits: int, list_of_digits: list) -> int:
    """This method creates an n-digit integer number from a list of n integers
    Parameters:
        number_of_digits: Integer value representing number of digits in list or length of list
        list_of_digits: List of digits to be used to creatye number
    ReturnValue:
        number: An integer created using the given digits in the list"""
    number = 0
    remaining_digits = number_of_digits
    while remaining_digits > 0:
        number += (list_of_digits[number_of_digits - remaining_digits]) * (10 ** (remaining_digits - 1))
        remaining_digits -= 1

    return number


def input_list_of_numbers(number_of_digits:int)->list:
    """This method takes the digits as input from the user and validates their values
    Parameters:
        number_of_digits: An integer value representing the number of digits that the user wants to input
    ReturnValue:
        list_of_digits: List containing all the digits entered by the user"""
    list_of_digits = []
    print("Enter single digit numbers between 0 and 9 one by one:")
    i = 1
    while i <= n:
        try:
            digit = input(f"Digit {i}-> ")
            assert digit.isdigit(), "Enter a valid integer number!"
            assert 0 <= int(digit) <= 9, "Enter a valid integer number between 0 and 9!"
            list_of_digits.append(int(digit))
            i += 1
        except AssertionError as e:
            print("Error!", e)

    return list_of_digits

if __name__ == "__main__":

    while True:
        try:
            n = input("Enter number of digits you would like to provide:\n")
            assert n.isdigit(), "Enter valid integer number!"
            n = int(n)
            list_of_digits = input_list_of_numbers(n)
            print("Number generated = ", build_number(n, list_of_digits))
            break
        except AssertionError as e:
            print(e)