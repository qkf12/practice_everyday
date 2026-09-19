# practice_everyday

> 每日代码练习仓库 —— 一条从 Java 基础到 Spring Boot 全栈的学习轨迹,外加两个持续迭代的自写项目。

![Java](https://img.shields.io/badge/Java-17%2B-orange)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-4.x-6DB33F)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 简介

本仓库用于记录我的编程学习历程,以「每天一个知识点、每个知识点落成一个能跑的程序」的方式推进。

主线是从 Java 基础出发,经 JDBC / MySQL 进入 Java Web,最终到 Spring Boot + MyBatis-Plus 分层开发;在此之上沉淀了两个持续迭代的自写项目。所有练习代码保持**注释即笔记**的风格,保留多版写法,方便回看思路的变化。

- **主线学习**:Java 基础 → JDBC / MySQL → Servlet / JSP → Spring Boot

- **附带沉淀**:中文学习笔记、竞赛与创业文档、开发环境资源

## 精选项目

### 一、记账本 —— 同一需求的三次架构演进

一个日常收支记账程序,用三种技术形态各实现一遍,完整体现从内存到数据库、再到前后端分离的演进过程。

| 版本 | 形态 | 数据存储 | 关键实现 |
| :--- | :--- | :--- | :--- |
| **v0.x** | 控制台程序 | `ArrayList` | 实体类封装 + `Scanner` 菜单 + 按日期增删改查 |
| **v1.0** | 控制台 + 数据库 | MySQL | JDBC `PreparedStatement` 参数化持久化,替代内存集合 |
| **v2.0** | Web 应用 | MySQL | Servlet 6.0 提供 JSON 接口 + 原生前端页面 |

**v0.x / v1.0** 位于 `practice/all_uesr/note_book` 与 `note_book1.0`,两者逻辑一一对应,后者把集合操作整体替换为 SQL 执行,重构前后的代码以注释并存,便于对照。

**v2.0** 位于 `practice/all_uesr/note_web2.0`,后端 `NoteServlet` 负责数据接口,前端为单页 HTML(深色卡片布局、按日期搜索、行内编辑、批量删除、状态提示):

| 方法 | 接口 | 说明 |
| :--- | :--- | :--- |
| `GET` | `/api/list` | 查询全部记录 |
| `POST` | `/api/add` | 新增记录 |
| `DELETE` | `/api/delete?date=` | 按日期删除 |



## 学习路径

| 阶段 | 目录 | 主要内容 | 代表性产出 |
| :--- | :--- | :--- | :--- |
| Java 基础 | `practice/base_language_practice/java` | 语法、数组、面向对象、集合、String、基础算法 | 菜品管理、数组工具类、算法练习 |
| JDBC | `practice/base_language_practice/jdbc` | 连接管理、参数化查询、结果集映射、事务 | 图书馆管理系统(终端) |
| 数据库 | `practice/MySQL_practice` | 建表与约束、多表连接、聚合分组、子查询 | 按日期归档的 SQL 练习集 |
| Python | `practice/base_language_practice/python` | 循环、字典与集合、文件读写、HTTP 请求 | 员工工资管理系统 |
| Java Web | `practice/base_language_practice/web_java` | Servlet 生命周期、会话与跳转、JSP | 文件自动归类、网页版文档编辑器 |
| Spring Boot | `practice/spring系列/spring_boot` | 配置读取、Profile 多环境、RESTful、MyBatis-Plus | 4 个渐进式子工程 |
| 工具笔记 | `practice/git_knowledge`、`practice/linux` | Git 分支与多远程推送、Linux 环境搭建 | 命令速查笔记 |

## 项目结构

```text
practice_everyday/
├── practice/                     学习练习主线
│   ├── all_uesr/                 记账本项目(v0.x / v1.0 / v2.0)
│   ├── base_language_practice/   Java · JDBC · Python · Java Web
│   ├── MySQL_practice/           SQL 练习与笔记
│   ├── spring系列/               Spring Boot 子工程
│   └── git_knowledge/ · linux/ · subject/
├── race/                         竞赛与创业文档
├── tools/                        工具资源与自写桌宠项目
│   └── tools_game/               明日香桌宠 bot0.5 / 1.0 / 1.1
└── entertainment/                建模截图与娱乐素材
```

## 技术栈

| 分类 | 使用内容 |
| :--- | :--- |
| 语言 | Java 17+、Python 3.13、SQL、JavaScript、HTML/CSS |
| 后端 | Jakarta Servlet 6.0、Spring Boot 4.x、MyBatis-Plus 3.5 |
| 数据库 | MySQL 8(Connector/J) |
| 桌面 | PyQt5 |
| 服务器 | Apache Tomcat 9.0 / 10.1 |
| 工具 | Maven、Git、IntelliJ IDEA、DBeaver |

## 快速开始

**运行 Web 版记账本**

```bash
# 1. 建库建表(代码默认使用 practice 库)
#    CREATE TABLE note (date VARCHAR(32), type VARCHAR(16), money DECIMAL(10,2));

# 2. 打包 war
cd practice/all_uesr/note_web2.0 && mvn clean package

# 3. 将 target/note_web1.war 部署到 Tomcat 10,访问
#    http://localhost:8080/note_web1/
```

> 需要 JDK 17+、Tomcat 10.x(Jakarta 命名空间)、MySQL 8;数据库账号密码在 `NoteServlet` 中修改。



**运行其他练习**:各模块互相独立,用 IDEA 打开对应目录运行入口方法即可;Spring Boot 子工程按各自 `application-dev.yml` 中的端口与访问前缀启动。



## 说明

- 仓库中的练习代码以学习为目的,部分文件保留了多个版本的注释写法。
- `practice/base_language_practice/web_java/8.4/servlet_jsp_basics-master` 为第三方 Servlet/JSP 教学示例,仅作学习参考,版权归原作者所有。
- 数据库连接等配置为本地开发环境示例,运行前请替换为自己的环境。

## License

本项目基于 [MIT License](LICENSE) 开源。

**GitHub** · <https://github.com/qkf12/practice_everyday>
**Gitee** · <https://gitee.com/qkf12/practice_everyday>



