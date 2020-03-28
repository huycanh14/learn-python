""" Hàm map này có tác dụng duyệt qua tất cả các phần tử của một hoặc nhiều list, dictionary hoặc tương tự như thế """

def add_five(x):
    return x + 5

def add_two(x):
    if x % 2 == 0:
        return x

nums = [i for i in range(2, 100)]
result = list(map(add_five, nums))
result_2 = list(map(lambda x: x + 5, nums))

# print(result_2)
"""Hàm này cũng có tác dụng duyệt qua các phần tử trong list, dict,... nhưng khác với map là hàm này sẽ chỉ trả về những giá trị mà điều kiện trong function chấp nhận (có nghĩa là True)."""

result_3 = list(filter(lambda x: x % 2 == 0, nums))
result_4 = list(filter(add_two, nums))
print(result_4
