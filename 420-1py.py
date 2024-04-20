from random import *
import turtle
a = ['common','uncommon','natural','rare','divious','christalrise','rage','glacier','legendary','precious','magentic','siderioum']
i=1
while i >0 :
    d = turtle.textinput('뽑기','a를 입력하세요')
    if d == 'a':
        print (choices(a, [5096,2048,1024,512,256,128,64,32,16,8,4,2]))
    else:
        print('error')
        
