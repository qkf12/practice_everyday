clubs = ["围棋社", "街舞社", "摄影社", "篮球社", "吉他社"]

# 每个社团的成员名单（字典：键是社团名，值是成员姓名列表）
members = {
    "围棋社": ["张伟", "李娜", "王磊"],
    "街舞社": ["李娜", "刘洋", "陈静", "周涛"],
    "摄影社": ["王磊", "陈静", "吴迪"],
    "篮球社": ["张伟", "刘洋", "周涛"],
    "吉他社": ["陈静", "吴迪"]
}

all_list_student = set(members[clubs[0]])
for  club  in    clubs[1:]:
     all_list_student = all_list_student & set(members[club])
print("参加了全部社团的学生：", list(all_list_student) if all_list_student else "无")

student_fen  ={}
for  i,j in  members.items():
    for  b in  j :
        student_fen[b]  =  student_fen.get(b,0)+1
print(student_fen)



print("="*30, "任务 5：反向字典（学生 -> 社团列表）", "="*30)
# 翻转字典
student_to_clubs = {}
for club, students in members.items():
    for name in students:
        # 如果学生还没有记录，则创建空列表
        if name not in student_to_clubs:
            student_to_clubs[name] = []
        student_to_clubs[name].append(club)

print("学生加入的社团（反向字典）：")
for name, club_list in student_to_clubs.items():
    print(f"  {name}：{club_list}")