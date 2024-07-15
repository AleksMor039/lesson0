# 4th program
a=13.42
b=42.13
c=(int(a)) # 13
d=(int(b)) # 42
print(c, d)
e=int(a*100%100) #42
f=int(b*100%100) #13
print(e, f)
print(c==f and d==e)
print(c=f or d==e)
