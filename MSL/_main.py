#####################################################################
# Time experiments                                                  #
# Test the time consumption of BL, BS, and our three MSL algorithms #
# author: @ Wenhui Yu, @ Huidi Zhang                                #
# E-mail: yuwh16@mails.tsinghua.edu.cn                              #
#####################################################################

from BL import BL
from BS import BS
from MSL import MSL
from MSL1 import MSL1
from MSL2 import MSL2
from Library import print_result

## Parameter setting
dataset = 1     # dataset, 0, 1, 2, 3 for corr, inde, anti, and NBA respectively
N = 100000      # point number
Dimension = 3   # dimensions
G_size = 3      # group size

dataset_name = ['corr', 'inde',  'anti', 'NBA']
filename = 'E:\\datasets\\' + dataset_name[dataset] + '_' + str(Dimension) + '.txt'

for i in range(1, 100000):
    i += 1

[layer, t1, t2, t3, t4] = BL(G_size, Dimension, filename, N)
print_result('BL', t1, t2, t3, t4)

[layer, t1, t2, t3, t4] = BS(G_size, Dimension, filename, N)
print_result('BS', t1, t2, t3, t4)

[layer, t1, t2, t3, t4] = MSL1(G_size, Dimension, filename, N)
print_result('MSL1', t1, t2, t3, t4)

[layer, t1, t2, t3, t4] = MSL2(G_size, Dimension, filename, N)
print_result('MSL2', t1, t2, t3, t4)

[layer, t1, t2, t3, t4] = MSL(G_size, Dimension, filename, N)
print_result('MSL', t1, t2, t3, t4)
