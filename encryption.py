t=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrytion(a,b):
    e=""
    for i in a:
        p=t.index(i)
        np=p+b
        e+=t[np]
    print(e)
def decryption(y,z):
    s=""
    for x in y:
        u=t.index(x)
        nu=u-z
        s+=t[nu]
    print(s)
print("do you want to decrypt or encrypt")
text=input("enter anything")
w=input("r or q")
shift=int(input("type shift"))
if w=="r":
    encrytion(text,shift)
if w=="q":
    decryption(text,shift)
        
    
    