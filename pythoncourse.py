


''' -: Section 3 :- Python Basics :-  '''

#Python Basics:-
'''#Developer Fundamentals:- 

-Don't read the dictionary. (Coz it is not gonna make you memories all the things.)

-Don't learn all about any language. Focus on the limited but useful concepts.
'''


'''How to write comment in python:-

1) Single line comment:-  use # to write single line comment.
Example:-  #This line is commented.

2) Multiline comment:- Use triple quotes to write multiline 
comment.

Shortcut to comment a line :-
First select a single line or multiple lines and then press
"Ctrl + /" to comment a line/s.
'''


#Fundamental Data Types
'''There are Eight fundamental data types in python and they are stated as below:-
1) int(integer) 
2) float(floating point number) 
3) bool(boolean data type) 
4) str(string data type)
5) list
6) tuple
7) set  
8) dict(dictionary data type)
9) None
10)complex
'''

'''Functions in python:-
print(), type(), 
'''
int and float
#print function
print(2+4)
print(2-4)
print(2*4)
print(2/4)

#find the type of the data using type() function:-
print(type(2+4))
print(type(2-4))
print(type(2*4))
print(type(2/4))

#different math operator:-
print(2 ** 4)      # 2 to the power 4. (Here ** means to the power or raised to.)
print(2 // 4)      # Here // gives the quotient.  (2/4=0)
print(5 // 4)      # Here // also gives quotient. (5/4=1)
print(5 % 4) 	     # Here % gives the remainder value. (5 % 4 = 1)

#math function:-
#1-round() function:-
print(round(3.1))   #round() function rounds the number. here the result is 3
print(round(3.4))	# here rounding number is 3.4 which is = 3
print(round(3.5))	# here we get 4
print(round(3.6))	# here we get 4
print(round(3.8))	# here we get 4
print(round(3.9))	# here we get 4
print(round(4.5))	# here we get 4
print(round(2.5))	# here we get 2
#2-abs() function:-
print(abs(-20))		# abs() function gives the absolute value of any number.

#Operator precedence (operators order):-
# Order :-   () , ** , * and / , + and -
print(20 + 4 * 3)
print(20 - 3 * 4)
print((5 + 4) * 10 / 2)
print(((5 + 4) * 10) / 2)
print((5 + 4) * (10 / 2))
print(5 + (4 * 10) / 2)
print(5 + 4 * 10 // 2)

#Optional : Additional data types - bin() and complex:-
#Decimal to binary :-
print(bin(0))
print(bin(1))
print(bin(2))
print(bin(4))
print(bin(10))
print(bin(254))
print(bin(255))
#reverse: binary to decimal(base 10):-
print(int('0b101', 2))		#0b101 is a base 2 number and convert it into int().

#Variables:-
#Variables are used to store the values to use them later.
iq = 190
print('iq:',iq)
# snake_case
# Start with lowercase or underscore
# Letters, numbers, underscore
# Case sensitive
# Don't overwrite keywords that are already present in python.
user_iq = 190
user_IQ = 180
_user_iq1 = 185
#print = 170
#print(print) #Don't overwrite the keywords in python, we wil get below error.
# Traceback (most recent call last):
#   File "C:\Users\Swapnil\Desktop\Complete Python Developer in 2023 - Zero to Mastery\code\main.py", line 88, in <module>
#     print(print) #Don't overwrite the keywords in python, we get error.
#     ^^^^^^^^^^^
# TypeError: 'int' object is not callable

#Constants:- constants in python-
PI = 3.14159265
print(PI)
#don't creat variables with double underscores like "__hihi ".
a,b,c = 1,2,3
print(a,b,c)

#Expressions VS Statements:-
iq = 100
user_age = iq / 5 	# so here "iq / 5" is an expression.
				    # And "user_age = iq / 5" is a statement.

#Augmented Assignment Operator:-
some_value = 5
some_value = some_value + 2
#Above is similar to below
some_value += 2
some_value -= 2
some_value *= 2 
print(some_value)

#Strings (str):- 
'Hi hello there'
"Hi hello there"
print(type('hi hello there'))
username='supercoder'
password="suersecret"
long_string='''    
wow
o o
---
'''					#''' is used for multiline print.
print(long_string)

first_name='swapnil'
last_name='Dhokchaule'
full_name=first_name + ' ' + last_name
print(full_name)


#string concatenation:-
print('hello' + ' Swapnil')

#Type conversion:- convert the type of the data type.
print(type(str(100)))

#Escape sequences/characters:-
#we can't print like " 'It's sunny' " coz of single quote.
''' \\= for backslash
	\t= for insert tab.
	\n= for insert new line.
	see official python document for more about this topic.
'''
weather="It\'s sunny"
print(weather)
print("\\ this is a backslash")
print("\t This is a tab line")
print("\n This is a new line\n")

#formated string:-
name = 'Johnny'
age = 55
print('Hi ' + name + '. You are ' + str(age) + ' year old')
print('\n')
print(f'Hi {name}. You are {age} years old') #This is a formatted string.
print('\n')
print('Hi {}. You are {} years old'.format('Johnny', '55')) #Here we used .format() .
print("\n")
print('Hi {}. You are {} years old'.format(name, age))
print("\n")
print('Hi {1}. You are {0} years old'.format(name, age))
print("\n")
print('Hi {0}. You are {1} years old'.format(name, age))
print("\n")
print('Hi {new_name}. You are {new_age} years old'.format(new_name='swapnil', new_age=22))

#string indexes:-
string1='me me me'
		#01234567  This is indexing
		# m e   m e   m e	
		#-8-7-6-5-4-3-2-1  This is a negative indexing.
# [start:stop]
print(string1)
print(string1[0])
print(string1[0:4])
print(string1[-1])
string2='01234567'
		#01234567  This is a indexing.
# [start:stop:stepover]
print(string2[0:8:2])
print(string2[1:])
print(string2[:5])
print(string2[::1])
print(string2[-1])
print(string2[::-1])  # This revers the string order.

#Immutability:-
# Strings are immutable means we can not reassign.

#Built-in functions + methods:-
print(len('hellllloooooo'))
quote='to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be', 'see'))
quote2=quote.replace('be', 'see')
print(quote)
print(quote2)

#Booleans:- (bool) can be True or Flase -
name = 'swapnil'
#profile look:-
is_cool=False
is_cool=True
print(bool(1))
print(bool(0))

#Exercise: Type conversion:-
name='Swapnil Dhokchaule'
age=22
relationship_status='single'
relationship_status='it\'s complicated'
print(relationship_status)
'''
#Exercise:-(Solved/Correct)
Find the age of a person by his birth year:-
birth_year=input('What year were you born?')
age=2023-int(birth_year)
print("Your age is :- ", age)
print(f"Your age is :- {age}")
'''

#Developer Fundamentals:-     
'''1) Don't use comment unnecessarily until it's important.
   2)Your code should be more self explanatory and concise.
   3)Use commenting only when it's necessary or importtant or something is hard to understand.'''

#Exercise: Password Checker:-
'''username=input("Enter your name :- ")
password=input("Enter your passwrod :- ")
password_length=len(password)
hidden_password='*' * password_length
print(f'hey, {username}, your password, {hidden_password}, is {password_length} letters long')
'''

#Lists:-
'''Collection of items.
1) It is a ordered sequence of objects.
2) Lists are mutable.
'''
li1=[1,2,3,4,5]
li2=['a','b','c']
li3=[1,2,'a',True]
amazon_cart = ['notebooks','sunglasses']
print(amazon_cart[0])

#List slicing:-
amazon_cart = [
	'notebooks',
	'sunglasses',
	'toys',
	'grapes']
print(amazon_cart)
amazon_cart[0] = 'Laptop'
print(amazon_cart)
new_cart=amazon_cart[0:3]
new_cart[0] = 'gum'
new_cart1=amazon_cart
new_cart1[0] = 'gel'
print(new_cart1)
print(amazon_cart[0::2])
#copy a list
new_cart2=amazon_cart[:]

#Matrix:- (2D list or multidimensional list)-
matrix = [
	[1,2,3],
	[2,4,6],
	[7,8,9]
]
print(matrix)
print(type(matrix))
print(matrix[0][1])

#List Methods:-
basket=[1,2,3,4,5]
print(len(basket))
#1-adding items to list:-
new_list = basket.append(100)
print(basket)
print(new_list) #Gives none coz don't produce result by .append()
basket.append(100) #add item to last.
new_list=basket
print(basket)
print(new_list)
basket.insert(4, 25)
print(basket)
basket.extend([125])
print(basket)
print("\n")
#removing items from list:-
basket.pop()
print(basket)
basket.pop(0)
print(basket)
basket.remove(4)
print(basket)
basket.clear()
print(basket)

#List methods 2:-
basket=['a','b','c','d','e','f','a','b','c','d','a','b']
print(basket.index('b'))    # gives the index of the item.
print(basket.index('d', 0, 4)) # index('item', starting-index, ending-index)
print('d' in basket)
print('y' in basket)

print('i' in 'hi my name is Ian.') #find char in string.

print(basket.count('a')) #counts the occurence of the char/letter/item in the list.
print(basket.count('c'))


#List methods 3:-
basket=['a','b','c','d','e','f','a','b','c']
basket.sort()   #Sorts the items in the list. returns none.
print(basket)

basket1=[9,5,6,8,4,6,3,4,654,687,987,4,65,4,13,54]
# basket1.sort()
# print(basket1)
# print(sorted(basket))
# new_basket=basket1.copy()  # here we can also use basket[:] to copy list.
# new_basket.sort()
# print(new_basket)
# print(basket1)
basket1.sort()
basket1.reverse()   #reverse the list.
print(basket1)
print("\n")


#Common list patterns:-
print(list(range(1, 101)))
sentence=' ! '
new_sentence=sentence.join(['hi','my','name','is','jojo.']) # .join() add the list items by anything.
print(new_sentence)
print("\n")


#List unpacking:-
a,b,c=[1,2,3]
print(a,b,c)
a,b,c, *other, d=[1,2,3,4,5,6,7,8,9]  
print(a)
print(b)
print(c)
print(other)
print(d)


#None-(Null in other programming languages):-
weapons=None   # None means just nothing.
print(weapons)
print("\n")

#Dictionary (it is data structure.):-
'''dict
1) it is a unordered key value paire.

'''
'''dictionary={'key':value}'''
dictionary={'a':[1,2,3], 'b':2,'c':True}
print(dictionary)
print(dictionary['a'])
print(dictionary['a'][1])

my_list=[
	{
	'a':[1,2,3],
	'b':'hello',
	'c':True
	},
	{
	'a':[4,5,6],
	'b':'hi',
     'c':False
	}
]

print(my_list[0]['a'][2])


#Developer fundamentals 3:-
'''  Understanding Data structure:-
[When to use what data structure]:-
>> It takes lot of practice and experiance to understand when to use what data structure. So practice more and more.
>> List is used when we have ordered sequence of the items.
>> Dictionary is used when the items are unordered or don't really mean by ordering them.'''


#Dictionary keys:-
dictionary1={
	123:[1,2,3],
	True:'hello',
}
print(dictionary1[123])  # key should be immutable/it can not be change. key should be discriptive string. key also in the dictionary has to be unique.

#Dictionary methods:-
user={
	'basket':[1,2,3],
	'greet': 'hello'
}
print(user.get('age'))
user={
	'basket':[1,2,3],
	'greet': 'hello',
	'age': 20
}
print(user.get('age', 55)) #get the age from dictionary and if age is not in the dictionary then return default value(55).

#Create a new dictionary:-
user2=dict(name='John wick')
print(user2)


#Dictionary methods 2:-
print('basket' in user)
print('size' in user)
print('age' in user.keys())
print('hello' in user.values())
print(user.items())

# user.clear()
# print(user)

# user3=user.copy()
# print(user.clear())
# print(user3)

print(user.pop('age'))
print(user)

print(user.popitem())  #it removes the last key:value paire.
print(user)

print(user.update({'age': 55}))
print(user)


#Tuple:-
''' Tuple is like list but we can not change it.
It is immutable.
They are less flexible.

'''

my_tuple=(1,2,3,4,5)
print(type(my_tuple))
print(my_tuple)
print(5 in my_tuple)

#Tuples 2:-
new_tuple=my_tuple[1:2]
print(new_tuple)

x,y,z, *other = (1,2,3,4,5)
print(x)
print(y)
print(z)
print(other)

new_tuple=(1,2,3,4,5,5)
print(new_tuple.count(5))
print(new_tuple.index(4))
print(len(new_tuple))


#Set:-
''' Unordered collection of unique values.
'''

my_set={1,2,3,4,5}
print(my_set)

my_set={1,2,3,4,5,5,5,5}
print(my_set)    # other 5 are not printed.

my_set.add(100)
my_set.add(2)  # 2 would not add to set coz it is already presents in set. The values of the set should be unique.
print(my_set)

my_list=[1,1,2,2,3,4,5,5,6,7,8,9,9]

print(set(my_list))

''' use case :- to avoid duplicate username or email address.
'''

my_set={1,2,3,4,5,5}
print(my_set)
print(len(my_set))
print(list(my_set))
new_set=my_set.copy()
my_set.clear()
print(my_set)
print(new_set)
print("\n")


#sets 2:-
'''  
	Set methods:-

.difference()
.discard()
.difference_update()
.intersection()
.isdisjoint()
.issubset()
.issuperset()
.union()
'''
my_set={1,2,3,4,5}
your_set={4,5,6,7,8,9,10}

# print(my_set.difference(your_set))
# my_set.discard(5)
# print(my_set)

# my_set.difference_update(your_set)
# print(my_set)

# print(my_set.intersection(your_set))

# print(my_set.isdisjoint(your_set)) # returns True only when no item is common.
'''
print(my_set.union(your_set)) 
This is also eqaul to :-
print(my_set | your_set)
'''
# print(my_set.issubset(your_set))
# print(my_set.issuperset(your_set))
print('Percentage course completed until now :- ',(60/342*100))
print("\n")


''' -: Section 4 :- Python Basics II :- '''


# Breaking the flow:-


# Conditional logic:-
'''
if condition:
	(block of code)
elif condition:
	(block of code)		# if-else and if-elif-else condition.
elif condition:
	(block of code)     # Their could be more elif: statements.
else:
	(block of code)
'''

is_old=False
is_licenced=True

if is_old:   # is_old  is an expression. Which returns value.
	print("You are old enough to drive.")
elif is_licenced:
	print("You can drive now.")
else:
	print("You can't drive.")
print("Code executed successfully.")

is_old=True
is_licenced=True
if is_old and is_licenced:
	print("You are old enough to drive. And you can drive now.")
else:
	print("You can't drive.")
print("Code executed successfully.")


# Truthy vs Falsey:-
'''
Truthy value:-
It returns True to any value there in bool conversion. It is called Truthy value.
'''
print(bool('Hello'))
print(bool(5))

'''
Falsey value:-
It returns False to an empty string and 0 if putted in bool. It is called Falsey value.
'''
print(bool(''))
print(bool(0))


# Ternary operator:- (conditional expression):-
'''It's a shortcut to make a code little bit cleaner.

<  Ternary operator or a conditional expression is an operation that evaluates to something based on the condition being true or not. >

'''
# condition_if_true if condition else condition_if_else

is_friend=True
can_message="Message allowed" if is_friend else "not allowed to message."

print(can_message)


# Short Circuiting:-
''' 
interpreter is smart enough to evalute the statement.
Below is the example.
'''
is_friend=True
is_user=False

if is_friend or is_user:
	print("Best friends forever!")


# Logical operators:-
'''
Below are the logical operators:-
<, >, <=, >=, ==, !=, and, or, not.

'''

print('a' > 'b')  # Why? google it.

''' because it checks for the ascii values of chars.'''
print('a' > 'b') # is false because print(97 > 98)
print(ord('a'))
print(ord('b'))
print(chr(97))
print(chr(98))


print('a' > 'A')	# why? google it.

''' because it checks for the ascii values of chars.'''
print('a' > 'A') # is true because print(97 > 65)
print(ord('a'))
print(ord('A'))
print(chr(97))
print(chr(65))

'''
goto below website for more.

https://djangocentral.com/display-char-from-a-z/
'''

import string

for i in string.ascii_lowercase:
	 print(i, end=' ')
print("\n")
for i in string.ascii_lowercase:
	 print(ord(i), end=' ')

print("\n")

for i in string.ascii_uppercase:
	 print(i, end=' ')
print("\n")
for i in string.ascii_uppercase:
	 print(ord(i), end=' ')

print("\n")

for i in range(97,123):
    print(chr(i), end=" ")

print("\n")

for i in range(65, 91):
	 print(chr(i), end=" ")

print("\n")

'''
Below are the logical operators:-
<, >, <=, >=, ==, !=, and, or, not.

'''
print(1 < 2)
print(1 < 2 < 3 < 4)
print(1 < 2 > 3 < 4)
print(1 <= 0)
print(1 >= 0)
print(0 != 0)
print(1 != 0)
print(not(False))
print(not(1 == 1))
print("\n")

# Exercise: Logical Operators:-

is_magician = True
is_expert = True

# Check if magician AND expert: 'Ypu are a master'
if is_magician and is_expert:
	print("You are a Master Magician.")

# Check if magician but not exprt: 'you are getting there.'
elif is_magician and not is_expert:
	print("You're getting there.")

# Check if expert but not magician: 'you need magic powers.'
elif is_expert and not is_magician:
	print("You need magic powers.")

# check if No magic and not expert.
else:
	print("You need to start right now.")

print("\n")


# is vs == :-
''' == checks if the values are equal or not '''
print(True == 1)	# True
print('' == 1)		# False
print([] == 1)		# False
print(10 == 10.0) # True
print([] == [])	# True

print("\n")

''' is checks if the memory location of the two values are same or not. '''
print(True is True)
print('1' is '1')
print([] is [])
print(10 is 10)
print([1,2,3] is [1,2,3]) # coz created at different location in memory.

print("\n")

a=1
b=a
print(b)
print(a is b)

print("\n")


# For Loops:-

for item in 'Zero to mastery':  # here item is a variable.
	print(item)
print("\n")
for item in [1,2,3,4,5]:
	print(item)
print("\n")
for item in {1,2,3,4,5}:
	print(item)
print("\n")
for item in (1,2,3,4,5):
	print(item)
	print(item)
	print(item)
print(item)
print("\n")

for item in (1,2,3,4,5):
	for x in ['a','b','c']:
		print(item, x)
print("\n")
for x in ['a','b','c']:
	for y in (1,2,3):
		print(x, y)
print("\n")


# Iterables:-
''' 
It is an object or a collection that can be iterated over. 

Iterables can be a -> list, dictionary, tuple, set, string, or any collection of items.

Iterate -> one by one check each item in the collection.

'''

user = {
	'name': 'Golem',
	'age': 5000,
	'can_swim': False
}

for item in user:  # it only prints keys of the dictionary.
	print(item)

print("\n")

for item in user.items(): # prints key-value pair as tuple.
	print(item)

print("\n")

for item in user.keys(): # it prints keys.
	print(item)

print("\n")

for item in user.values(): # it prints values.
	print(item)

print("\n")

for item in user.items(): # it prints key-value pair.
	key, value = item;
	print(key,'=', value)

print("\n")

for key, value in user.items(): # prints key-value pair.
	print(key,'-', value)

print("\n")


# for item in 50:
# 	print(item)

# Error occure:-

# <-- Traceback (most recent call last):
#   File "C:\Users\Swapnil\Desktop\Complete Python Developer in 2023 - Zero to Mastery\code\main.py", line 850, in <module>
#     for item in 50:
# TypeError: 'int' object is not iterable -->

# --> integer is not iterable because it is not a collection of the data or items.



# Exercise: Tricky Counter:-
''' 
Build a counter which will count the items in the iterable.
Below is the code.
'''

my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for item in my_list:
	counter = counter + item
print(counter)

print("\n")


# range():-
''' returns an object that produces a sequence of integers from start(inclusive) to stop(exclusive) by step. range(i, j) produces i, i+1, i+2, ..., j-1. 
	start defaults to 0, and stop is omitted.
	for example:- range(4) --> 0,1,2,3
'''
''' range(stop),
	 range(start, stop(exclusive)),
	 range(start, stop, stepover)
'''

print(range(100))    # range(stop) default start=0
print(range(0, 100)) # range(start, stop(exclusive))

for number in range(10):
	print(number)
	print("Hi")
print("\n")
# range(start, stop, stepover)
for number in range(0, 10, 2):
	print(number)
print("\n")
for number in range(10, 0, -1):
	print(number)
print("\n")
for i in range(2):
	print(list(range(10)))
print("\n")


# Enumerate():-
'''returns the value and its index of a iterable.
'''

for i, char in enumerate('Hellooo'):
	print(i, char)
print("\n")
for i, char in enumerate([1,2,3]):
	print(i, char)
print("\n")
for i, char in enumerate((1,2,3)):
	print(i, char)
print("\n")


for i,char in enumerate(list(range(100))):
	print(i,char)
	if char == 50:
		print(f'index of 50 is: {i}')
print("\n")


# while loop:-
''' while condition:
		[code block]
'''
i=0
while i<50:
	print(i)
	break			# breaks the infinite loop/runs only once.
print("\n")

while i<50:
	print(i)
	i+=1
else:
	print("Done with all the work.")
print("\n")


''' Here else is only executed if there is no break.'''
while i<50:
	print(i)
	i+=1
	break
else:			
	print("Done with all the work.")

print("\n")


''' For loop and while loop :- '''
my_list=[1,2,3]
for item in my_list:
	print(item)
print("\n")

i=0
while i < len(my_list):
	print(my_list[i])
	i+=1
print("\n")


'''
while True:
	response = input('Say something: ')
	if (response=='bye'):
		break
print("\n")
'''


# break, continue, pass:-
'''
--> break = to break out of the loop.
--> continue = continue the enclosing loop from start.
---> pass = passess to next line or does nothing or used when you don't know what do your code want to do.
		usecase of pass:
		example:- 
		for item in my_list:
			pass                
'''

# break-
for i in range(5):
	print(i)
	break
print("\n")

# continue-
for i in range(5):
	print(i)
	continue
	print(i)
print("\n")

# pass-
for i in range(100):  # don't know what to do with code.
	pass
print("\n")


# Our first GUI:-

''' Christmas tree '''
''' print ' ' if there is 0 and * if there is 1.'''
picture = [
	[0,0,0,1,0,0,0],
	[0,0,1,1,1,0,0],
	[0,1,1,1,1,1,0],
	[1,1,1,1,1,1,1],
	[0,0,0,1,0,0,0],
	[0,0,0,1,0,0,0]
]

print(picture); print("")
print(type(picture)); print("")
print(len(picture)); print("")

''' -:    A christmas tree:-   '''
print("-:A christmas tree:-"); print("")

for row in picture:
	for pixel in row:
		if (pixel == 1):
			print("*", end="")
		else:
			print(' ', end="")
	print("")		
 
print("")


# Developers fundamentals:-
'''What is clean/good code ?:- '''
''' follow the best practices or following a style that python comunity endorses. Use coments wisely. Use better variable names. keep code as compact as possible if possible. And do not repeat yourself (don't repeat piece of code in same code.)

'''
fill='*'        #just change the variable here.
empty=' '    
for row in picture:
	for pixel in row:
		if (pixel):
			print(fill, end='')
		else:
			print(empty, end='')
	print("")
print("")


# Exercise: Find Duplicates:-
'''find duplicate values in the list.'''

some_list=['a','b','c','b','d','m','n','n']

duplicates=[]
for value in some_list:
	if some_list.count(value) > 1:
		if value not in duplicates:
			duplicates.append(value)
print(duplicates)

print("")

# Functions:- 
''' Create our own function.'''

def say_hello():
	print("hello")
say_hello()
say_hello()

print("")


# Parameter and Arguments:-

				  #Parameters
def say_hello(name, emoji):
	print(f"Hello {name}{emoji}")

			 #Arguments
say_hello('Swapnil', ' 😊')

'''Click   "windows logo + . " for opening emoji keyboard.'''
print("😂 🤣 ❤️ 😍 😒 🙌 👍 😁 💕 😘 👌")

print("")


#Default Parameters and Keyword Arguments:-



















































