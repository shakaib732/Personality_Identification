import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
text1=open("D:\\New folder (2)\\cEXT.txt")
t=text1.read()
t22=t.lower()
t222=t22.replace('-',' ')
t2k=t222.replace('.',' ')
t1=t2k.replace('?'," ")
t11=t1.replace(","," ")
d=t1.split()
sid = SentimentIntensityAnalyzer()
pos_word_list=[]
neu_word_list=[]
neg_word_list=[]

for word in d:
    if (sid.polarity_scores(word)['compound']) >= 0.5:
        pos_word_list.append(word)
    elif (sid.polarity_scores(word)['compound']) <= -0.5:
        neg_word_list.append(word)

    
def getUniqueWords(allWords) :
    uniqueWords = [] 
    for i in allWords:
        if not i in uniqueWords:
            uniqueWords.append(i)
    return uniqueWords



print('Positive :',getUniqueWords(pos_word_list))
list1=getUniqueWords(pos_word_list)
n=len(list1)
print('count=',n)
print("\n\n" )
print('Negative :',getUniqueWords(neg_word_list))
list1=getUniqueWords(neg_word_list)
n=len(list1)
print('count=',n)
