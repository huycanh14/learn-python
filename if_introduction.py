print("Enter your age: ")
age = int(input())
if age < 18:
    print('You can enter')
elif age > 18 and age < 20:
    print('You Can enter')
elif age > 60:
    print('Your so old to enter')
else:
    print('You can\'t enter')