# *****
# *****
# *****
# *****
# *****
for i in range(5):
    for j in range(5):
        print("*",end="")
    print()
print()


# *
# **
# ***
# ****
# *****
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()
print()


# *****
# ****
# ***
# **
# *
for i in range(5):
    for j in range(5-i):
        print("*",end="")
    print()
print()

#     *
#    **
#   ***
#  ****
# *****
for i in range(5):
    for j in range(5-1-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
print()

# *****
#  ****
#   ***
#    **
#     *
for i in range(5):
    for j in range(i):
        print(" ",end="")
    for j in range(5-i):
        print("*",end="")
    print()


# pyramid
#   *
#  ***
# *****
num = int(input())
for i in range(num):
    for j in range(num-1-i):
        print(" ",end="")
    for j in range(i*2+1):
        print("*",end="")
    print()



