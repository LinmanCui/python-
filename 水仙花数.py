temp = input('输入3位数:')
num = int(temp)
a = num/100
temp1 = num%100
b =  temp1/10
c = temp1%10
if num == a**3 + b**3 +c**3:
    print('水仙花数')
else:
    print('不是水仙花数')
 
