#!/usr/bin/env python3

trueNum = 19
count = 0
while count < 3:
    userNum = int(input('请输入一个数字：'))
    if userNum < 19:
        print('太小')
    elif userNum > 19:
        print('太大')
    else:
        print('对咯')
        break
    count += 1
else:
    print('超过尝试次数')


