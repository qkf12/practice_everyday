# -*- coding: utf-8 -*-
"""
工具注册表 - 在此注册所有可用工具
新增工具步骤:
  1. 在 tools/ 下新建 your_tool.py，继承 BaseTool
  2. 在下方 import 并加入 TOOL_REGISTRY 列表
"""
from tools.notepad import NotepadTool
from tools.software import OpenSoftwareTool

# === 工具注册表 ===
# 按顺序显示在工具箱侧边栏
TOOL_REGISTRY = [
    NotepadTool,
    OpenSoftwareTool,
]


def get_all_tools():
    """获取所有已注册工具的实例列表"""
    return [tool_cls() for tool_cls in TOOL_REGISTRY]


def get_tool_by_name(name):
    """根据名称获取工具类"""
    for tool_cls in TOOL_REGISTRY:
        if tool_cls.name == name:
            return tool_cls
    return None
