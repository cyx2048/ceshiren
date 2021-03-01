# coding:utf-8
import pytest,yaml

class TestDemo:
    @pytest.mark.parametrize("env",yaml.safe_load(open("D:\\ceshiren\\pytest_xin\\env.yaml")))
    def test_demo(self,env):
        if "test" in env:
            print("这是测试环境")
            print(f"测试环境的ip是",env["test"])
        elif "dev" in env:
            print("这是开发环境")
            print(f"开发环境的ip是", env["dev"])