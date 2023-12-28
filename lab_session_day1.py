"""write a program to demostarte the following operator in python with example total 8 operators 
1.arithematic ,assingment,logical,bit wise,terminate,relational,membership,identity."""
a = int(input("Enter a : "))
b = int(input("Enter b : "))
operator = input('Enter ==,!=,>,<,>=,<=,+, -, *, /,and,or,not : ')

if operator == '+':
    print(a + b)
elif operator == '-':
    print(a - b)
elif operator == '*':
    print(a * b)
elif operator == '/':
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero.")
if operator == '==':
    print (a == b)
elif operator == '!=':
    print (a != b)
elif operator == '>' :
    print (a > b)
elif operator == '<':
    print (a < b)
elif operator == '>=':
    print (a >= b)
elif operator == '<=':
    print (a <= b)

if operator == 'and':
    print(a < 5 and b < 10)
elif operator == 'or' :
    print (a < 5 or b < 4)
elif operator == 'not' :
    print (not(a < 5 and b < 10))