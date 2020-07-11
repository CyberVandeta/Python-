s = "hello world"
print(s)
s1 = s.capitalize()
print(s1)
s2 = s.upper()
print(s2)
s3 = s.lower()
print(s3)
s4 = s.count("l")
print(type(s4))
print(s4)
s5 = s.find("c")
print(type(s5))
print(s5)
x = "concat"
s6 = "hello {0}".format(x)
print(s6)
s7 = s.index("r")
print(s7)
s8 = s.isascii()
print(s8)
s9 = s.swapcase()
print(s9)
s10 = s.isdecimal()
print(s10)
z = "         strip me!"
s11 = z.strip()
print(s11)
# s12 = s.format_map(x)
# print(s12)
# # '{name} was born in {country}'.format_map(name='Guido')
s13 = s.isspace()
print(s13)
s15=s.isupper()
print(s15)


# print('Py' in 'Python')

name = "bob"
age = 38
city = "new york"
print("my name is {0}, my age is {1}, i liv in {2}".format(name, age, city))

"""Print Formatting"""

v = "string"
print("this is a %s" % v)

