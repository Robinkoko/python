def get_sum(n):
    s = 0
    for i in range (1,n+1):
        s+=i
    return s
n = int(input())
print("1부터 %d까지의 합은 %d입니다." %(n,get_sum(n)))

def get_sum(n):
    s = 0
    for i in range (n,n1+1):
        s+=i
    return s
n = int(input())
n1 =int(input())
print("%d부터 %d까지의 합은 %d입니다." %(n,n1,get_sum(n)))

def area(n):
    return (n**2) * 3.14159265358972323846265028841971693949445923
a = int(input())
print(area(a))

def number(n):
    if n%2 == 0:
        return "even"
    else :
        return "odd"
a = int(input())
print(number(a))

def get_max(n):
    a = 0
    for i in range(n):
        b = int(input())
        if b>a:
            a=b
    return a
c = int(input("Enter integer : "))
d = get_max(c)
print ("Max value : %d" % d)

def rect (w,h):
    return w*h
def tri(w,h):
    return w*h/2
def circle(r) :
    return str(r**2) + str("π")
print("choose a shape:")
print("1.Rectangle" , "2.Triangle","3.Circle", sep = '\n')
n = int(input())
if n == 1:
    w = int(input("width : "))
    h = int(input("height : "))
    area = rect(w,h)
if n == 2:
    w = int(input("width : "))
    h = int(input("height : "))
    area = tri(w,h)
if n == 3:
    r = int(input("radious : "))
    area = circle(r)
print(area)

def Login(id,password):
    global result
    if id =='Cube' and password == 1234:
        result =1
    if id =='Cube' and password != 1234:
        result =2
    if id !='Cube' and password == 1234:
        result =3
    if id !='Cube' and password != 1234:
        result =4
def say(result):
    if result ==1 :
        return "Login Success"
    if result ==2 :
        return "Please check your PW"
    if result ==3 :
        return "Please check your ID"
    if result ==4 :
        return "Please check your ID and PW"
a = str(input("ID : "))
b = int(input("PW : "))
Login(a,b)
print(say(result))
