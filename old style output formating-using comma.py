#old style uotput fomating by using comma
'''name ="chandu"
age = 22
print("Name is ",name,"and age is ",age)'''


#1.modulo operator output formating
## Access specefiers
# %d - integers
# %f - float
# %s - string

# type error
'''name ="chandu"
age = 22
print("Name is %s and age is %d "%(age,name))'''

#dot format
'''name ="chandu"
age = 22
print("Name is {} and age is {}".format(name,age))
print("Name is {} and age is {}".format(age,name))
print("Name is {1} and age is {0}".format(name,age+5))'''


# f- format
# dot format

'''name ="chandu"
age = 22
percentage = 95.2568
print(f"Name is {name} and age is {age} and i have {percentage}")
print(f"Name is {name} and age is {age} and i have {percentage:.2f}")
print(f"Name is {name} and age is {age} and i have {percentage:}")
num ='01'
print(f"{num:2{5}}")'''

# eval () function
'''res = eval ('52+3')
print (res)
print ('52+3')
print (eval('53+3'))'''


#
'''num = eval(input())
print(type(num),num)


#

num = eval(input())
print(type(num),num)'''

#
l=list(map(int,input().strip().split()))
print(l)

'''#
s=input().strip()
print(s)
l=list(map(int,input().strip().split()))
print(l)'''

