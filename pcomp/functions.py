from collections.abc import Iterable

def check_arguments(iterable,length):
    if not(isinstance(iterable, Iterable)):
        raise ValueError("Iterable Argument is not Iterable.")
    if not(isinstance(length, int)):
        raise ValueError("Length Argument is not a number.")
    if not(length>0):
        raise ValueError("Length Argument must be >0 .")

def area(iterable,length):
    check_arguments(iterable,length)
    return pow(len(iterable),length)

def pc(iterable,length):
    power = area(iterable,length)
    temp_list = [[None]*length for i in range(power)]
    for i in range(-1,length*-1-1,-1): # negative i
        change = len(iterable)**abs(i+1)
        counter = 0 
        index = 0
        for j in range(power):
            if counter != change:
                temp_list[j][i] = iterable[index]
                counter += 1
            else:
                counter = 0
                if index<len(iterable)-1:
                    index += 1
                else:
                    index = 0
                temp_list[j][i] = iterable[index]
                counter += 1
        result = temp_list
    return result