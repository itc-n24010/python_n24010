# python_n24010
python 課題　提出
import os, sys
MAX = 2
print(sys.getdefaultencoding())
print(os.path.basename(os.getcwd()))
for i in range(3):
    print(i, end = " ")
    if MAX > i:
        print(MAX)
    else:
        print("#")
