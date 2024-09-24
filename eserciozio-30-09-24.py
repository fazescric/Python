def func(lista):
    numberList = []
    numberSum = 0
    numeriMedia = 0
    for i in lista:
        if isinstance(i, int) or isinstance(i, float):
            numberList.append(i)
            numberSum += i
            
        else: 
            pass
        
    numeriMedia = numberSum/len(numberList)
    
    return numberList, numberSum, numeriMedia

dati = [1,2, 'ciao', 3.5, [1,2], None, 10, 'mondo', 3.14]

print(func(dati))