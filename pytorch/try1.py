# -*- config:utf-8 -*-
"""
作者:计AI181宋曜通 201806030121
日期：2020年10月21日
"""
import torch
import numpy as np

# np_data=np.arange(6).reshape((2,3))
# torch_data=torch.from_numpy(np_data)
# tensor2array=torch_data.numpy()
# print(
#     '\n numpy',np_data,
#     '\n torch',torch_data,
#      '\n tensor2array',tensor2array,
# )

# data=[-1,-2,1,2]
''
data =[[1,2],[3,4]]
tensor=torch.FloatTensor(data)
data =np.array(data)
print(
    '\n numpy', data.dot(data),
    '\ntorch', tensor.dot(tensor)
)