import pickle
import nltk
from nltk.util import ngrams
from collections import Counter
from nltk.corpus import stopwords
import re
x=[]
text1=open("D:\\New folder (2)\\cOPN.txt")
t=text1.read()
t22=t.lower()
t222=t22.replace('-',' ')
t2k=t222.replace('.',' ')
t1=t2k.replace('?'," ")
t11=t1.replace(","," ")
d=t11.split()
f=[word for word in d ]
k=" ".join(f)
trigrams1=ngrams(k.split(),3)
count=Counter(trigrams1)
u=count.most_common(500)


for n in range(0,500):
  x.append(u[n][0])

with open("E:\\New folder (2)\\ocean\\opn\\trig.txt", 'wb') as f:
    pickle.dump(x, f)
print (u)
j=len(u)
print (j)
