def Dec2Bin(dec):

    temp = []
    result = ''

    while dec:
        quo = dec % 2
        dec = dec //2
        temp.append(quo)  #求余数

    while temp:
        result += str(temp.pop()) #排序

    return result

