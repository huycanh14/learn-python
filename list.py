l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
a = len(l)
# print(a)
b = l[0:5]
# c = l[0::]
c = l[0::2]
# d = l[-1: -4]
d = l[10::-1]
# print(d)
n = 'Dang Huy Canh'
name = n.split()
# print(name)

string = list('34')
# print(string)

# for x in [1, 2, 3]:
    # print(x, end = ' ')

# rec = [i for i in range(0, 10)]
# rec = [i * 4 for i in 'spam']
rec = []
for c in 'spam':
    rec.append(c * 4)
print(rec)

a = list(map(abs, [1, 2, -4, 70, -23]))
print(a)
