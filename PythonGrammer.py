# is, not, in, del

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

print(4,end='') # end is many line show one line
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
# key = int, float, bool but list, dictionary can't
# value = all type ex)int, float, bool, class, list, ditionary

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
