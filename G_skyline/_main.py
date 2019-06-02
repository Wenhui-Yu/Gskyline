##################################################################
# Time experiments                                                #
# Test the time of PWise, UWise, F_PWise, and F_UWise algorithms  #
# author: Wenhui Yu                                               #
# E-mail: yuwh16@mails.tsinghua.edu.cn                            #
##################################################################

from DSG import DSG
from UWise import UWise
from PWise import PWise
from F_UWise import F_UWise
from F_PWise import F_PWise

## Parameter setting
dataset = 1     # dataset, 0, 1, 2, 3 for corr, inde, anti, and NBA respectively
N = 100000      # point number
Dimension = 3   # dimensions
G_size = 3      # group size

dataset_name = ['corr', 'inde',  'anti', 'NBA']
filename = 'E:\\datasets\\' + dataset_name[dataset] + '_' + str(Dimension) + '.txt'

for i in range(0, 100000):
    i += 1

dsg = DSG(filename, G_size, N)
[g_skyline, t1, t2] = PWise(G_size, dsg)
print 'PWise  ', t1
[g_skyline, t1, t2] = UWise(G_size, dsg)
print 'UWise  ', t1
[g_skyline, t1, t2] = F_PWise(G_size, dsg)
print 'F_PWise', t1
[g_skyline, t1, t2] = F_UWise(G_size, dsg)
print 'F_UWise', t1
