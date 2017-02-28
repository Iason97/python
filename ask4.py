#----------ASKHSH 4------------
from __future__ import division

q=0
q=input("DWSE EPILOGH  \n 1 gia  OLH LISTA \n 2 gia JEXVSRISTA KATHE STOIXEIO  ")
if (q==1):
    separator = " "
    s = map(int, raw_input("Enter your list separating elements with space : ").split(separator))
    i = len(s)
elif (q==2):
    i= input (" plhthos stoixeiwn listas")
    s=list()
    for x in range (i):
        c=input ("Dwse stoixeio listas")
        s.append(c)
b=list(s)
b.remove(max(b))
b.remove(min(b))
b.remove(max(b))
b.remove(min(b))

i-=4
x=sum(b)
s2=0.0
float (s2)

for k in range(i):

    s2= s2 + (b[k]-(x/i))**2

s1=0
float (s1)
s1=(s2 / i)**(1/2)
print (s1)
