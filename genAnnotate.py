import pandas as pd 
import numpy as np

'''
FigTree did not accept GFF3 as inputs 
so wrote the script to read GFF3 and generate
tab-separated CSV

'''

file = '14/sequence (1).gff3'
with open(file, 'r') as f:
    lines = f.readlines()

acclist = []
for l in lines:
    if '##sequence-region' in l:
        acclist.append(l.split(' ')[1])

lines2 = []
for l in lines:
    if 'country' in l:
        lines2.append(l)

lines3 = []
for l in lines2:
    lines3.append(l.split('\t'))

ids = []
for i in lines3:
    id = i[-1].split(';')
    oo = id[0]
    ids.append([oo[oo.find('=')+1:oo.find(':')], id[3]])

ids = np.array(ids)


result = np.zeros([len(acclist), 2], dtype='object')
for i in range(result.shape[0]):
    result[i, 0] = acclist[i]
    result[i, 1] = 'not_defined'
    for j in range(ids.shape[0]):
        if acclist[i] == ids[j][0]:
            country = ids[j][1][ids[j][1].find('=')+1::]
            if ':' in country:
                country = country[:country.find(':')]
            result[i, 1] = country

result = np.concatenate([result, [['OURCASE', 'Brazil']]]) 
    
result = pd.DataFrame(result, columns=['acc', 'country'])
print(result)
result.to_csv('14/annotation.csv' ,sep= '\t', index=False)