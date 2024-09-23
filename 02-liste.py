

lista  = [[[1,2,3,7], [4,5,6]], [[7,8,9], [10,11,12,21], [3,4,11]], [[13,14,15], [16,17,18]]]


print(lista)

print(f"lunghezza lista:  {len(lista)}") #lista[0], lista[0][0] primo numero indica la lista il secondo l'elemento

for a in lista:
    for b in a:
        for i in range(len(b)):
            b[i] +=1
            
        
        
print(lista)


