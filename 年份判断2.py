temp = input('请输入年份：')
while not temp.isdigit():
    temp = input('输入的不是数字,请输入数字:')
year = int(temp)
if (year%4 == 0 and year%100 !=0) or (year%400 == 0):
    print('是闰年')
else:
    print('不是闰年')
