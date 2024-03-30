list1 = []
list2 = [1,2,3,]
list3 = ['a','b','c']
list4 = ['hello','world']
list5 = [1,2, 'a','b', 'python']
list6 = [1,2,['a','b','c'],3]
list7 = ['정성현','이율']
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print(list7)

a = "python"
b = " is fun"
print(a+b)
print(a*2)

a = [1,2,3]
b = [4,5,6]
print (a+b)
print(a*3)
print("     *  ")
print("   * * * ")
print("* * * * * *")
print("    * *  ")
print("     *  ")
a = 'hi'
b = 4
print(a+b)
a = "carpe Diem!"
print(a[6:11])

a = [1,2,[3,4,5,[6,7,[8,9]]]]
print(a[2][3][2][1])
a = [1,2,'a','b',3,4,'c']

print(a[4:-1])
a=[10,20,30,40,50]

a[0]='a'
print(a)
a[1:3] = 'b'
print(a)

a = 'I Love You'
print(a.count('o'))
print(a.find('Y'), a.index('Y'))
print('.'.join(a))
print(a.split())
print(a.replace('Love','Like'))
print(a.upper() , a.lower())

a = ' abcd '
b = 'efgh'
print('%s%s' %(a,b))
a = a.strip()
print('%s%s' %(a,b))

a = [1,5,10,3]
a.append(20)
print(a)
a.sort()
print(a)
a = ['b','a','n','a','n','a']
a.reverse()
print(a)
a.remove('a')
print(a)
p = a.pop()
print(p,a)
n = a.count('n')
print(n)

num = input('주민번호 : ')
a = (num[:6])
b = (num[7])
print(f'생년월일 : {a}')
print(f'성별 : {b}')

num = input('주민번호 : ')
a = (num[2:6])
print('생년월일 : %s월 %s일' %(a[:2],a[2:]))

import turtle
t = turtle.Turtle()
x = []
y = []
x.append(input("x1: "))
y.append(input("y1: "))
x.append(input("x2: "))
y.append(input("y2: "))
x.append(input("x3: "))
y.append(input("y3: "))
for i in range(3):
    t.goto(x[i])
    t.goto(y[i])
