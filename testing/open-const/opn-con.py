import pickle
import xlsxwriter

with open("E:\\New folder (2)\\testing\\open\\uni_inter.txt", 'rb') as p:
        a = pickle.load(p)

h=len(a)
workbook=xlsxwriter.Workbook("E:/New folder (2)/Openness(intersections)/INTERSECTION/open-(agr+con+ext+neu)/Open.xlsx")
worksheet=workbook.add_worksheet()

for i in range(0,h):
    worksheet.write(i, 0,a[i])
    


workbook.close()

print('work done')
        
'''with open("E:\\New folder (2)\\ocean\\const\\unig.txt", 'rb') as q:
    b = pickle.load(q)

#print(b)
g=[val for val in a if val in b]
print(g)'''
