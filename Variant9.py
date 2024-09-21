def argCheck(args):
    if len(args) != 2:
        print('Error, enter a two-digit number')
        quit()
    return args

def numCheck(nums):
    for c in nums:
        if not c.isdigit():
            print('Error, enter valid values')
            quit()
    return nums

a = float(numCheck(argCheck(input('x:'))))
b = float(numCheck(argCheck(input('y:'))))
c = float(numCheck(argCheck(input('z:'))))

num1 = a + b + c

num2 = a * b * c

print("Сума чисел:", num1)
print("Добуток чисел:", num2)