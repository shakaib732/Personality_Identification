import pickle

with open("E:\\New folder (2)\\ocean\\opn\\biig.txt", 'rb') as f:
    a = pickle.load(f)

with open("E:\\New folder (2)\\ocean\\agr\\biig.txt", 'rb') as f:
    b = pickle.load(f)

    
c=[val for val in a if val not in b]
print(c)
with open("E:\\New folder (2)\\Openness(intersections)\\INTERSECTION\\fn_inte_bigram\\open-agreb.txt", 'wb') as f:
    pickle.dump(c, f)
h=len(c)
print(h)

