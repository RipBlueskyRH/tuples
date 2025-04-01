#input1=str(input("enter a series of numbers or letters to see if it is a palendrome"))
#input2=""
#for i in input1:
#    input2=i+input2
#if input1==input2:
#    print("the number is a palendrome")
#else:
#    print("the number isn't a palendrome")


def palin(list):
    e=(len)-1
    s=0
    while s<e:
        if list[s]!=list[e]:
            return False
        s=s+1
        e=e+1
    return True

tuple1=(1, 2, 3, 4, 3, 2, 1)
if palin(tuple1):
    print("it'sa palindrome")
else:
    print("it isn't a palindrome")