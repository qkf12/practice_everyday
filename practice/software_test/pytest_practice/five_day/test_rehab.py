import pytest

# 被测函数：电梯超载检测
def check_weight(weight):
    if weight > 1000:
        return "超载，警报！"
    elif weight < 0:
        return "重量数据错误"
    else:
        return "正常运行"

# 测试代码：参数化（顺便复习一下你之前学的）
@pytest.mark.parametrize("weight, expected", [
    (1001, "超载，警报！"),  # 边界值：刚刚超载
    (1000, "正常运行"),      # 边界值：刚好卡在超载线
    (0, "正常运行"),         # 边界值：0
    (-1, "重量数据错误"),    # 边界值：负数
    (500, "正常运行")        # 正常值
])
def test_check_weight(weight, expected):
    assert check_weight(weight) == expected



# 异常测试：测试电梯超重时，是否抛出预期的异常（假设这是被测函数的另一种写法）
def trigger_alarm(weight):
    if weight > 1000:
        raise ValueError("重量超标，触发紧急制动！")
    return "安全"

# 测试异常（用 with pytest.raises 来抓错）
def test_trigger_alarm_error():
    # 预期会抛出 ValueError，且错误信息必须包含“紧急制动”
    with pytest.raises(ValueError, match="紧急制动"):
        trigger_alarm(1200)  # 注意：这里绝对不要写 raise，只调用函数！