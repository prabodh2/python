# '*' = *args = positional 
# '**' = **kwags = keyword based 
# def fun_name(name,age):
#     z = name+age 
#     print(z)
# fun_name(name='ABC',age =32 )
# fun_name("ABC",32)
# fun_name("ABC",age=32)
# def main():
#     a = int(input("Enter a value of a : "))
#     b = int(input("Enter a value of b : "))
#     #print("in function main ............dir()= %s", %(dir()))
#     print("in function main .............dir() =",dir())
#     result = absdiff(a,b)
#     #print(" the absolute value of %d - %d = %d" %(a,b,result))
#     print("the absolute value of",a,"-",b,"=",result)
    
# def absdiff(x,y):
#     #print("in function absdiff.....dir() = %s"%(dir()))
#     print("in function absdiff.......dir() = ",dir())
#     if x > y:
#         z = x-y
#     else:
#         z = y-x
#     return z
# main() 
# incremental development /   scaffloding 
# def dist(x1,x2,y1,y2):
#     d_x = x2-x1
#     d_y = y2-y1
#     sqx =d_x**2
#     sqy =d_y**2
#     plus = sqx+sqy
#     sqrt = plus ** 0.5
#     print(sqrt)
# dist(1,4,2,6)
# wt is composition in python 

# def distance(x1,x2,y1,y2):
#     return (((x2-x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)
# cx = int(input("Enter a cx : "))
# cy = int(input("Enter a cy : "))
# px = int(input("Enter a px : "))
# py = int(input("Enter a py : "))
# def circledata(cx,cy,px,py):
#     return (3.14 * (distance(cx,px,cy, py) ** 2))
# print(circledata(cx,cy,px,py))
# factorial
a = int(input("Enter a integer : "))
def fact (n):
    if (n==0):
        return 1
    else :
        recurse = n*fact(n-1)
    return recurse 
print(fact(a))
# wt is type checking 