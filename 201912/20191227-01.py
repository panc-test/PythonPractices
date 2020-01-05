#往csv文件里写入数据

import csv

with open('data.csv','w') as f:
    w=csv.writer(f)
    w.writerow([1,2,3,4,5])
f.close()

