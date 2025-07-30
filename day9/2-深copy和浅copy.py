# 作者: karryhuang
# 2025年07月24日13时36分16秒
# 2416864569@qq.com
import copy


def use_list_copy():
    """
    使用列表自身的copy
    :return:
    """
    a = [1, 2, 3]
    b = a.copy()
    b[0] = 10
    print(a)
    print(b)


def use_copy():
    """
    使用copy包中的copy
    :return:
    """
    c = [1, 2, 3]
    d = copy.copy(c)
    d[0] = 10
    print(id(c))
    print(id(d))
    print(c)
    print(d)


def use_copy2():
    """
    copy是浅copy，只做第一层copy
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.copy(c)
    print(id(c))
    print(id(d))
    a[0] = 10
    print(f'c--{c}')
    print(f'd--{d}')
    print('-' * 50)
    print(id(c[0]), id(c[1]))
    print(id(d[0]), id(d[1]))


def use_deepcopy():
    """
    递归去copy，不管有多少层，都会新做一个空间，把数据拿进来
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    print(id(c))
    print(id(d))
    a[0] = 10
    print(f'c--{c}')
    print(f'd--{d}')
    print('-' * 50)
    print(id(c[0]), id(c[1]))
    print(id(d[0]), id(d[1]))


class Hero:
    def __init__(self, name, blood):
        self.name = name
        self.blood = blood
        self.equipment = ['鞋子', '指环']


def use_copy_own_obj():
    """
    实际对于自定义对象的练习
    :return:
    """
    old_hero = Hero('蚂蚁', 90)
    new_hero = copy.deepcopy(old_hero)
    new_hero.blood = 80  #新对象修改后，原对象不会受到任何影响
    new_hero.equipment.append('药水')
    print(old_hero.blood)
    print(old_hero.equipment)


if __name__ == '__main__':
    # use_copy()
    # use_copy2()
    # use_deepcopy()
    use_copy_own_obj()