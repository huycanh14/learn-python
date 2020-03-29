n = int(input('Please enter a number: '))
n2 = int(input('Please enter an other number: '))

try:
    print(n / n2)
    
except ZeroDivisionError:
    print('The answer is zero')
