def cal():
    a=int(input('Please enter respective number to perform the operation: \n 1.Addition 2.Subtraction 3.Multiplication 4.Division : '))
    b=int(input('Enter first number to perform the operation: '))
    c=int(input('Enter second number to perform the operation: '))

    if a==1:
        print(b+c)
    elif a==2:
        print(b-c)
    elif a==3:
        print(b*c)
    else:
        print(b/c)
    
cal()

#code on dev1 branch
def greet():
    print('The code developed on dev1 branch')
def greeting():
    print('Code developed on branch dev2')
