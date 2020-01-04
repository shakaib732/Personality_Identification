import pickle


with open("E:\\New folder (2)\\ocean\\neu\\unig.txt", 'rb') as f:
    a = pickle.load(f)

with open("E:\\New folder (2)\\ocean\\const\\unig.txt", 'rb') as f:
    b = pickle.load(f)

    
c=[val for val in a if val not in b]


with open("E:\\New folder (2)\\Neuroticism(intersections)\\INTERSECTION\\final_intersect_files\\neuro-const.txt", 'wb') as f:
    pickle.dump(c, f)
    print(c)
h=len(c)
print(h)
