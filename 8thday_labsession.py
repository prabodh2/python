#wap to create a dictionary with mixed keys and print the keys and print values
#and key value pairs
# d = {1:"india",'city':'new delhi','record':{'id':101,'name':'amit','age':21} }
# print(d.keys())
# print(d.values())
# print(d)
# wap for accessing element from a dictionary.
# r1={'id':101,'name':'Amit','Age':21}
# print(f'id: {r1["id"]}')
# print(f'name: {r1.get("name")}')
#wap to compare two dictionary inpy
# r1={'id':101,'name':'Amit','Age':21}
# r2={'id':101,'name':'Amit','Age':21}
# r3={'id':101,'name':'raheel','Age':26}

# if (r1 == r2):
#     print("r1 and r2 are equal")
# elif (r1 == r3):
#     print("r1 and r3 are equal")
# elif (r2 == r3):
#     print("r2 and r3 are equal")
# else:
#     print("none")
#wap to removing element from a dictionary 
# record={'id':101,'name':'Amit Kumar','Age':21}
# del record['id']
# print(record)
# record.pop('name')
# print(record)
#wap to generate and print dictionary of no and its square like
# n = int(input("Enter a number: "))
# result = dict(sorted({(i, i*i) for i in range(1,n+1)}))
# print(result)
#wap for adding element to a empty dictionary on the following 
# d={}
# d[0] = 'Amit'
# d[1] = 'Kumar'
# d[2] = 23
# d[3] = 'Delhi'
# d['name'] = (69, 70, 58)
# d[4] = {'Nested': {'Name': 'Shivang', 'Age':24}}
# print(n)
p = "jithu"
def my_fun():
    print("Gagan loves " + p)
my_fun()