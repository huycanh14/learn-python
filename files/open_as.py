"""file = open('ali.txt', 'w')
file.write('Hello world\n')
file.close()"""

"""with open('ali.txt') as file:
    file = file.read()"""

with open('ali.txt', 'w') as file:
    file.write('hi \n hello world \n bye')
file.close()

with open('ali.txt') as f:
    f = f.read()

print(f)
