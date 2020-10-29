# -*- config:utf-8 -*-
"""
作者:计AI181宋曜通 201806030121
日期：2020年10月15日
"""
num = input("请输入一个自然数")
print(sum(map(int, num)))


setA = eval(input('请输入第一个集合：'))
setB = eval(input('请输入第二个集合：'))
print('交集：', setA & setB)
print('并集：', setA | setB)
print('setA-setB：', setA - setB)

num = int(input('请输入一个自然数：'))
print('二进制：', bin(num))
print('八进制：', oct(num))
print('十六进制：', hex(num))

def Prime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True
n = int(input('请输入一个自然数：\n'))
result=list()
for i in range(2, n):
    if Prime(i)==True:
        result.append(i)
print('返回的素数有：', result)