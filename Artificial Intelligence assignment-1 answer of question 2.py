print("only answer as yes or no")
l=[]
l2=[]
a=input("i am a human being: ")
if a!='yes' and a!='no':
    print("wrong input")
    exit()
else:
    l.append(a)
b=input("i am good: ")
if b!='yes' and b!='no':
    print("wrong input")
    exit()
else:
    l.append(b)
c=input("Good graders study well: ")
if c!='yes' and c!='no':
    print("wrong input")
    exit()
else:
    l.append(c)
d=input("Humans love graders: ")
if d!='yes' and d!='no':
    print("wrong input")
    exit()
else:
    l.append(d)
e=input("Every human does not study well: ")
if e!='yes' and e!='no':
    print("wrong input")
    exit()
else:
    l.append(e)
print(l)
if l[0]=="yes" and l[1]=="yes" and l[2]=="yes" and l[3]=="yes" and l[4]=="no":
    print("every human is good grader")
else:
    print("No, every human is not a good grader")