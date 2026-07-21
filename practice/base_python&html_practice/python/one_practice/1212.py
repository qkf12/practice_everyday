# with open("wen.txt",'w',encoding='utf-8') as f:
#     f.write(f"你是一个2b")


employees = [
    {"id": "E01", "name": "张三", "base": 5000, "sales": 12000, "dept": "销售部"},
    {"id": "E02", "name": "李四", "base": 4500, "sales": 8000,  "dept": "销售部"},
    {"id": "E03", "name": "王五", "base": 6000, "sales": 5000,  "dept": "技术部"},
    {"id": "E04", "name": "赵六", "base": 5500, "sales": 2000,  "dept": "行政部"},
    {"id": "E05", "name": "陈七", "base": 4800, "sales": 15000, "dept": "销售部"}
]
WEN = "wen.txt"

def nene_list():
    global employees
    with open(WEN,'r', encoding="utf-8") as f:
        new_list = []
        for line in f:
            line = line.strip()
            if line:
                lines = line.split()
                if len(lines) == 5:
                    eid, name, base, sales, dept = lines
                    lines = {'id':eid,'name':name, 'base':base, 'sales': sales, 'dept':dept}

                    new_list.append(lines)
        if new_list:
            employees = new_list
            print('数据加载成功')

def one_list():
            for employee in employees:
                print(
                    f"{employee['id']:^8}{employee['name']:^8}{employee['base']:^8}{employee['sales']:^8}{employee['dept']:^8}\n")




def zero_list():

    with open(WEN,'w', encoding="utf-8") as f:
        for employee in employees:
            f.write(f"{employee['id']:^8}{employee['name']:^8}{employee['base']:^8}{employee['sales']:^8}{employee['dept']:^8}\n")


def two_list():
    global employees

    while True:
        add_employees = {}
        add_employees['id'] = input("请输入员工id")
        add_employees['name'] = input("请输入员工姓名")
        add_employees['base'] = int(input("请输入员工基础工资"))
        add_employees['sales'] = int(input("请输入员工销售额"))
        add_employees['dept'] = input("请输入员工所在部门")
        trip = input("!!!您还要再添加一个员工吗？是/1·，否/2")
        employees.append(add_employees)
        if trip == '1':
            print("录入成功")

        elif trip == '2':
            break

def three_list():
    global employees
    j = input("请输入你要删除的员工id")
    for i, employee in enumerate(employees):
        if employee['id'] == j:
           employees.pop(i)


def four_list():
    global employees
    ert = {}
    for rty in employees:
        d = rty['dept']
        f = rty['sales']
        if d in ert:
            ert[d] = ert[d] + f
        else:
            ert[d] = f
    for k, v in ert.items():
        print("===销售额=====")
        print(f"{k:^8}{v:^8}")

while True:
    print("""
    ===== 员工工资管理系统 =====
    9. 导入员工信息
    1. 查看全部员工
    2. 添加新员工
    3. 删除老员工
    4. 部门绩效统计
    5. 查找销冠
    6. 调整基本工资
    0. 退出并保存
    """)
    choose = int(input("请选择你要的功能；"))
    if choose == 1:
        one_list()
    elif choose == 2:
        two_list()
    elif choose == 3:
        three_list()
    elif choose == 4:
        four_list()
    elif choose == 0:
        zero_list()
    elif choose == 9:
        nene_list()



