# Q1
import sys

# 1. Create a function called return_num_vowels that accepts an 
# input string and returns a dictionary where the keys are the vowels
# a, e, i, o, u, and the values are the count of the vowels.

# write function here
def return_num_vowels(input_str):
    result = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for each in input_str:
        if (each == 'a') or (each == 'A'):
            result['a'] += 1
        elif (each == 'e') or (each == 'E'):
            result['e'] += 1
        elif (each == 'i') or (each == 'I'):
            result['i'] += 1
        elif (each == 'o') or (each == 'O'):
            result['o'] += 1
        elif (each == 'u') or (each == 'U'):
            result['u'] += 1
    
    return result


# 2. Create a function called return_num_characters that counts the number english alpha
# characters in a input string (less spaces, punctuation, numbers, and all other characters not a-z) 
# and returns the count. Hint: review the python built-in functions to find functions that could help.

# write function here
def return_num_characters(input_str):
    result = 0
    
    for each in input_str:
        each = ord(each)
        if (each > 64 and each < 91) or (each > 96 and each < 123):
            result += 1
    
    return result


# 3. Create a function called bar_plot that draws a bar plot taking as input a list of numbers.
# and printing out bars. This function should ignore negative values and floating point values.
#Example:
#bar_plot([1,2,10])
#+
#++
#++++++++++

# write function here
def bar_plot(num_list):
    for num in num_list:
        if int(num) == num:
            if num > 0:
                print('+' * num)


# Q2
import sys
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


# Q3
import random

random.seed(0)
class MyPerfTime:
    elapsed_time=0
    @staticmethod
    def time():
        number=random.randrange(1, 10)
        MyPerfTime.elapsed_time+=number
        return MyPerfTime.elapsed_time-number


# Create the decorator here
def timer(func):
    
    def wrapper():
        print("Testing the performance of '%s'" % func.__name__)
        start = MyPerfTime.time()
        func()
        end = MyPerfTime.time()
        print("Finished '%s' in %.4f secs" % (func.__name__, end - start))
        return func()

    return wrapper
@timer
def function_to_be_tested():
    res=[]
    for i in range(8):
        res.append(str(i))
    return ' '.join(res)

@timer
def second_function_to_be_tested():
    res=[]
    for i in range(12):
        res.append(str(i))
    return ' '.join(res)

print(function_to_be_tested())
print(second_function_to_be_tested())


# Q4
def argument_test_natural_number(f):
    def wrapper(a, b, c):
        if type(a) != Order or type(b) != Order:
            raise Exception()
        
        result = f(a, b, c)
        return result
    return wrapper

def argument_no_negative_value(f):
    def wrapper(self, *args, **kwargs):
        print('I am checking if the %s is higher than 0' % f.__name__)
        for arg in args:
            if arg < 0:
                raise Exception()
        
        result = f(self, *args, **kwargs)
        return result
    return wrapper



class Order:

    # you should leave the constructor unchanged
    def __init__(self, a,b):
        self.price = a
        self.quantity = b

    # now time to play with decorators to declare propoerties slide 14

    # when you create the setter, you need to check if quantity >=0
    # if not you can use assert
    # do the same for price
    # don't forgot that you will certainly need to override __repr__    
    @property
    def price(self):
        return self._price
    
    @property
    def quantity(self):
        return self._quantity
    
    @price.setter
    @argument_no_negative_value
    def price(self, p):
        self._price = p
    
    @quantity.setter
    @argument_no_negative_value
    def quantity(self, q):
        self._quantity = q

    def __repr__(self):
        return '%s(price=%d,quantity=%d)' % (self.__class__.__name__, self.price, self.quantity)




    @staticmethod
    @argument_test_natural_number
    def add_quantity_for_two_orders_and_one_number(a,b,c):
        return a.quantity+b.quantity+c
    
    
x = Order(10,100)
x.quantity=15
x.price=150
print(x)
y = Order(10,100)
y.quantity=13
y.price=16
print(y)

try:
    y.quantity=-100
except:
    print("dammed the quantity was negative")


try:
    y.price=-100
except:
    print("dammed the price was negative")



try:
    print(Order.add_quantity_for_two_orders_and_one_number(100, y, 100))
except:
    print("mistakes after mistakes...I should go to sleep instead of writing tests for my students. 1st argument is an order")


try:
    print(Order.add_quantity_for_two_orders_and_one_number(x, 100, 100))
except:
    print("NO NO STOP THAT -- again an error")


try:
    print(Order.add_quantity_for_two_orders_and_one_number(x, y, 100))
except:
    print("You will never see this code again !")

