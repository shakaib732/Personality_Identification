import pickle

with open("E:\\New folder (2)\\ocean\\ext\\trig.txt", 'rb') as f:
    a = pickle.load(f)

with open("E:\\New folder (2)\\ocean\\const\\trig.txt", 'rb') as f:
    b = pickle.load(f)

    
c=[val for val in a if val not in b]
print(c)

with open("E:\\New folder (2)\\Extraversion(intersections)\\INTERSECTION\\fn_inte_trigram\\extra-const.txt", 'wb') as f:
    pickle.dump(c, f)

h=len(c)
print(h)
