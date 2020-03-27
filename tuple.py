"""
tuple là một kiểu dữ liệu dùng để lưu trữ các đối tượng không thể thay đổi về sau(giống như hằng số - const)
Cách lưu trũ giống như kiểu list
"""
a = () #Khai báo tuple
# print(type(a))

users = ('ali', 'kain', 'root', 'administration')
# print(type(users))
# tuple không dùng được append, pop, del assign value

password = ('12345', '7893', '8242','82552')
l = []
l.append(users)
l.append(password)
# print(l)
print(l[0].index('ali'))