# Q5
# Complete the 'largestSegment' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY radius
#  2. INTEGER segments
#

def largestSegment(radius, segments):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    radius_count = int(input().strip())

    radius = []

    for _ in range(radius_count):
        radius_item = int(input().strip())
        radius.append(radius_item)

    segments = int(input().strip())

    result = largestSegment(radius, segments)

    fptr.write(result + '\n')

    fptr.close()


# Q6
import re
import sys

poesie_francaise="""Le présent se fait vide et triste,
Ô mon amie, autour de nous ;
Combien peu de passé subsiste !
Et ceux qui restent changent tous.

Nous ne voyons plus sans envie
Les yeux de vingt ans resplendir,
Et combien sont déjà sans vie
Des yeux qui nous ont vus grandir !

Que de jeunesse emporte l'heure,
Qui n'en rapporte jamais rien !
Pourtant quelque chose demeure :
Je t'aime avec mon cœur ancien,

Mon vrai cœur, celui qui s'attache
Et souffre depuis qu'il est né,
Mon cœur d'enfant, le cœur sans tache
Que ma mère m'avait donné ;

Ce cœur où plus rien ne pénètre,
D'où plus rien désormais ne sort ;
Je t'aime avec ce que mon être
A de plus fort contre la mort ;

Et, s'il peut braver la mort même,
Si le meilleur de l'homme est tel
Que rien n'en périsse, je t'aime
Avec ce que j'ai d'immortel.    """
def is_password_allowed(string):
    # you need to validate if a password is correct or not
    # the password policy is the following
    # at least 32 characters
    # it should contain only a-z, A-Z and 0-9
    res = re.match('^[A-Za-z0-9]+$', string)

def find_position_of_a_string(pattern,text):
    # you will return if you found a string the position of this string

def find_all_the_words_with_the_size(n,text):
    # you will find all the words from the string text where the size of these words is n
    

def display_first_word_of_a_line(text):
    # you will just return the first word of a line

def is_it_a_decimal_with_a_precision_of_3(num):
    # you will verify if the preicison is 3 for a number num
def test1():
    print(is_password_allowed("Dammedthispythonclassisnotoverye"))
    print(is_password_allowed("Dammedthispythonclassisnotovery"))
    print(is_password_allowed("Dammedthispythonclassisnoe4324234tovery"))
    print(is_password_allowed("Damme$#dthispythonclassisnoe4324234tovery"))
    print(is_password_allowed("Damme$#dthispythonclassisnoe4324234to@very"))


def test2():
    print(find_position_of_a_string('Christmas','This is close to be Christmas!!'))
    print(find_position_of_a_string('with', 'I will not have any contacts with Python for Thanksgiving'))
    print(find_position_of_a_string('berk', 'I will not have any contacts with Python for Thanksgiving'))

def test3():
    print(find_all_the_words_with_the_size(5,'Python is better than Pytho. Sebas prefers Pytho. It is short'))
    print(find_all_the_words_with_the_size(7,'Christmas without Python is like Santa Claus without gifts'))
    print(find_all_the_words_with_the_size(3, 'Seb will miss all his students for Christmas and he will hope that they will get job'))

    for i in range(2,10):
        print(find_all_the_words_with_the_size(i, poesie_francaise))


def test4():
    print(display_first_word_of_a_line('Python is better than Pytho. Sebas prefers Pytho. It is short'))
    print(display_first_word_of_a_line('Christmas without Python is like Santa Claus without gifts'))
    print(display_first_word_of_a_line( 'Seb will miss all his students for Christmas and he will hope that they will get job'))
    print(display_first_word_of_a_line(poesie_francaise))


def test5():
    print(is_it_a_decimal_with_a_precision_of_3("1.233"))
    print(is_it_a_decimal_with_a_precision_of_3("1.000"))
    print(is_it_a_decimal_with_a_precision_of_3("1.2331"))
    print(is_it_a_decimal_with_a_precision_of_3("seb"))
    print(is_it_a_decimal_with_a_precision_of_3("1.1"))


if __name__ == '__main__':
    test_number = int(input().strip())
    globals()['test'+str(test_number)]()


# Q7
from os import environ
from re import compile
from re import match


#
# Write the regular expression in the blank space below
#
regularExpression = '________'
pattern = compile(regularExpression)

query = int(input())
result = ['False'] * query

for i in range(query):
    someString = input()
    
    if pattern.match(someString):
        result[i] = 'True'

with open(environ['OUTPUT_PATH'], 'w') as fileOut:
    fileOut.write('\n'.join(result))


# Q8
Regex_Pattern = r"_________"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())