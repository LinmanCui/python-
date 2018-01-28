def count(*param):
    length = len(param)

    for i in range(length):
        letter = 0
        num = 0
        space = 0
        others = 0
        for each in param[i]:
            if each.isalpha():
                letter += 1
            elif each.isdigit():
                num += 1
            elif each == ' ':
                space += 1
            else:
                others += 1

    print('第%d个字符串共有：英文字母%d个，数字%d个，空格%d个，其他字符%d个。' % （i+1，letter,num,space,others))
