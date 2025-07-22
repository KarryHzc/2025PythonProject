# 作者: karryhuang
# 2025年07月16日13时02分51秒
# 2416864569@qq.com
class Node:
    def __init__(self,elem = -1, lchild = None, rchild = None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree:
    def __init__(self):
        self.root = None
        self.help_queue = []  # 辅助队列

    def level_build_tree(self, node: Node):
        if self.root is None:  # 树根为空
            self.root = node
            self.help_queue.append(node)
        else:
            self.help_queue.append(node)
            if self.help_queue[0].lchild is None:  # 如果当前的父亲左孩子是None
                self.help_queue[0].lchild = node  # 放入左孩子
            else:
                self.help_queue[0].rchild = node  # 放入右孩子
                self.help_queue.pop(0)  # 当前父亲满了，出队

    def pre_order(self,current_node: Node):
        if current_node:
            print(current_node.elem, end = ' ')
            self.pre_order(current_node.lchild)
            self.pre_order(current_node.rchild)

    def in_order(self, current_node: Node):
        if current_node:
            self.in_order(current_node.lchild)
            print(current_node.elem, end=' ')
            self.in_order(current_node.rchild)

    def post_order(self, current_node: Node):
        if current_node:
            self.post_order(current_node.lchild)
            self.post_order(current_node.rchild)

if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(1,11):
        new_node = Node(i)  # 实例化结点
        tree.level_build_tree(new_node)  # 把结点放入树中

    tree.pre_order(tree.root)
    print()

    tree.in_order(tree.root)
    print()

    tree.post_order(tree.root)
    print()