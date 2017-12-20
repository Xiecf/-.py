#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""标识符检查"""

import string

alphas = string.ascii_letters + '_'
nums = string.digits

print('欢迎进行标识符测试。\n')
print('''标识符至少为2位,可使用数字、字母、下划线;\n首位只能是字母（推荐小写）或下划线;\n不能使用python关键字。
    ''')

myInput = True

while myInput != 'q':
    myInput = input('请输入要测试的标识符或输入‘q’退出测试: ')
    if myInput != 'q':
        if len(myInput) > 1:
            if myInput[0] not in alphas:
                print('''无效：首位必须为字母''')
            else:
                for otherChar in myInput[1:]:
                    if otherChar not in string.printable:
                        print('无效：除首位外，其余位需为字母及数字')
                else:
                    print('合格的标识符')
        else:
            print('无效：标识符至少为2位')
else:
    print("测试结束。")
