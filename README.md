# practice_everyday

> 每日代码练习仓库 —— 一条从 Java 基础到 Spring Boot 全栈的学习轨迹,外加两个持续迭代的自写项目。

![Java](https://img.shields.io/badge/Java-17%2B-orange?logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-4.x-6DB33F?logo=springboot&logoColor=white)
![pytest](https://img.shields.io/badge/test-pytest-0A9EDC?logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

![Gitee Star](https://gitee.com/qkf12/practice_everyday/badge/star.svg?theme=dark)
![Gitee Fork](https://gitee.com/qkf12/practice_everyday/badge/fork.svg?theme=dark)
![GitHub Stars](https://img.shields.io/github/stars/qkf12/practice_everyday?style=flat&logo=github&label=GitHub%20Stars)

---

## 📖 简介

本仓库用于记录我的编程学习历程,以「每天一个知识点、每个知识点落成一个能跑的程序」的方式推进。

主线是从 Java 基础出发,经 JDBC / MySQL 进入 Java Web,再到 Spring Boot + MyBatis-Plus 分层开发;在此之上沉淀了两个持续迭代的自写项目,并补充了软件测试、前端与 Markdown 等配套练习。仓库内所有代码保持**注释即笔记**的风格,同时保留多版写法,便于回看思路变化。

- **技术覆盖**:Java · Python · SQL · HTML/CSS · JavaScript
- **自写项目**:Web 记账本、PyQt5 桌面宠物
- **学习方向**:后端开发为主,兼顾软件测试与前端基础

---

## 🔥 精选项目

### 一、记账本 —— 同一需求的三次架构演进

一个日常收支记账程序,用三种技术形态各实现一遍,完整体现从内存到数据库、再到前后端交互的演进过程。

| 版本 | 形态 | 数据存储 | 关键实现 |
| :--- | :--- | :--- | :--- |
| **v0.x** | 控制台程序 | `ArrayList` | 实体类封装 + `Scanner` 菜单 + 按日期增删改查 |
| **v1.0** | 控制台 + 数据库 | MySQL | JDBC `PreparedStatement` 参数化持久化 |
| **v2.0** | Web 应用 | MySQL | Servlet 6.0 提供 JSON 接口 + 原生前端页面 |

> 📁 `practice/all_uesr/` —— v0.x 与 v1.0 逻辑一一对应,后者把集合操作整体替换为 SQL 执行,重构前后代码以注释并存,可直接对照阅读。

**Web 版接口**

| 方法 | 接口 | 说明 |
| :--- | :--- | :--- |
| `GET` | `/api/list` | 查询全部记录 |
| `POST` | `/api/add` | 新增记录 |
| `DELETE` | `/api/delete?date=` | 按日期删除 |

前端为单页 HTML:深色卡片布局、按日期搜索、行内编辑、批量删除与状态提示栏。

### 二、明日香桌宠 —— PyQt5 桌面宠物

位于 `tools/tools_game/`,用 Python 3 + PyQt5 实现,重点在于一套**可扩展的插件式工具箱**设计。

- 🪟 无边框透明置顶窗口,支持拖拽、点击弹跳、正弦浮动动画与对话气泡
- 🎚️ 右键菜单内嵌缩放滑块(50% ~ 250%),缩放比例持久化
- 🧰 工具箱弹窗:侧边栏导航 + 内容区堆叠切换,带淡入淡出与阴影

```python
# tools/base_tool.py —— 继承 BaseTool 并在 TOOL_REGISTRY 注册即可扩展
class BaseTool:
    name = "未命名工具"
    icon = "🔧"
    def get_widget(self, parent=None): ...   # 返回工具界面
    def on_show(self): ...                   # 可选:显示时回调
    def on_close(self): ...                  # 可选:关闭时回调
```

| 内置工具 | 功能 |
| :--- | :--- |
| 📝 记事本 | 按 `notes/YYYY/MM/DD/HH_MM.txt` 自动归档,实时字数统计,可自定义保存位置 |
| 📦 软件箱 | 桌面式图标网格,双击启动程序,支持自定义图标与右键管理,数据存于 JSON |

**版本演进**

| 版本 | 变化 |
| :--- | :--- |
| `bot0.5` | 桌宠本体 + 工具箱 + 记事本(单工具) |
| `bot1.0` | 新增「软件箱」;异常落盘 `pet_error.log` 便于排查 |
| `bot1.1` | 唯一 ID、图标缓存、气泡文案随机化、动画冲突与文本超长等缺陷修复 |

---

## 🧭 学习路线

| 阶段 | 目录 | 主要内容 | 代表性产出 |
| :--- | :--- | :--- | :--- |
| Markdown | `practice/md_practice` | 标题、列表、表格、脚注、代码块、图片与 HTML 混排、预览 CSS | 4 份语法练习文档 |
| Java 基础 | `practice/base_language_practice/java` | 语法、数组、面向对象、集合、String、基础算法 | 菜品管理、数组工具类 |
| JDBC | `practice/base_language_practice/jdbc` | 连接管理、参数化查询、结果集映射、事务 | 图书馆管理系统(终端) |
| 数据库 | `practice/MySQL_practice` | 建表与约束、多表连接、聚合分组、子查询 | 按日期归档的 SQL 练习集 |
| Python | `practice/base_language_practice/python` | 循环、字典与集合、文件读写、类与对象 | 员工工资管理系统、面向对象练习 |
| 前端 | `practice/base_language_practice/html` | HTML 结构、CSS 布局与动画、Vue 2 列表渲染 | 课程导航页、祝福卡片动画 |
| Java Web | `practice/base_language_practice/java/web_java` | Servlet 生命周期、会话与跳转、JSP | 文件自动归类、网页版文档编辑器 |
| Spring Boot | `practice/spring系列/spring_boot` | 配置读取、Profile 多环境、RESTful、MyBatis-Plus | 4 个渐进式子工程 + 2 个抄写复刻项目 |
| 软件测试 | `practice/software_test` | pytest 命名规范、参数化、异常断言、覆盖率方法 | 边界值测试用例与学习总结 |
| 工具笔记 | `practice/git_knowledge`、`practice/linux` | Git 分支与多远程推送、Linux 环境搭建 | 命令速查笔记 |

<details>
<summary><b>🔍 展开:各模块具体练了什么</b></summary>

- **Java 基础**:变量与输入、分支循环、数组与随机数、方法抽取与 `static` 的区别、封装与构造器、`ArrayList` 增删改查、String API、双指针与归并类小算法。
- **JDBC**:`DriverManager` 四步流程、`Statement` 与 `PreparedStatement` 对比、防 SQL 注入、`ResultSet` 映射为 JavaBean、try-with-resources、事务提交与回滚。
- **MySQL**:数据类型与约束、条件与模糊查询、排序分页、聚合与分组、外键级联、多表连接与子查询、`CASE WHEN` 统计及格率。
- **Python**:循环图形、字典与集合统计、文件读写、`requests` 发送 HTTP 请求、类与实例属性(动态增删、`__dict__`)。
- **前端**:HTML 结构与语义化、CSS 盒子模型与渐变阴影、`@keyframes` 滑入动画、Vue 2 的 `v-for` 列表渲染与数据绑定。
- **Java Web**:Servlet 生命周期与三种数据传递(session / cookie / URL 重写)、`@WebServlet` 与 `web.xml`、JSP 指令与 EL、NIO 文件读写 + `fetch` 前后端交互。
- **Spring Boot**:`@Value` / `Environment` / `@ConfigurationProperties` 三种取值、配置优先级、Profile 多环境切换、REST 四种映射注解与三种接参方式、MyBatis-Plus 的 `BaseMapper` 与分页插件。
- **软件测试**:pytest 用例命名与运行参数(`-v` / `-s`)、`@pytest.mark.parametrize` 参数化与边界值设计、`pytest.raises` 异常断言、浮点结果用 `pytest.approx` 比较、语句/判定/条件/条件判定四种覆盖方法。

</details>

---

## 🛠 技术栈

| 分类 | 使用内容 |
| :--- | :--- |
| 语言 | Java 17+、Python 3.13、SQL、HTML/CSS、JavaScript |
| 后端 | Jakarta Servlet 6.0、Spring Boot 4.x、MyBatis-Plus 3.5 |
| 数据库 | MySQL 8(Connector/J) |
| 前端 | 原生 HTML/CSS/JS、Vue 2 |
| 测试 | pytest |
| 桌面 | PyQt5 |
| 服务器 | Apache Tomcat 9.0 / 10.1 |
| 工具 | Maven、Git、IntelliJ IDEA、PyCharm、DBeaver |

---

## 🚀 快速开始

**运行 Web 版记账本**

```bash
# 1. 建库建表(代码默认使用 practice 库)
#    CREATE TABLE note (date VARCHAR(32), type VARCHAR(16), money DECIMAL(10,2));

# 2. 打包 war
cd practice/all_uesr/note_web2.0 && mvn clean package

# 3. 将 target/note_web1.war 部署到 Tomcat 10,访问
#    http://localhost:8080/note_web1/
```

> 依赖 JDK 17+、Tomcat 10.x(Jakarta 命名空间)、MySQL 8;数据库账号密码在 `NoteServlet` 中修改。

**运行桌宠**

```bash
cd tools/tools_game/bot1.1/bot
pip install PyQt5
python main.py          # 或双击 启动桌宠.bat
```

**运行测试练习**

```bash
cd practice/software_test/pytest_practice
pytest -v               # -s 可显示测试函数内的打印输出
```

**运行其他练习**:各模块互相独立,用 IDEA / PyCharm 打开对应目录运行入口方法即可;Spring Boot 子工程按各自 `application-dev.yml` 中的端口与访问前缀启动。

---

## 🗂 项目结构

```text
practice_everyday/
├── practice/                        学习主线
│   ├── all_uesr/                    记账本项目(v0.x / v1.0 / v2.0)
│   ├── base_language_practice/      Java · JDBC · Python · 前端
│   │   ├── java/                    Java 基础(含 web_java 子目录)
│   │   ├── jdbc/                    JDBC 与图书馆管理系统
│   │   ├── python/                  基础练习与面向对象
│   │   └── html/                    HTML / CSS / Vue 练习
│   ├── MySQL_practice/              SQL 练习与笔记
│   ├── spring系列/spring_boot/      Spring Boot 子工程
│   ├── software_test/               pytest 软件测试练习
│   ├── md_practice/                 Markdown 语法练习
│   ├── git_knowledge/               Git 命令笔记
│   ├── linux/                       Linux 笔记
│   └── subject/                     英语、数学学习资料
├── race/                            竞赛与创业文档
├── tools/                           工具资源与自写桌宠项目
│   └── tools_game/                  明日香桌宠 bot0.5 / 1.0 / 1.1
├── entertainment/                   建模截图与娱乐素材
├── LICENSE                          MIT
└── README.md
```

---

## 🏆 文档与竞赛

`race/` 目录收录了技术之外的项目与竞赛材料:

- **中国软件杯全国总决赛** —— 「基于大模型技术的软件实训教学结果检查评价与报表系统」的产品说明书、演示 PPT 与决赛答辩大纲
- **智网卫士** —— 智能变电站数据交互网关项目计划书
- **创新创业** —— 老年陪伴机器人「国芯智护」商业计划书与原型
- **红色故事** —— 主题演讲稿与报送材料

---

## 📌 说明

- 仓库中的练习代码以学习为目的,部分文件保留了多个版本的注释写法,便于对照思路变化。
- `practice/base_language_practice/java/web_java/8.4/servlet_jsp_basics-master` 为第三方 Servlet/JSP 教学示例,仅作学习参考,版权归原作者所有。
- 数据库连接等配置为本地开发环境示例,运行前请替换为自己的环境。

## 📄 License

本项目基于 [MIT License](LICENSE) 开源。

---

<div align="center">

**如果这个仓库对你有帮助,欢迎点个 Star ⭐**

[GitHub](https://github.com/qkf12/practice_everyday) · [Gitee](https://gitee.com/qkf12/practice_everyday)

</div>