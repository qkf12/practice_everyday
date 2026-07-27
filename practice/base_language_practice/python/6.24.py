# 活动列表：每个活动是一个元组 (活动名称, 类别, 参与学生名单)
activities = [
    ("数学竞赛", "学科", ["张三", "李四", "王五"]),
    ("编程马拉松", "学科", ["张三", "赵六"]),
    ("篮球赛", "体育", ["李四", "王五", "赵六", "陈七"]),
    ("校运会", "体育", ["张三", "王五", "陈七"]),
    ("歌唱比赛", "艺术", ["李四", "赵六"]),
    ("画展", "艺术", ["王五", "陈七"])
]


# 计算学生得分
score = {'学科':5,'体育':3,'艺术':2}
student = {}
for activity,vary,names in activities:
    for name in names:
            student[name] = student.get(name,0)+score[vary]
print("计算学生得分")
for str_name,str_scores in student.items():
    print(f"{str_name} : {str_scores}")


# vary_list = {}
# for activity,vary,names in activities:
#     if vary not in vary_list:
#         vary_list[vary] = []  # 直接创建空列表
#     vary_list[vary].extend(names)
#
#
# print(vary_list)
vary_list = {}
for activity, vary, names in activities:
    if vary not in vary_list:
        vary_list[vary] = set()        # 初始化为空集合
    vary_list[vary].update(names)      # 把当前活动的所有学生加入集合（自动去重）

# 把集合转成列表（方便阅读）
for key in vary_list:
    vary_list[key] = list(vary_list[key])

print(vary_list)