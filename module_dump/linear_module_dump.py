"""
    线性模型持久化存储及加载

"""
from sklearn.linear_model import LinearRegression
import pickle
from sklearn.utils import _joblib


def test_module_dump():
    reg = LinearRegression()
    reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
    res = reg.predict([[4, 4]])
    print(res[0])
    _joblib.dump(reg, 'linear_reg.pkl')
    pickle.dumps(reg)


if __name__ == "__main__":
    test_module_dump()
    reg2 = _joblib.load("linear_reg.pkl")
    print(type(reg2))
    new_res = reg2.predict([[5, 5]])
    print(new_res)

