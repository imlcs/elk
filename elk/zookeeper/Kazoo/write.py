#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: write.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com 
#  Created Time: 2018-09-13 16:31:25
#########################################################################

#!/usr/bin/py3

filename = '/tmp/filename'

f = open(filename,'w')
f.write('1\n')
f.close()
f = open(filename,'a')

for i in range(1,11):
    f.write(str(i) + '\n')
f.close()

