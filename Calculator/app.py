choice = input("Perform math functions.Would you like to proceed?(y/n)")

if choice == 'y':
    print('You can add (+), subtract (-), multiply (*), or divide (/).')
    operation =input('What do you have in mind:')

num1 = int(input('Enter number one:'))
num2 = int(input('Enter number two:'))
def calculate(num1, num2):
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        if num1 >= num2 :
            print(num1 - num2)
        else:
            print(num2 - num1)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        if num1 >= num2:
            print(num1 / num2)
        else:
            print(num2 / num1)
    else:
        print('The provided operation is not a maths function.')
calculate(num1, num2)