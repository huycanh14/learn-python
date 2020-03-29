# f = open('text.txt')  #mo file
# f = open('text.txt', 'r')  #mo file: chi duoc dung phuong thuc read
f = open('text.txt', 'w')  #mo file: chi duoc dung phuong thuc write
# f.read() doc file
# print(f.read())
# file_l = f.read()
# print(file_l)
f.write('Hello world')
f.close()
file_l = open('text.txt', 'r')
print(file_l.read())