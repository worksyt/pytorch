# -*- config:utf-8 -*-
"""
作者:计AI181宋曜通 201806030121
日期：2020年10月21日
"""
import torch
from torch.autograd import Variable

tensor=torch.FloatTensor([[1,2],[3,4]])
variable=Variable(tensor,requires_grad=True)
t_out=torch.mean(tensor*tensor)
v_out=torch.mean(variable*variable)
print(t_out)
print(v_out)