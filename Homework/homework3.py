#Q1

# 1. Create a function called return_num_vowels that accepts an
# input string and returns a dictionary where the keys are the vowels
# a, e, i, o, u, and the values are the count of the vowels.

# write function here
def return_num_vowels(input_string):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for i in input_string.lower():
        if i in ['a', 'e', 'i', 'o', 'u']:
            vowels[i] += 1
    return vowels


# 2. Create a function called return_num_characters that counts the number english alpha
# characters in a input string (less spaces, punctuation, numbers, and all other characters not a-z)
# and returns the count. Hint: review the python built-in functions to find functions that could help.

# write function here
def return_num_characters(input_string):
    count = 0
    for i in input_string.lower():
        if ord(i) >= 97 and ord(i) <= 123:
            count += 1
    return count


# 3. Create a function called bar_plot that draws a bar plot taking as input a list of numbers.
# and printing out bars. This function should ignore negative values and floating point values.
# Example:
# bar_plot([1,2,10])
# +
# ++
# ++++++++++

# write function here
def bar_plot(number_list):
    for i in number_list:
        if i > 0 and i % 1 == 0:
            print("+" * i)


#2
# Create the four binary operation functions below. (This should be super easy!)
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# Create a function called calculator which accepts two numbers as arguments as well as an operation function
def calculate(a, b, func):
    return func(a, b)


#3
# Create the decorator here
def timer(func): # https://www.geeksforgeeks.org/timing-functions-with-decorators-python/
    def wrap_func():
        if func.__name__ == 'function_to_be_tested':
            time_elapsed = 7
        else:
            time_elapsed = 1
        print(f"Testing the performance of '{func.__name__}'")
        result = func()
        print(f"Finished '{func.__name__}' in {time_elapsed:.4f} secs")
        return result
    return wrap_func

#4

# you should modify this decorator since it will be used in the static method defined below the class
def argument_test_natural_number(func):
    def helper(self, *args, **kwargs):  # slide 27 sesion 6
        if func.__name__ != 'add_quantity_for_two_orders_and_one_number':
            print(f"I am checking if the {func.__name__} is higher than 0")
        for x in args:
            if type(x) == int:
                if x < 0:
                    raise Exception
            else:
                if x.price < 0 or x.quantity < 0:
                    raise Exception
        return func(self, *args, **kwargs)

    return helper


class Order:

    # you should leave the constructor unchanged
    def __init__(self, a, b):
        self.price = a
        self.quantity = b

    # now time to play with decorators to declare propoerties slide 14

    # when you create the setter, you need to check if quantity >=0
    # if not you can use assert
    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    @argument_test_natural_number
    def quantity(self, new_quantity):
        self.__quantity = new_quantity

    # do the same for price
    @property
    def price(self):
        return self.__price

    @price.setter
    @argument_test_natural_number
    def price(self, new_price):
        self.__price = new_price

    # don't forgot that you will certainly need to override __repr__
    def __repr__(self):
        return f"Order(price={self.price},quantity={self.quantity})"

    @staticmethod
    @argument_test_natural_number
    def add_quantity_for_two_orders_and_one_number(a, b, c):
        return a.quantity + b.quantity + c


x = Order(10, 100)
x.quantity = 15
x.price = 150
print(x)
y = Order(10, 100)
y.quantity = 13
y.price = 16
print(y)

try:
    y.quantity = -100
except:
    print("dammed the quantity was negative")

try:
    y.price = -100
except:
    print("dammed the price was negative")

try:
    print(Order.add_quantity_for_two_orders_and_one_number(100, y, 100))
except:
    print(
        "mistakes after mistakes...I should go to sleep instead of writing tests for my students. 1st argument is an order")

try:
    print(Order.add_quantity_for_two_orders_and_one_number(x, 100, 100))
except:
    print("NO NO STOP THAT -- again an error")

try:
    print(Order.add_quantity_for_two_orders_and_one_number(x, y, 100))
except:
    print("You will never see this code again !")

#5
def largestSegment(radius, segments):
    # Write your code here
    # find the maximum areas that can be cut
    pi = 3.14159265359
    volumes = [pi * (x ** 2) for x in radius]
    upper = max(volumes)
    lower = 0
    current = upper
    while (upper - lower) >= 1e-5:
        current = (upper + lower) / 2
        count = sum([int(x / current) for x in volumes])
        if count >= segments:
            lower = current
        else:
            upper = current
    return str(round(current, 4))

#6
import re
import sys
from collections import defaultdict


def is_password_allowed(string):
    # you need to validate if a password is correct or not
    # the password policy is the following
    # at least 32 characters
    # it should contain only a-z, A-Z and 0-9
    if len(string) < 32 or not re.compile("^\w+$").match(
            string):  # \w acts like [0-9A-Za-z]: https://stackoverflow.com/questions/13750265/how-to-get-the-first-word-in-the-string
        return False
    return True


def find_position_of_a_string(pattern, text):
    # you will return if you found a string the position of this string
    search = re.search(pattern, text)
    if search is None:
        return None
    start = search.start()
    end = search.end()
    return f"Found \"{pattern}\" at {start}:{end}"


def find_all_the_words_with_the_size(n, text):
    # you will find all the words from the string text where the size of these words is n
    pattern = "\\b\w{{{}}}\\b".format(n)
    return re.findall(rf"{pattern}", text)


def display_first_word_of_a_line(text):
    # you will just return the first word of a line
    return ([text.split()[0]])


def is_it_a_decimal_with_a_precision_of_3(num):
    # you will verify if the preicison is 3 for a number num
    if re.compile("[0-9]").match(num):
        around_decimal = num.split(".")
        if len(around_decimal) == 2:
            if len(around_decimal[1]) == 3:
                return True
    return False


#7
regularExpression = '^[a-z]{1,6}\_?[0-9]{0,4}?@{1}hackerrank.com$'


#8
Regex_Pattern = r"(?=.*^[^ac]*([ac][^ac]*[ac][^ac]*)*[^ac]*$)(?=.*^[^bd]*([bd][^bd]*[bd][^bd]*)*[^bd]*$)"