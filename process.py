import sys
import os
def back_propagate(lines):
    L3=lines[0]
    L4=lines[1]
    if len(L4)>2:
        return 3
    if len(L3)>2:
        return 2

path_to_file='data.txt'
text = open(path_to_file, 'rb').read().decode(encoding='utf-16')
file = open('./new.txt', 'w')
lines = text.split('\n')
adrs=0
hikes=0

while adrs < len(lines):
    L1=lines[adrs]
    L2=lines[adrs+1]
    L3=lines[adrs+2]
    L4=lines[adrs+3]
    if L1[len(L1) - 1] == ' ':
        L1 = L1[:len(L1) - 1]
    if L2[len(L2) - 1] == ' ':
        L2 = L2[:len(L2) - 1]
    if L3[len(L3) - 1] == ' ':
        L3 = L3[:len(L3) - 1]
    if len(L4) is not 0:
        if L4[len(L4) - 1] == ' ':
            L4 = L4[:len(L4) - 1]
    if len(L1)>2 and len(L2)>2 and len(L3)>2 and len(L4)<=1:
        file.write(L1+L2+L3+L4)
        adrs+=4
        hikes+=1
    else:
        adrs+=back_propagate((L3,L4))
file.close
print('\nWord prossessing completed. {} Haikus in the "new.txt" file.\n'.format(hikes))
########################################################################################################################

'''
#general prossessing
import sys
import word2vec
import os

path_to_file='五言絕句/raw.txt'
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
lines = text.split('\n')

type="五言絕句"
if os.path.exists('./' + type + '/' + type + '.txt'):
    os.remove('./' + type + '/' + type + '.txt')
file = open('./' + type + '/' + type + '.txt', 'a')

for i in lines:

    if len(i)==25:
        file = file.write(i)

text.close()
file.close()
print ("word prossessing completed")'''