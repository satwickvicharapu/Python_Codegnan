#Armstrong number 
'''
n = int(input())
length = 0
temp1 = temp2 = n
while 0 < temp1:
  rem = temp1 % 10
  length += 1
  temp1 //= 10
res = 0
while 0 < temp2:
    rem = temp2 % 10
    res = res + res**length
    temp2 //= 10
if res == n:
    print(f"{n} is a armstrong number ")
else:
    print(f"{n} is not a armstrong number ")'''
    


# Armstrong number blw 1 to 1000 number
n=int(input())
armstrong_list = []
for i in range (1,1001):
    length = len(str(n))
    temp2 = n
    res = 0
    while 0 < temp2:
        rem = temp2 % 10
        res = res + rem**length
        temp2 //= 10
    if res == n:
        armstrong_list.append(n)
print(armstrong_list) 
