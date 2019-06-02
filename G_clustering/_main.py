################################################################
# Time experiments                                             #
# Test the time of Maximum_dominance and RG-skyline algorithms #
# author: Wenhui Yu,                                           #
# E-mail: yuwh16@mails.tsinghua.edu.cn                         #
################################################################

from DSG import DSG
from UWise import UWise
from g_clustering import g_clustering
from Library import repre_output
from brute_force import brute_force
from maximum_dominance import maximum_dominance
import time

## Parameter setting
k = 6               # number of representative groups
G_size = 2          # group size
N = 100000          # point number
Dimension = 3       # dimensions
dataset = 1         # set dataset
iteration = 0       # interaction for clustering
dataset_name = ['corr', 'inde', 'anti', 'NBA']
t = time.time()

print '\nNumber of representative groups :  ', k
print 'Group size:                        ', G_size
print 'Dimension:                         ', Dimension
print 'Point_point_number:                ', N
print 'Dataset_type:                      ', dataset_name[dataset]
print 'Iterations:                        ', iteration

filename = 'E:\\datasets\\' + dataset_name[dataset] + '_' + str(Dimension) + '.txt'

print '\nConstructing DSG...',
test = DSG(filename, G_size, N)
print 'Finished'
print 'Constructing G-skyline...',
g_skyline = UWise(G_size, test)
print 'Finished   Length of G-skyline:', len(g_skyline)

[represent_skyline, time] = maximum_dominance(g_skyline, k, filename, test, N)
print '\nMaximum_dominance:   ', time
#repre_output(g_skyline, represent_skyline, 1)
#0 to output repr group, 1 to output each repr group and corresponding groups, 2 for NBA

[represent_skyline, time] = brute_force(g_skyline, G_size, Dimension, k, iteration)
print 'RG_skyline_B:        ', time
#repre_output(g_skyline, represent_skyline, 0)

[represent_skyline, time] = g_clustering(g_skyline, G_size, Dimension, k, iteration)
print 'RG_skyline:          ', time
#repre_output(g_skyline, represent_skyline, 1)
