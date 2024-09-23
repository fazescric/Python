
#git commit -m "main" 

lista  = [[[1,2,3,7], [4,5,6]], [[7,8,9], [10,11,12,21], [3,4,11]], [[13,14,15], [16,17,18]]]


#print(lista)

#print(f"lunghezza lista:  {len(lista)}") #lista[0], lista[0][0] primo numero indica la lista il secondo l'elemento

for a in lista:
    for b in a:
        for i in range(len(b)):
            b[i] +=1
            
        
        
#print(lista)

x = 10

x = "ciao"

x = [1,2,3]

def incrementa(valore):
    if isinstance(valore, int) or isinstance(valore, float):
        return valore + 1

    elif isinstance(valore, str):
        return valore + "aggiunto"
    
    else:
        return "tipo non supportato"
    
#per aggiungere metono in una lista usiamo il metodo .append(x)


dati = [1,2, 'ciao', 3.5, [1,2], None, 10, 'mondo', 3.14]

def check(lista):
    stringList = []
    numberList = []
    for i in lista:
        if isinstance(i, int) or isinstance(i, float):
            numberList.append(i)

        elif isinstance(i, str):
            stringList.append(i)
    
        else:
            pass
        
    return (f"String list: {stringList}, Number list: {numberList}")
    
    
print(check(dati))
    





