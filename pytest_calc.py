import pytest

from python.Calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()

    def test_add_1(self):
        # self.calc = Calc()
        result = self.calc.add(1, 2)
        print(result)
        assert 3 == result

    def test_div_1(self):
        result = self.calc.div(2, 2)
        print(result)
        assert 1 == result

    if __name__=='__main__':
        pytest.main(['-vs', 'pytest_calc.py::TestCalc::test_div_1'])
