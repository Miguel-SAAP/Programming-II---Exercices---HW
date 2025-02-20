#Exercice 1:

print(type(2 + 3))  # int
print(type(6 / 2))  # float
print(type(2 != 3))  # bool
print(type(5 or 6))  # int
print(type(print))  # builtin_function_or_method
print(type(2 * 2))  # int
print(type("abc".find))  # builtin_function_or_method
print(type("bubu" * 2))  # str
print(type("bubu" * (4 / 2)))  # TypeError (4/2 is float, cannot multiply string by float)
print(type(["abc", 2]))  # list
print(type("abc"[2]))  # str
print(type("abcabcabc".split("a")))  # list

#Exercice 2:

print(2 + 3)  # 5
print(6 / 2)  # 3.0
print(2 != 3)  # True
print(5 or 6)  # 5
print([1, 2, 3].append("John"))  # None
print("bubu" * 2)  # "bubububu"
print("bubu" * (4 / 2))  # Erreur (TypeError: can't multiply sequence by non-int of type 'float')
print(len(["abc", 2]))  # 2
print(2 + 3 * 2 ** 2)  # 14

#Exercice 3:

a = 2
b = 3
c = "abc"
print(a, b, c)
print(a, b, c, sep=",")
a += 2
a == 5
print(a)
print(c*(a-b))
d = c.find("b")
print(d)
print(d and b)
print(d == True)
e = str(a) + str(b) + str(c) + str(d)
print(e)
print(e[1::2])
print(e+e[::-1])

## Write a function that takes the name of a text file as parameter. Print out the 3-letter words that start with “


#Tuples (Collection of elements   ,
#Exercice 1:
a = (1, 2, 3)
print(a)

b = ("me", "myself", "Them")
print(b)
type(b)

c = tuple("macarena")
print(c)
c[2] #result = C because it starts at 0,1,2,3

c[2] = "w"
print(c)

tpl = (1,2,3,4,5,6,7,8,9,10)
tpl[::3] # 1 every 3 numbers (1,4,7,10)

tpl = (100,) + tpl[1:] # Valid, construct a new tuple!
tpl #(100, 2, 3, 4, 5, 6, 7, 8, 9, 10)


#the sign + :
a = (1, "one", None)
b = (3, 'seven')
a + b #(1, 'one', None, 3, 'seven')

# Function len() to see the lenght of the strim
a = ("Hello World")
print(len(a)) # 11

#How to create a dictionary
Dico = {"one": "Uno", "Two": "Dos", "Quatro": "Four"}
print(Dico)

Dico["one"]

print(len(Dico))

#How to add or delete an element from the dictionary:
d = {'John': 7, 'Mary': 9, 'James': 4, 'Jane': 6, 'Jorge': 8}
d["Ana"] = 9
d #{'John': 7, 'Mary': 9, 'James': 4, 'Jane': 6, 'Jorge': 8, 'Ana': 9} Ana has been added to the dico

del(d["Mary"])
d #{'John': 7, 'James': 4, 'Jane': 6, 'Jorge': 8, 'Ana': 9} Mary has been deleted

#To check in the element is on the list
"mari" in d
"John" in d