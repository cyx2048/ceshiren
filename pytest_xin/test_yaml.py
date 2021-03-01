# coding:utf-8
import pytest,yaml

class TestData:
    @pytest.mark.parametrize(("a,b"),yaml.safe_load(open("D:\\ceshiren\\pytest_xin\\data.yaml")))
    def test_data(self,a,b):
        print(a+b)