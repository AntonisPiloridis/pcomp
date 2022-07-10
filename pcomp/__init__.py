def all(array=None,length=None):
    if array and length:
        x = len(array)
        y = length
        power = x**y
        lista = []
        for i in range(power):
            lista.append([0]*length)
        for i in range(-1,length*-1-1,-1):
            change = x**abs(i+1)
            counter = 0
            dikt = 0
            for j in range(power):
                if counter != change:
                    lista[j][i] = array[dikt]
                    counter +=1
                else:
                    counter = 0
                    if dikt<len(array)-1:
                        dikt+=1
                    else:
                        dikt = 0
                    lista[j][i] = array[dikt]
                    counter+=1
        result = []
        for i in lista:
            temp = ""
            for j in i:
                temp+=str(j)
            result.append(temp)
        return result
    else:
        return None

def area(array=None,length=None):
    if array and length:
        x = len(array)
        y = length
        power = x**y
        return power
    else:
        return None