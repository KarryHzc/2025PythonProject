# 作者: karryhuang
# 2025年07月12日13时04分58秒
# 2416864569@qq.com
# 如果 两个模块，存在 同名的函数，那么 后导入模块的函数，会 覆盖掉先导入的函数
from module1 import test1
from module2 import test1 as module2_test1
import random

test1()
module2_test1()

print(random.__file__)  #查看模块所在路径

random.randint(1,3)


'''
from module1 import test1
from module2 import test1 as module2_test1
import random

test1()
module2_test1()

print(random.__file__) #查看模块所在路径
random.randint(1,3)
'''