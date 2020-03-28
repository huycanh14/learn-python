"""
Lệnh này cách sử dụng gần giống với lệnh return, tuy nhiên nó khác return ở chỗ trả về một object thì yield sẽ trả về một generator.
+Khi tạo 1 list và truy xuất lần lượt từng giá trị của list đó =>iteration. Mọi thứ mà bạn có thể dùng cú pháp “for … in …” đều là một iterable. Ví dụ như chuỗi, list, tuple, file,..
===> ko được tái sử dụng
+ Generator là iterator, một dạng của iterable nhưng khác ở chỗ bạn không thể tái sử dụng
"""

# def countdown(x):
#     while  x > 0:
#         yield x
#         x -= 1

# for i in countdown(10):
#     print(i)

# print(countdown(100))

def countdown(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(countdown(10)))