# -*- config:utf-8 -*-
"""
作者:计AI181宋曜通 201806030121
日期：2020年10月15日
"""
from __future__ import print_function
import torch
#张量（Tensors)
x = torch.Tensor(3,4)#初始化一个3*4的矩阵
# print(x)
# x = torch.rand(5, 3)#初始化一个随机的矩阵
# print(x)
x.size()#获取矩阵大小
# print(x.size())
# y = torch.rand(5, 3)
# print(x + y)
# print(torch.add(x, y))
# #创建一个输出向量
# result = torch.Tensor(5, 3)
# torch.add(x, y, out=result)
# print(result)
# y.add_(x)#x加到y上
# print(y)
# #numpy桥
# a = torch.ones(5)#把Torch张量转换为numpy数组
# print(a)
# b = a.numpy()
# print(b)
# print(type(b))
# #使用.cuda()可以将张量移动到GPU上
# if torch.cuda.is_available():
#     x = x.cuda()
#     y = y.cuda()
#     x + y
#自动求导
from torch.autograd import Variable
x = Variable(torch.ones(2, 2), requires_grad=True)
print(x)
y = x + 2
print(y.grad_fn)
print(x.grad_fn)