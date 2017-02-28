# ----------ASKHSH 3 ----------
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

for j in range (i):
    if (s[j]==0):

        for k in range (j,(i-1)):
            p=s[k]
            s[k]=s[k+1]
            s[k+1]=p

print s
