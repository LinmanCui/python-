num = '0123456789'
alp = 'abcdefghijklmnopqrstuvwxyz'
spe = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''

passwrd = input('请输入密码：')

length = len(passwrd)
while (passwrd.isspace() or length == 0) :
    passwrd = input('密码为空，请输入密码：')

if length <= 8:
    flag_len = 1
elif 16 > length >8:
    flag_len = 2
else:
    flag_len = 3

    
flag_con = 0

for each in passwrd:
    if each in spe:
        flag_con += 1
        break
    if each in alp:
        flag_con += 1
        break
    if each in num:
        flag_con += 1
        break

while 1:
    print("您的密码安全级别评定为：", end='')
    if flag_len ==1 or flag_con == 1:
        print('低')
        
    elif flag_len == 2 or flag_con == 2:
        print('中')
        
    elif flag_len == 3 and falg_con == 3:
        print('高')
        break

    print("请按以下方式提升您的密码安全级别：\n\
	    \t1. 密码必须由数字、字母及特殊字符三种组合\n\
	    \t2. 密码只能由字母开头\n\
	    \t3. 密码长度不能低于16位")
    break

