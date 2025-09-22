a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index=0
while (index := a.find('is',index)) != -1:
    print(index)
    index+=1
print('End')

