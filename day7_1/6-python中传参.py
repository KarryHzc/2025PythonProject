# 作者: karryhuang
# 2025年07月14日21时02分11秒
# 2416864569@qq.com
import sys

# print(type(sys.argv))
# print(sys.argv)
def write_hello(file_path):
    file = open(file_path, 'w+', encoding='utf8')
    file.write('hello')
    file.close()


if __name__ == '__main__':
    write_hello(sys.argv[1])