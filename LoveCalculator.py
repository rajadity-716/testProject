a=input("Enter name A\n")
print(f"Hello {a}")
b=input("Enter name B\n")
print(f"Hello {b}")
a=list(a).upper()
b=list(b).upper()
c=[]
def name(str1,str2):
    for letter in str1:
        c.append(letter)
    for letter in str2:
        c.append(letter)
    return c
final_name=name(a,b)
t=r=u=e=l=o=v=els=0
def true_check(str):
    for x in str:
        if x=="T":
            t+=1
        elif x=="R":
            r+=1
        elif x=="U":
            u+=1
        elif x=="E":
            e+=1
        else:
            els+=1
    return(t,r,u,e,els)

def love_check(str)   :
    for y in str:
        if y=="L":
            l+=1
        elif y=="O":
            o+=1
        elif y=="V":
            v+=1
        elif y==e:
            e+=1
        else:
            els+=1
    return(l,o,v,e,els)

t,r,u,e1,els1=true_check(final_name)
l,o,v,e2,els2=love_check(final_name)




# a='Aditya'
# b=a.split()
# print (a)
# print (type(a))
# print (b)
# print (type(b))
# c=[*a]
# print(c)
# print (type(c))
# d=[]
# for letter in a:
#     d.append(letter)
# print(d)
# print (type(d))
# e=list(a)
# print (e)
# print (type(e))