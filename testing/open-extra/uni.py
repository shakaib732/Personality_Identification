import pickle

with open("E:\\New folder (2)\\testing\\open\\uni_inter.txt", 'rb') as p:
        a = pickle.load(p)
        
with open("E:\\New folder (2)\\ocean\\ext\\unig.txt", 'rb') as q:
    b = pickle.load(q)

#print(b)
g=[val for val in a if val in b]
print(g)
