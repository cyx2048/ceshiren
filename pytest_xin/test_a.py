# coding:utf-8
import pytest
def func(x):
    return x + 1
#参数
@pytest.mark.parametrize("a,b",[
    (1,2),
    (10,20)
])
def test_answer(a,b):
    assert func(4) == 5

def test_answer1():
    assert func(5) == 5

#pytest装饰器
@pytest.fixture()
def login():
    print("登录操作")
    username = 'xiaoming'
    return username

class TestDemo:
    def test_a(self,login):
        print(f"a登录操作 username = {login}")

    def test_b(self):
        print("b不需要登录操作")

# if __name__=='__main__':
#     pytest.main(['test_a.py','-v'])