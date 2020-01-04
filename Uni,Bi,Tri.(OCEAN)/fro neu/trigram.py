import pickle
import nltk
from nltk.util import ngrams
from collections import Counter
from nltk.corpus import stopwords
import re
a=[]
text1=open("D:\\New folder (2)\\cNEU.txt")
t=text1.read()
t22=t.lower()
t222=t22.replace('-',' ')
t2k=t222.replace('.',' ')
t1=t2k.replace('?'," ")
t11=t1.replace(","," ")
d=t11.split()
f=[word for word in d ]
k=" ".join(f)
Trigrams1=ngrams(k.split(),3)
count=Counter(Trigrams1)
u=count.most_common(500)
print (u)
j=len(u)
print (j)

for n in range(0,500):
  a.append(u[n][0])
  


with open("E:\\New folder (2)\\ocean\\neu\\trig.txt", 'wb') as f:
   pickle.dump(a, f)







