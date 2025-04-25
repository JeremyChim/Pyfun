# Project : 魔术方法
# Author : Jeremy
# GitHub : https://github.com/JeremyChim/Pyfun
# Time : 2025.04.25

ls = [1, '2', 3]
ls2 = [4, 5, 6, 7, 8]
ls3 = ls + ls2
print(f'list add : {ls3}')


class Nlist:
    list_num = 0  # 计数器

    def __init__(self, xlist: list):
        Nlist.list_num += 1

        # 有字符串就转int或者float
        nlist = []
        for i in xlist:
            if type(i) is str:
                if '.' in i:
                    nlist.append(float(i))
                else:
                    nlist.append(int(i))
            else:
                nlist.append(i)

        self.nlist = nlist
        self.nlist_index = Nlist.list_num

    def __add__(self, other):
        """定义加法：两表元素相加"""
        alist = []
        long = max(len(self.nlist), len(other.nlist))  # 去两个列表长的长度
        for i in range(long):
            x = self.nlist[i] if i < len(self.nlist) else 0  # 超过表长度取0
            y = other.nlist[i] if i < len(other.nlist) else 0
            new_content = x + y
            alist.append(new_content)
        return alist

    def __str__(self):
        """重写打印：输出类索引和数量，表长度，表内容"""
        return (f'Nlist Index : {self.nlist_index} / {Nlist.list_num} , '
                f'Nlist Len : {len(self.nlist)} , Nlist Content : {self.nlist}')

    def __len__(self):
        """定义len函数输出"""
        return len(self.nlist)

    def __call__(self, num):
        """像调用函数一样的调用实例"""
        self.nlist.append(num)


if __name__ == '__main__':
    nls1 = Nlist([1, '2.0', 3.5])
    nls2 = Nlist([4, 5, 6, 7, 8])
    nls3 = nls1 + nls2

    print(f'Nlist add : {nls3}')
    print(f'Nlist num : {Nlist.list_num}')
    print(nls1)
    print(nls2)

    nls2(9)
    print(nls2)
    nls4 = nls1 + nls2
    print(f'Nlist add : {nls4}')
