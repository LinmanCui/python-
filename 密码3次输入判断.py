count = 3
password = '1234abc'

while count:
    temp = input('请输入密码：')
    if password == temp:
        print('答对了')
        break
    elif '*' in temp:
        print('密码中不能含有*','你还有',count,'次机会',end=' ')
        continue
    else:
        print('密码输入错误','你还有',count-1,'次机会',end=' ')
    count -= 1
