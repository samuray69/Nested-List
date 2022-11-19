a = [40,30,3,25,1,5,2,3,4,2,2,23,5]
b =[3,4,5,4,3,23,5,3223,23,23]
c =[4,3,2,2,23,2,23,23,5,2,32]
sum = 0
for i in a:
    for j in range(2,6):
       if i%j==0:
           sum+=i
print(sum)
multi = 1
sum_1 = 0
for h in a:
    if h%2==0:
        sum_1+=h
    if h%sum_1==0:
        multi*=1
print(multi)
sum_2=0
for t in range(len(b)):
    if t%2!=0:
        sum_2+=t
sum_3 = 0
for y in range(len(a)):
    if y%2==0:
        sum_3+=y
if sum_2>sum_3:
    b = b.append(a[-1])
sum_4 = 0
sum_5 = 0
for m in range(len(c)):
    if m%2!=0:
        sum_4+=m
    else:
        sum_5+=m
    if sum_4>sum_5:
        b.sort()
        #harcnel
    else:
        a.pop(5)
if len(b)<len(a)and len(b)>len(c):
    a.clear()
    a.append(c)
if a[0] + a[-1]>10:
    b.reverse()
    b.append(c[int(len(c)/2)])
x = a + b + c
print(x)
