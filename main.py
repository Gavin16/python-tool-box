# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pickle
from module_A.fibo import *
import module_A.fibo


"""
pickle 模块使用: 保存/加载内存数据
"""

aaa = "python is so useful that you'd better pick it"


def test_pickle():
    print(aaa)
    test_pickle_write()
    test_pickle_read()


def test_pickle_write():
    data1 = {"a": "123", "b": "def", 123: 666}
    data2 = [1, 2, 3, 4]
    output = open('cache/data.pkl', 'wb+')
    pickle.dump(data1, output)
    pickle.dump(data2, output)
    output.close()


def test_pickle_read():
    pkl_input = open('cache/data.pkl', 'rb')
    data1 = pickle.load(pkl_input)
    data2 = pickle.load(pkl_input)
    pkl_input.close()
    print(data1)
    print(data2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_pickle()
