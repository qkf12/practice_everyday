import pytest

# 1. 假设这是开发写的被测函数（判断成绩等级）
def check_grade(score):
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

# 2. 测试用例设计（白盒测试里的边界值法）
@pytest.mark.parametrize("score, expected", [
    (95, "优秀"),    # 正常数据
    (90, "优秀"),    # 边界值（刚好90）
    (89, "及格"),    # 边界值（差一分）
    (60, "及格"),    # 边界值（刚好60）
    (59, "不及格"),  # 边界值（差一分）
    (0, "不及格")    # 极端数据
])
# 3. 测试函数
def test_check_grade(score, expected):
    assert check_grade(score) == expected