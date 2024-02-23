import random
l=["apple","potato","mango"]
lives=6
m= [" 0\n     /|\ \n      /\ ",
    "\n     0\n    /|\ \n    /   ",
    "\n     0\n    /|\ \n      ",
    "\n     0\n    /| \n    ",
    " 0\n      |",
    "\n       0\n       "]
w=random.choice(l)
print(w)
d=[]
for i in range(len(w)):
        d+="_"      
print(d)
while "_" in d:
    g=input("guess a letter: ").lower()
    chk=False
    for i in range(len(w)):
        if g == w[i]:
            d[i] = g
            chk = True
            break
    print(d)
    if not chk:
        lives-=1
        print(m[lives-1])

    
if lives==0:
    print("you lost!!!")         
      