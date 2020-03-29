"""with open('text.txt', 'r') as file:
    file = file.readlines()

string = ''

for f in file:
    string += f.rstrip()
print(string)

if 'python' in string:
    print('yes')
else:
    print('no')
"""

with open('ali.txt', 'w') as file:
    file.write('Hello world\n')
    file.write('this is python learning\n')
    file.write('how to write data in file with pytho')

file.close()

with open('ali.txt') as f:
    f = f.read()
print(f)

