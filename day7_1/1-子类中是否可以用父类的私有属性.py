# 作者: karryhuang
# 2025年07月12日12时59分34秒
# 2416864569@qq.com

'''
在Python中，子类不能直接访问父类的私有属性（以双下划线 __ 开头的属性），
但可以通过间接方式访问。以下是结合您代码的详细分析：
父类 A 中的 __age 是私有属性，Python会通过名称重整（Name Mangling） 将其重命名为 _A__age。这意味着：

子类 B 无法通过 self.__age 直接访问（实际会触发 AttributeError）
父类内部方法（如 base_age）可通过重整后的名称访问私有属性


'''
class A:
    def __init__(self):
        self.__age = 18

    def base_age(self):
        print(self.__age)

class B(A):
    # def __init__(self):
    #     super().__init__()
    def get_age(self):
        self.base_age()


if __name__ == '__main__':
    zhangsan = B()
    zhangsan.get_age()