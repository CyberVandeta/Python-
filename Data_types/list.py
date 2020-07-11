l = []
l.append(1)
print(l)
l.append(2)
print(l)
for i in range(3, 10):
    l.append(i)
print(l)

l1 = ["string", 1, 2.3, "o"]
print(l1)
x = l1.pop(3)
print(x)
print(l1)

l2 = [1, 8, 5, 6, 9, 1, 3]
l2.sort()
print(l2)
l2.reverse()
print(l2)
l3 = l2.count(1)
print(l3)
l2.insert(8, 6)
# l2.insert(9)   # require two args
print(l2)
l2.remove(1)
print(l2)
l2.clear()
print(l2)


auto = []
for i in range(10):
    auto.insert(i, i)
print(auto)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
mat = [a, b, c]
print(mat)
d = mat[0]
print(d)
d = mat[1][2]
print(d)

f_col = [row[2] for row in mat]
print(f_col)

col = [i for i in range(1, 11)]
print(col)