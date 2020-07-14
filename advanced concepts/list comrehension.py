num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# my_list = [n for n in num]
# print(my_list)

# my_list = []
# for n in num:
#     my_list.append(n*n)
# print(my_list)

# my_list = [n*n for n in num]
# print(my_list)

# my_list = map(lambda n: n*n, num)
# print(my_list)

# my_list = []
# for n in num:
#     if n % 2 == 0:
#         my_list.append(n)
# print(my_list)

# my_list = [n for n in num if n%2 == 0]
# print(my_list)

# my_list = filter(lambda n: n%2 == 0, num)
# print(my_list)
#
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)

# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)

name = ['bruce', 'clark', 'peter']
heros = ['batman', 'superman', 'spiderman']
# my_dict = {}
# for name, heros in zip(name, heros):
#     my_dict[name] = heros
# print(my_dict)

my_dict = {name: hero for name, hero in zip(name, heros)}
print(my_dict)

