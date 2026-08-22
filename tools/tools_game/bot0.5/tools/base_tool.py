# -*- coding: utf-8 -*-
"""
工具基类 - 所有工具箱工具都继承此类
新增工具只需:
  1. 继承 BaseTool
  2. 实现 name / icon / get_widget()
  3. 在 tools/__init__.py 的 TOOL_REGISTRY 中注册
"""
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal


class BaseTool:
    """工具基类，定义统一接口"""

    # 子类必须设置
    name = "未命名工具"       # 工具名称
    icon = "🔧"               # 工具图标 (emoji 或 图片路径)
    tooltip = ""              # 悬停提示
    shortcut = ""             # 快捷键 (可选)

    # 信号 (子类可使用)
    # 工具内容变化时发出，用于外部通知
    content_changed = None

    def __init__(self):
        self._widget = None

    def get_widget(self, parent=None):
        """
        返回工具的主界面 QWidget
        子类必须重写此方法
        :param parent: 父窗口
        :return: QWidget
        """
        raise NotImplementedError("子类必须实现 get_widget()")

    def on_show(self):
        """工具被选中/显示时调用，子类可重写"""
        pass

    def on_hide(self):
        """工具被取消/隐藏时调用，子类可重写"""
        pass

    def on_close(self):
        """工具箱关闭时调用，子类可重写（用于保存状态等）"""
        pass

    def refresh(self):
        """刷新工具内容，子类可重写"""
        pass
