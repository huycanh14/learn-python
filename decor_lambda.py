"""
decorator là những functions thay đổi tính năng của một function, method hay class một cách dynamic, mà không phải sử dụng subclass.
"""


def apply_one(func, arg):
    return func(arg)


def apply_twice(func, arg):
    return func(func(arg))


def add_five(x):
    return x + 5


# print(apply_one(add_five, 10))
# print(apply_twice(add_five, 10))

"""
hàm vô danh là hàm được định nghĩa mà không có tên. Nếu các hàm bình thường được định nghĩa bằng cách sử dụng từ khóa def, thì hàm vô danh được định nghĩa bằng cách sử dụng từ khóa lambda. Vì lý do đó mà hàm vô danh còn được gọi là hàm Lambda. 
"""

def test(f, arg):
    return f(arg)


print(test(lambda x: 2 * x, 5))

