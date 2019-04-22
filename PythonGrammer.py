import random
import copy
# is, not, in, del, and, or

print("test")
print("test"); print("test") # many sentence in oneline so take a semicolon
# how to comment => #

# how to indentation
# empty2, empty4, tap but python coding style guide shows empty4

print(4/2) # float
print(int(4/2)) # integer
print(int("10"))
print(5//2) # floor division
print(5%2) # mod
print(2**10) # involution answer: 1024

print(type(10)) # typeid
quotient, remainder= divmod(5,2) # quotient, remainder together
print(quotient,remainder) # 2 1

0b1001 # binary 0b
0o10 # oct 0o
0xf # hex 0x

x,y,z= 10,20,30 # many variable assignment
x,y,z= y,z,x # swap
print(x,y,z)
# None = NULL

# arithmetic operator
# a=20
# a+=20
# a=a+20
# -=, *=, /=, %=




# scanf_s
x= int(input("first number"))
y= int(input("second number"))
result= x+y
print(result)

a,b=input("input two string").split() # split is seperated by empty space
print(a)
print(b)

aa,bb=input().split()
aa=int(aa); bb=int(bb)
print(aa+bb)


xx,yy= map(int, input("input two number").split())
print(xx+yy)

aaa,bbb= map(int,input("input two number").split(',')) # divided by comma
print(aaa+bbb)





print(123) # 123
print(1,2,3) # 1 2 3
print(1,2,3,sep=',') # 1,2,3
print('fuck','you',sep=' the ') # fuck the you

print(1,2,3,sep='\n') # \n next line

print(4,end='') # end is many lines show one line
print(5,end='')
print(6)

print(2000,10,22,sep=" / ",end=' ')
print(11,44,33,sep=" : ")


# id = confirm the memory address


print(10==10)  # == equal
print(10!=5) # != not equal
print("zz"=="zz")
print("zz"!="zz")
print("Zz"=="zz")
print(1==1) # same value so true
print(1 is 1.0) # different object so false
print(1 is not 1) # flase

# (is, is not) compare object
# logical operator
# and, or, not
print(True and True) # True
print(True and False) # False
print(True or False) # True
print(False or False) # False
print(not True) # False
print(not False) # True





#hello= '''fuck
#the
#world'''
#print(hello)




# list can edit. insert, delete
a=[1,2,3,4,5,56] # list
person= ["bruce", 34, 185.4, True] # list has many type

b=[] # empty list
bb= list() #empty list

# range(a,b,c) a=begin b=end c=increase width, decrease width
c= list(range(10)) # [0,1,2,3,4,5,6,7,8,9]
print(c)
d= list(range(4,8)) # [4,5,6,7]
print(d)
e= list(range(-2,10,2)) # [-2,0,2,4,6,8]
print(e)
f= list(range(8,-2,-2)) # [8,6,4,2,0]
print(f)


# tuple can't edit, insert, delete
tup=(3,5,6,7,8)
person2=("dick",22,179.34,True)
onlyone_tuple= (3,) # only one element tuple

cc= tuple(range(10)) # (0,1,2,3,4,5,6,7,8,9)
print(c)
dd= tuple(range(4,8)) # (4,5,6,7)
print(d)
ee= tuple(range(-2,10,2)) # (-2,0,2,4,6,8)
print(e)
ff= tuple(range(8,-2,-2)) # (8,6,4,2,0)
print(f)





# tuple convert list
# list convert tuple

a=list(range(0,4))
a=tuple(a)
print(a) # tuple

b=tuple(range(0,4))
b=list(b)
print(b) # list

aa=list("happy birthday to you")
bb=tuple("happy birthday to you")

xyz=[1,2,3]
x,y,z= xyz
print(x,y,z)# x=1 y=2 z=3

# in => when find value use 'in'
# not in 
print('h' in aa) # true
print('b' in bb) # true
print(1 in xyz) # true





# sequence object + sequence object can be

a=list(range(5)) # 0,1,2,3,4
b=list(range(5,11)) #5,6,7,8,9,10
print(a+b) # [0,1,2,3,4,5,6,7,8,9,10]

print("rich"+str(10)) # str + str

aa= tuple(range(3))*3
print(aa) # 0 1 2 0 1 2 0 1 2
fucking= "fucking"*3
print(fucking) # fuckingfuckingfucking

# len = list or tuple of size
# when find list or tuple of size
# arr/sizeof(int)
listsize= [2,4,5,6,34,634]
print(len(listsize)) # 6
strsize="i'm rich"
print(len(strsize)) # 8

# find index = arr[i]
practice=[24,45,657,79,574,4325,222]
print(practice[0], practice[2], practice[4],sep=",") # 24, 657, 574
print(practice[-1], practice[-3], practice[-5], sep=",") # 222, 574, 657 reverse print[-1]
# -1 is last index 
print(practice[len(practice)-1 ]) # 222 find last index

r=range(0,10,2)
print(r[2]) # 4


# allocation list value

a=[0,0,0,0,0]
a[0]=24; a[1]=35; a[2]=111
print(a) # 24,35,111,0,0
del(a[1]) # del = delete index
print(a)

aa=list(range(0,10))
print(aa[0:4]) # 0,1,2,3 index 0 ~ index 4 slice
print(aa[3:7]) # 3,4,5,6 # slice mid part
print(aa[2:9:2]) # 2,4,6,8 # slice 2 to 9 increase 2++
print(aa[:7]) # 0,1,2,3,4,5,6 # skip the first index so [0] ~ [num]
print(aa[7:]) # 7,8,9 # skip last index so [num] ~ [last]
print(aa[:9:2]) # [0] ~ [9] increase 2++
print(aa[5::2]) # [5] ~ [last] increase 2++
print(aa[:]) # all list

r=range(10)
aaa= list(r[:7:2]); print(aaa) # 0,2,4,6 

# a=(0,0,0,0,0) => tuple can't allocation
# aa=range(0,10,2) => range can't allocation
# aaa= "fuck you" => str can't allocation
# thus tuple, range, str only can read not write 값변경 불가 



# allocation used slice
a=list(range(10))
a[4:8]= [45,34,24,646]
print(a) # 0,1,2,3,45,34,24,646,8,9
a[2:8:2]=[99,88,77] # 2 ~ 8 increase 2++ alloc value
print(a) # 0,1,99,3,88,34,77,646,8,9


b=list(range(10))
b[4:5]=['a','b','c','d','e','f']
print(b) # 0,1,2,3,a,b,c,d,e,f,5,6,7,8,9 => changed list size
del(b[2:8:2]) # 2 ~ 8 increase 2++ del index
print(b)


# dictionary
# dictionary = {'key1':value1, 'key2':value2}
# key = int, float, str, bool but list, dictionary can't
# value = all type ex)int, float, str, bool, class, list, ditionary

powerlifter={'bench press':120,'squart':210,'deadlift':230}

dic1={} # empty dictionary
dic2=dict() # empty dictionary

print(powerlifter['bench press'], powerlifter['squart'],sep=",") # 120 210
powerlifter['bench press']= 140 # bench press alloc
powerlifter['squart']= 240 # squart alloc

powerlifter['military press']= 100 # there are no 'military press' in dic so new key alloc(???)

# when find key use 'in'
# 'not in' =>
print('bench press'in powerlifter) # true
print('arm curl'in powerlifter) # false

# when find dictionary key size
print(len(powerlifter)) # 4





# if
x= 10
if x==10: # :colon
    print(True) # 4space

if x==20:
    pass # pass is continue

# 2 if
if x==20:
    print("20")
else:
    print("not 20")

if True: # if true if code operate
    print("true")
else:
    print("False")

if 123: # not 0 is true 0 is false
    print("true")
else:
    print("false")

if "hello": # str is not empty true
    print("true")
else:
    print("false")

if "": # str empty is false so else code is operated
    print("true")
else:
    print("false")
# if code 0,None,'' is false but
if not 0:
    print(True) # true
if not None:
    print(True) # true
if not "":
    print(True) # true

# The following grammar is treated as a False.
# None, 0, '', empty list, tuple, dictionary, set

a,b=20,34

if a==20 and b==34:
    print(True) # true

button = int(input())
if button == 1:
    print("1")
elif button == 2:
    print("2")
elif button== 3:
    print("3")
else :
    print("over")




#loop for grammer
for i in range(4): # range generates sequence number
    print("loop ") # 10 loop

for i in range(5):
    print("loop test",i,sep=",") # 0,1,2,3,4
print("\n")
for i in range(3,6):
    print("loop test",i,sep=",") # 3,4,5
print("\n")
for i in range(2,8,2):
    print("loop test",i,sep=",") # 2,4,6
print("\n")
for i in range(10,0,-1):
    print("loop test", i, sep=",")  # 10,9,8,7,6,5,4,3,2,1
print("\n")
for i in reversed(range(5)):
    print("loop test", i, sep=",")  # 4,3,2,1,0

#count= int(input())
#for i in range(count):
#   print("loop test", i, sep=",")

# for loop can use list, tuple, str
a= list(range(10,41,10))
for i in a:
    print(i,sep=",",end="")
print("\n")
b= ("bench","squart","deadlift")
for index in b:
    print(index)
print("\n")
for letter in "Rich":
    print(letter,end=",")
print("\n")
for letter in reversed("Rich"):
    print(letter,end=",")


# while loop
# Conditional expression is true so operate
i=0 # initail sentence
while i < 3: # only true
    print("test")
    i+=1
    
j=10
while j > 0: # 반대로 감소시키면서도 가능
    print("dec")
    i-=1
    
r = random.randrange(1,101) # 랜덤

while True: #랜덤숫자 맞추기
    n = int(input("입력"))
    if r>n:
        print("작음 더 큰 수 입력하셈")
    elif r<n:
        print("큼 더 작은 수 입력")
    else :
        print("맞춤 숫자는 %d" %r)
        break 
       
dice = [1, 2, 3, 4, 5, 6]
random.choice(dice) # 주사위 중 무작위 출력

#while 1:    # 0이 아닌 숫자는 True로 취급하여 무한 루프로 동작
    #print('Hello, world!')
#while 'Hello':    # 내용이 있는 문자열은 True로 취급하여 무한 루프로 동작
    #print('Hello, world!')
    
#break: 제어흐름 중단 반복문 빠져나옴
#continue: 제어흐름 유지, 코드 실행만 건너띔

i=100
while True: 
    print(i)
    i+=1
    if(i==50) #50되면 빠져나온다
        break 
        
for i in range(100):       # 0부터 99까지 증가하면서 100번 반복
    if i % 2 == 0:         # i를 2로 나누었을 때 나머지가 0면 짝수
        continue           # 아래 코드를 실행하지 않고 건너뜀 continue 다음 아랫줄만 실행을 안함
    print(i)
    

    
#리스트와 튜플 응용하고 사용하기
#append: 요소 하나를 추가
#extend: 리스트를 연결하여 확장
#insert: 특정 인덱스에 요소 추가

a = list(range(0,401,100))
a.append(500) #마지막에 500 추가
#물론 빈리스트에도 추가가능

aa = list(range(0,401,100))
aa.append([500,501])
print(a) #[100,200,300,400,[500,501]] 길이는 4임 

b = list(range(5))
b.extend([6,7])
print(b) #0,1,2,3,4,6,7 길이는 7임 extend에 전달된 길이만큼 증가

>>> a = [10, 20, 30]
>>> a.insert(2, 500)
>>> a
[10, 20, 500, 30]
>>> len(a)
4

c= list(range(5))
c.insert(2,99) #insert는 원하는 위치에 삽입
print(c) # 0,1,99,2,3,4 [2]번째 인덱스에 99 추가 

#insert(0, 요소): 리스트의 맨 처음에 요소를 추가 insert는 요소 하나만 추가한다. 
#insert(len(리스트), 요소): 리스트 끝에 요소를 추가 이건 append와 같다

#>>> a = [10, 20, 30] #리스트 중간에 여려 요소를 삽입하고 싶다면
#>>> a[1:1] = [500, 600] #요소와 끝을 같게하면 덮어쓰지 않으면서 삽입가능
#>>> a
#[10, 500, 600, 20, 30]



l=list(range(1,5+1))
l.pop() # pop()은 마지막 요소삭제후 반환
print(l) # 1,2,3,4

l.pop(1) #원하는 인덱스 삭제 pop(0)은 맨처음
print(l) # 1,3,4
# pop 대신 del 사용해도 가능

l.remove(3) # 인덱스가 아닌 값을 찾아 삭제 중복이 있다면 처음 찾은 값만 삭제
l.insert(1,4)

l.index(4) # 값의 인덱스 구하기 가장 첨 찾은 인덱스를 구한다 튜플도 마찬가지
l.count(4) # 값이 몇개있는지 구함 튜플도 마찬가지로 같이씀
l.reverse() # 뒤집음

l.sort() # 오름차순 sort 와 sorted 둘의 차이 전자는 정렬 후자는 새 리스트 생성
l.sort(reverse=True) # 내림차순

l.clear() # 모든요소삭제 빈리스트
del l[:] #요것도 모든요소삭제

# 메서드를 사용하지않고 슬라이스로 조작가능
l=list(range(1,5+1))
l[len(l):]=[500,600]
print(l)

# 리스트가 비어있는지 확인
ll=list(range(1,5+1))
ll.clear()

if not ll:
    print("리스트가 비어 있으면 트루")
if ll:
    print("리스트에 내용이 있으면 트루")

a= list(range(1,5+1))
b=a # 둘은 같은 객체 새로생성된게 아님 얕은복사
print(a is b) # 트루 ~
b[2]='tetetest'
print(a,b) # 값을 변경하면 둘다 변함 공유
b=a.copy() # 깊은복사 copy메서드는 리스트로 변수불가
print(a is b) # 객체다름 ~

t1=tuple(range(1,5+1))
t2=tuple(range(6,10+1))
t3=t1+t2
#반복문으로 리스트 출력 인덱스랑 값
for i,value in enumerate(t3): #enumerate를 씀
    print(i,value)

# 큰값 작은값 구하기
# max, min 쓰거나 소트해서 0번쨰 찾거나 직접 짜거나 튜플도 사용가능
print(max(t3))
print(min(t3))
print(sum(t3)) # 합계 출력

# 리스트표현식 
l = [i for i in range(10) if i % 2 == 0]    # 0~9 숫자 중 2의 배수인 숫자(짝수)로 리스트 생성 튜플도 사용가능

gugudan = [i * j for j in range(2, 10)
           for i in range(1, 10)] # 반복문 여러개 써도 가능


# map은 리스트의 요소를 지정된 함수로 처리해주는 함수
# map은 원본 리스트를 변경하지 않고 새 리스트를 생성

floatl = [1.2, 2.5, 3.7, 4.6] #실수 정수 변환
intl = list(map(int, floatl))
strl = list(map(str,range(0,5+1))) # 스트링으로 변환

test= map(int,input().split()) # 띄어쓰기로 구분해 정수 받기
test= list(map(int,input().split())) # 정수받고 리스트로 생성
print(type(test)) #list 

import time
import keyword
import sys

print(keyword.kwlist) # 파이썬 예약어 출력

twodemension = [ #2차원리스트
                [10, 20],
                [30, 40],
                [50, 60]]
print(twodemension[1][0]) # 2차원배열처럼 [][] 대괄호 2개로 접근

#2차원 리스트의 여러가지 출력방법
for first,last in twodemension:
    print('(',first+last,')')
    print(first,last) #2차원 리스트 출력 이건 가로 길이가 맞아야 함

for i in twodemension:
    for j in i:
        print(j, end=" ")
print()
for i in range(len(twodemension)):
    for j in range(len(twodemension[i])):
        print(twodemension[i][j],end=" ")
        
        
        
# 리스트 응용하기    
import copy

l=[]
for i in range(10): # 반복문으로 1차원 리스트 생성
    l.append((0))

twodemension=[]
for i in range(3): # 반복문으로 2차원 리스트 생성
    line=[]
    for j in range(2):
        line.append(0)
    twodemension.append(line)

l=[[0 for j in range(2)] for i in range(3)] # 리스트표현식으로 2차원 리스트생성

# 가변길이 리스트 만들기
a=[3,1,2,4,5]
l=[]

for i in a:
    line=[]
    for j in range(i):
        line.append(0)
    l.append(line)
# [[0, 0, 0], [0], [0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]

li = [[0] * i for i in [3, 1, 3, 2, 5]] # 리스트표현식
# 2차원 리스트의 깊은복사
aa=[[2*j for j in range(2)]for i in range(3)]
bb=copy.deepcopy(aa)
bb[0][0]= 5000




# 문자열 다루기
str="aaa bbb ccc"
str=str.replace("aaa","sss") # sss bbb ccc

# 문자바꾸기 (?)
table= str.maketrans('aeiou','12345')
'apples'.translate(table)
print(table)
pass

# 문자열 분리하기
string="apple banana cherry democracy earth"
string= string.split()  # 스페이스, 탭, 엔터기준으로 문자열 나눠줌
print(string)
# 괄호에 값 넣어주면 그 값 기준으로 나눠서 리스트 생성


# 문자열 연결하기
# string = ' '.join(string) # 리스트를 하나의 문자열로
# print(string)

string = '-'.join(string) # 각 인덱스요소 사이 마이너스로 연결
print(string)

# 대소문자 변환
rich="rich man".upper(); print(rich) # 대문자로
rich="rich man".lower(); print(rich) # 소문자로

# 공백삭제
strtest="   Snake"
print(strtest.lstrip()) # 왼쪽 공백 삭제
strtest="   Snake    "
print(strtest.rstrip()) # 오른쪽 공백 삭제
strtest="   Snake    "
print(strtest.strip()) # 양쪽 공백 삭제
#공백삭제 함수안에 특정 문자를 넣으면 삭제한다

import string
# 구두점 삭제 방법

gudu= "$&/+ SNAKE^^~~"
print(gudu.strip(string.punctuation))
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# 문자열 정렬
strsort="LION"
strsort.ljust(10) # 지정된 길이로 만든위 왼쪽으로 정렬 남는공간을 공백으로
print(strsort) # L I O N □ □ □ □ □ □
strsort.rjust(10) # □ □ □ □ □ □ L I O N # 오른쪽 정렬

strsort.center(10) # □ □ □ L I O N □ □ □ # 센터정렬

# 메서드 체이닝 메서드를 연속해서 호출 그렙과 파이프라인같은거라 보면 됨
str="snake"
str.rjust(10).upper() # 오른정렬하고 대문자로

# 문자열 왼쪽에 0 채우기
# zfill (zero fill)
print('35'.zfill(4)) # 0035
print('3.5'.zfill(6)) # 0003.5
print('Fuck'.zfill(8)) # 0000Fuck

# 문자열 찾기
fruits="banana watermelon"
print(fruits.find('na')) # 찾은 문자열의 인덱스 반환
print(fruits.rindex('na')) # 오른쪽부터 찾음
print(fruits.count('na')) # 문자열 몇개 나오는지 카운트

# 문자열 포매팅
bench =150
deadlift = 20
squart = 6700
print("내 3대 무게는 벤치: {} 데드: {} 스쾃:{}입니다.".format(bench,deadlift,squart))



