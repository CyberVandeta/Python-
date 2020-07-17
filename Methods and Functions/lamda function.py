def square(num):
    result = num ** 2
    return result


x = square(13)
print(x)

sq = lambda n: n ** 2
x = sq(10)
print(x)


def even(n):
    return n % 2 == 0


e = even(11)
print(e)

rev = lambda s: s[::-1]
r = rev("love")
l = rev("evolve")
print(r)
print(l)

len_chk = lambda item: len(item)
chk = len_chk("this is length check using anonymous function")
print(chk)

# three main functions
# map()
# filter()
# reduce()
