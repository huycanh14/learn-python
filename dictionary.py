"""
kiểu dữ liệu dictionary trong python là một kiểu dữ liệu lưu trữ các giá trị chứa key và value , nhìn một cách tổng quát thì nó giống với json. và đối với kiểu dữ liệu này thì các giá trị bên trong nó không được sắp xếp theo một trật tự nào cả.
"""
# my_dic = {'name': 'kain', 'age': 22, 'color': 'red'}
# print(my_dic['name'])
# print(my_dic['age'])
# test = {'x_position': 0, 'y_position': 25}
# print(test['x_position'])
# print('The location is ', test['x_position'], test["y_position"])
# test['speed'] = 80
# print(test)
# test = {'ali': 'C++', 'sara': 'C', 'param': 'ruby', 'para': 'perl'}
# del test['ali']
# print(test)
d = {
    'name': 'kain',
    'age': 22,
    'family_name': 'Huy'
}
# print(d.keys())
# print(d.values())
# print(d.items())
# print(d['name'])
# print(d.get('name'))
#get: nếu khi ko có key thì vẫn chạy chương trình và trả về kết quả là ko có key, ['key']: ko có ky thì dừng chương trình và hiện lỗi
d2 = d.copy()
print(d2)
d2['name'] = 'john'
print(d2)

d3 = {}
d3.update(d)
# print(d3)

test = {
    'key_1': {'name': 'kain', 'age': '22', 'f_name': 'Huy'},
    'key_2': {'name': 'john', 'age': '26', 'f_name': 'Robert'},
    'key_3': {'name': 'Tran', 'age': '18', 'f_name': 'Tung'},
}
# for key, value in test.items():
    # print(key, value)
    # print(test[key], value)
input_1 = input('Enter key search')
my_list = [k for (k, v) in test.items() if k == input_1]
print(my_list)