import random
a =["q","w","e","r",'t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
s= ["!","@","#","%","^","&","*","(",")","+","-","/",";"]
n=['1','2','3','4','5','6','7','8','9','0','10']
password =""
l=int(input("enter a number of letters"))
p=int(input("enter a number of symbol "))
z=int(input("enter number numeric values"))
for i in range(0,l+1):
    char=random.choice(a)
    password+=char
for x in range(0,p+1):
    sym=random.choice(s)
    password+=sym
for y in range(0,z+1):
    num=random.choice(n)
    password+=num
print(password)
