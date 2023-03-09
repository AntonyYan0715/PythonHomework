# 3.1
import sys

# 1. Create a function called return_num_vowels that accepts an 
# input string and returns a dictionary where the keys are the vowels
# a, e, i, o, u, and the values are the count of the vowels.

# write function here
def return_num_vowels(strings):
    n = len(strings)
    res = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for i in range(n):
        if strings[i].lower() in res.keys():
            res[strings[i].lower()] += 1
    return res
            

# 2. Create a function called return_num_characters that counts the number english alpha
# characters in a input string (less spaces, punctuation, numbers, and all other characters not a-z) 
# and returns the count. Hint: review the python built-in functions to find functions that could help.

# write function here
def return_num_characters(strings):
    repo = set(list('abcdefghijklmnopqrstuvwxyz'))
    n = len(strings)
    res = 0
    # s.isalpha() cant distinguish beta from [a-z]
    for i in range(n):
        if strings[i].lower() in repo:
            res += 1
    return res


# 3. Create a function called bar_plot that draws a bar plot taking as input a list of numbers.
# and printing out bars. This function should ignore negative values and floating point values.
#Example:
#bar_plot([1,2,10])
#+
#++
#++++++++++
def bar_plot(list_arg):
    list_arg = list(list_arg)
    n = len(list_arg)

    for i in range(n):
        if isinstance(list_arg[i], int) and list_arg[i] > 0:
            print('+'*list_arg[i])

# write function here
    

def case_vowel_count(string_arg):
    string_arg = ' '.join(string_arg)
    vowel_count = return_num_vowels(string_arg)
    sys.stdout.write(f"a {vowel_count['a']}\n")
    sys.stdout.write(f"e {vowel_count['e']}\n")
    sys.stdout.write(f"i {vowel_count['i']}\n")
    sys.stdout.write(f"o {vowel_count['o']}\n")
    sys.stdout.write(f"u {vowel_count['u']}\n")
                     

def case_character_count(string_arg):
    string_arg = ' '.join(string_arg)
    character_count = return_num_characters(string_arg)
    sys.stdout.write(str(character_count))
                     
def case_bar_plot(list_arg):
    list_arg = map(int, list_arg[0].split(' '))
    bar_plot(list_arg)
                     
                     
if __name__ == '__main__':
    test_func_name = sys.stdin.readline().strip()
    test_func = globals()[test_func_name]
    arg = sys.stdin.readlines()
    test_func(arg)


# 3.2
import sys

# Create the four binary operation functions below. (This should be super easy!)
def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a,b):
    return a/b if b!=0 else None

# Create a function called calculator which accepts two numbers as arguments as well as an operation function
def calculate(arg1, arg2, func):
    return func(arg1, arg2)

if __name__ == '__main__':
    arg1 = int(sys.stdin.readline().strip())
    arg2 = int(sys.stdin.readline().strip())
    funcs = [add, subtract, multiply, divide]
    for func in funcs:
        sys.stdout.write(str(calculate(arg1, arg2, func))+'\n')


# 3.3
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
    def wrapper(*args, **kwargs):
        print(f"Testing the performance of '{func.__name__}'")
        start = MyPerfTime.time()
        f = func(*args, **kwargs)
        end = MyPerfTime.time()
        print(f"Finished '{func.__name__}' in {(end-start):.4f} secs")
        return f
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


# 3.4
# you should modify this decorator since it will be used in the static method defined below the class
def argument_test_natural_number(f):
    def wrapper(x,y,z):
        if not (isinstance(x, Order) and isinstance(y, Order)):
            raise Exception()
        res = f(x,y,z)
        return res
    return wrapper

def argument_protector(func):
    def wrapper(self, *args):
        print(f'I am checking if the {func.__name__} is higher than 0')
        for arg in args:
            assert arg >= 0
        res= func(self, *args)
        return res
    return wrapper

class Order:

    # you should leave the constructor unchanged
    def __init__(self, a,b):
        self.price = a
        self.quantity = b
        
    @property
    def price(self):
        return self._price
    @property
    def quantity(self):
        return self._quantity
    # now time to play with decorators to declare propoerties slide 14
    
    
    @price.setter
    @argument_protector
    def price(self, new_price):
        # assert new_price >=0
        self._price = new_price
    
    
    @quantity.setter
    @argument_protector
    def quantity(self, new_quantity):
        # assert new_quantity >= 0
        self._quantity = new_quantity
    # when you create the setter, you need to check if quantity >=0
    # if not you can use assert
    # do the same for price
    # don't forgot that you will certainly need to override __repr__    
    
    def __repr__(self):
        return f"{self.__class__.__name__}(price={self.price},quantity={self.quantity})"




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


# 3.5
import math
def f(x,sizes, segments):
    
    k = 0
    for a in sizes:
        k += a // x
        if k >= segments:
            return True
    return False

def largestSegment(radius, segments):
    # Write your code here

    sizes = [math.pi * r * r for r in radius]
    
    left = 0
    right = max(sizes)
    
    while left + 1e-5 <= right:
        
        x = (left + right) / 2
        if f(x,sizes, segments):
            left = x
        else:
            right = x
            
    return str(round(x, 4))

# 3.6
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
    pattern = '\w{32}\w*'
    res = re.match(pattern, string)
    return False if res is None else True

def find_position_of_a_string(pattern,text):
    res = re.search(pattern, text)
    if res is None:
        return None
    else:
        return f"Found \"{pattern}\" at {res.span()[0]}:{res.span()[1]}"
    # you will return if you found a string the position of this string

def find_all_the_words_with_the_size(n,text):
    poss = re.split('\W+', text)
    res = []
    for j in poss:
        if len(j) == n:
            res.append(j)
    return res
    # you will find all the words from the string text where the size of these words is n
    

def display_first_word_of_a_line(text):
    return [re.search('\w+', text).group()]
    # you will just return the first word of a line

def is_it_a_decimal_with_a_precision_of_3(num):
    pattern = '\d+\.\d{3}$'
    res = re.match(pattern, num)
    if res is None:
        return False
    # if res.span()[1] == len(num):
    #     return True
    else:
        return True
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


# 3.7

#!/bin/python3

from os import environ
from re import compile
from re import match


#
# Write the regular expression in the blank space below
#
regularExpression = '([a-z]{1,6})_?([0-9]{0,4})@hackerrank.com'
pattern = compile(regularExpression)

query = int(input())
result = ['False'] * query

for i in range(query):
    someString = input()
    
    if pattern.match(someString):
        result[i] = 'True'

with open(environ['OUTPUT_PATH'], 'w') as fileOut:
    fileOut.write('\n'.join(result))



# 3.8
Regex_Pattern = r"^([ac][ac]|[bd][bd])*(([ac][bd]|[bd][ac])([ac][ac]|[bd][bd])*([ac][bd]|[bd][ac])([ac][ac]|[bd][bd])*)*$"
