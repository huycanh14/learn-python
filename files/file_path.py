file_path = './text.txt'
filename = './text.txt'

# with open(file_path, 'w') as file:
#     file.write('Hello world \n this is python is the best \n how to open file in python')

# with open(file_path, 'r') as file:
# with open(filename, 'r') as file:
    # for f in file:
    #     print(f.rsplit())
    #     print(f)
    # file = file.readlines()
# print(file)
# file.close()

with open(filename) as file:
    # line = file.readlines()
    line = file.readlines()

string = ''

# print(type(line))
# print(line)
for i in line:
    print(i)
    string += i.rstrip()
print(string)
