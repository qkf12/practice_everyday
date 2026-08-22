# -*- coding: utf-8 -*-
"""
工具箱弹窗 - 点击桌宠后弹出的精致功能窗口
支持工具切换、动画效果、可扩充
"""
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QFrame, QStackedWidget, QSizePolicy
)
from PyQt5.QtCore import (
    Qt, QPropertyAnimation, QEasingCurve, QPoint,
    QTimer, pyqtSignal
)
from PyQt5.QtGui import QFont, QPainter, QColor, QBrush, QPainterPath

import config
from tools import get_all_tools


class ToolboxPopup(QWidget):
    """工具箱弹窗"""

    closed = pyqtSignal()  # 窗口关闭信号

    def __init__(self, pet_pos=None):
        super().__init__()
        self.pet_pos = pet_pos
        self.tools = get_all_tools()
        self.current_tool_index = 0
        self.tool_buttons = []
        self._is_closing = False

        self._init_ui()
        self._init_animation()

    def _init_ui(self):
        """初始化界面"""
        # 窗口属性
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(config.TOOLBOX_WIDTH, config.TOOLBOX_HEIGHT)

        # 主容器 (用于圆角阴影效果)
        self.container = QWidget(self)
        self.container.setObjectName("container")
        self.container.setGeometry(0, 0, config.TOOLBOX_WIDTH, config.TOOLBOX_HEIGHT)
        self.container.setStyleSheet(f"""
            #container {{
                background-color: {config.COLOR_BG_DARK};
                border-radius: 16px;
                border: 1px solid {config.COLOR_BORDER};
            }}
        """)

        # 主布局
        main_layout = QHBoxLayout(self.container)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # === 左侧边栏 ===
        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(config.TOOLBOX_SIDEBAR_WIDTH)
        self.sidebar.setStyleSheet(f"""
            QFrame {{
                background-color: {config.COLOR_BG_SIDEBAR};
                border-top-left-radius: 16px;
                border-bottom-left-radius: 16px;
                border: none;
            }}
        """)

        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(8, 16, 8, 16)
        sidebar_layout.setSpacing(6)

        # 顶部 Logo / 标题
        logo = QLabel("✦")
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet(f"""
            QLabel {{
                color: {config.COLOR_ACCENT_ORANGE};
                font-size: 22px;
                background: transparent;
                padding-bottom: 8px;
            }}
        """)
        sidebar_layout.addWidget(logo)

        # 分隔线
        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setStyleSheet(f"background-color: {config.COLOR_BORDER}; max-height: 1px; margin: 0 4px;")
        sidebar_layout.addWidget(sep)

        # 工具按钮区
        self.tools_layout = QVBoxLayout()
        self.tools_layout.setSpacing(4)
        sidebar_layout.addLayout(self.tools_layout)

        sidebar_layout.addStretch()

        # 关闭按钮
        self.close_btn = QPushButton("✕")
        self.close_btn.setCursor(Qt.PointingHandCursor)
        self.close_btn.setFixedSize(40, 40)
        self.close_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                color: {config.COLOR_TEXT_SECONDARY};
                border: none;
                border-radius: 8px;
                font-size: 16px;
            }}
            QPushButton:hover {{
                background-color: {config.COLOR_ACCENT_RED};
                color: white;
            }}
        """)
        self.close_btn.clicked.connect(self.close_animated)
        sidebar_layout.addWidget(self.close_btn, alignment=Qt.AlignCenter)

        main_layout.addWidget(self.sidebar)

        # === 右侧内容区 ===
        self.content_area = QFrame()
        self.content_area.setStyleSheet(f"""
            QFrame {{
                background-color: {config.COLOR_BG_CARD};
                border-top-right-radius: 16px;
                border-bottom-right-radius: 16px;
                border: none;
            }}
        """)

        content_layout = QVBoxLayout(self.content_area)
        content_layout.setContentsMargins(0, 0, 0, 0)

        # 工具标题栏
        self.title_bar = QFrame()
        self.title_bar.setFixedHeight(44)
        self.title_bar.setStyleSheet(f"""
            QFrame {{
                background-color: {config.COLOR_BG_DARK};
                border-top-right-radius: 16px;
                border: none;
            }}
        """)
        title_layout = QHBoxLayout(self.title_bar)
        title_layout.setContentsMargins(16, 0, 16, 0)

        self.tool_title = QLabel()
        self.tool_title.setStyleSheet(f"""
            QLabel {{
                color: {config.COLOR_TEXT_PRIMARY};
                font-size: 15px;
                font-weight: bold;
                background: transparent;
            }}
        """)
        title_layout.addWidget(self.tool_title)
        title_layout.addStretch()

        content_layout.addWidget(self.title_bar)

        # 工具内容堆叠
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setStyleSheet("background: transparent; border: none;")
        content_layout.addWidget(self.stacked_widget)

        main_layout.addWidget(self.content_area, 1)

        # 加载所有工具
        self._load_tools()

    def _load_tools(self):
        """加载所有注册的工具"""
        for i, tool in enumerate(self.tools):
            # 创建工具按钮
            btn = QPushButton(tool.icon)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFixedSize(56, 56)
            btn.setToolTip(tool.name)
            btn.setProperty("tool_index", i)
            btn.setStyleSheet(self._get_tool_btn_style(i, selected=(i == 0)))
            btn.clicked.connect(lambda checked, idx=i: self.switch_tool(idx))
            self.tools_layout.addWidget(btn)
            self.tool_buttons.append(btn)

            # 创建工具 widget
            widget = tool.get_widget(self.stacked_widget)
            self.stacked_widget.addWidget(widget)

        # 默认选中第一个工具
        if self.tools:
            self.switch_tool(0)

    def _get_tool_btn_style(self, index, selected=False):
        """获取工具按钮样式"""
        if selected:
            return f"""
                QPushButton {{
                    background-color: {config.COLOR_ACCENT_RED};
                    color: white;
                    border: none;
                    border-radius: 12px;
                    font-size: 24px;
                }}
                QPushButton:hover {{
                    background-color: {config.COLOR_ACCENT_HOVER};
                }}
            """
        else:
            return f"""
                QPushButton {{
                    background-color: transparent;
                    color: {config.COLOR_TEXT_SECONDARY};
                    border: none;
                    border-radius: 12px;
                    font-size: 24px;
                }}
                QPushButton:hover {{
                    background-color: {config.COLOR_BG_CARD};
                    color: {config.COLOR_TEXT_PRIMARY};
                }}
            """

    def switch_tool(self, index):
        """切换到指定工具"""
        if index < 0 or index >= len(self.tools):
            return

        # 通知旧工具隐藏
        if 0 <= self.current_tool_index < len(self.tools):
            self.tools[self.current_tool_index].on_hide()

        self.current_tool_index = index
        self.stacked_widget.setCurrentIndex(index)

        # 更新按钮样式
        for i, btn in enumerate(self.tool_buttons):
            btn.setStyleSheet(self._get_tool_btn_style(i, selected=(i == index)))

        # 更新标题
        tool = self.tools[index]
        self.tool_title.setText(f"{tool.icon}  {tool.name}")

        # 通知新工具显示
        tool.on_show()

    def _init_animation(self):
        """初始化弹出动画"""
        # 透明度动画
        self.setWindowOpacity(0.0)
        self.fade_anim = QPropertyAnimation(self, b"windowOpacity")
        self.fade_anim.setDuration(config.ANIM_POPUP_DURATION)
        self.fade_anim.setStartValue(0.0)
        self.fade_anim.setEndValue(1.0)
        self.fade_anim.setEasingCurve(QEasingCurve.OutCubic)

    def show_at(self, pos, pet_width=None):
        """在指定位置附近显示工具箱
        :param pos: 桌宠位置
        :param pet_width: 桌宠实际宽度 (缩放后), 不传则用基准宽度
        """
        if pet_width is None:
            pet_width = config.PET_BASE_WIDTH

        # 计算位置: 显示在桌宠右侧 (如果空间不够则左侧)
        screen = self.screen()
        if screen:
            screen_geo = screen.availableGeometry()
        else:
            screen_geo = self.frameGeometry()

        x = pos.x() + pet_width + 10
        y = pos.y()

        # 如果右侧空间不够，显示在左侧
        if x + config.TOOLBOX_WIDTH > screen_geo.right():
            x = pos.x() - config.TOOLBOX_WIDTH - 10

        # 垂直方向确保不超出屏幕
        if y + config.TOOLBOX_HEIGHT > screen_geo.bottom():
            y = screen_geo.bottom() - config.TOOLBOX_HEIGHT
        if y < screen_geo.top():
            y = screen_geo.top()

        self.move(x, y)
        self.show()
        self.raise_()
        self.activateWindow()

        # 播放弹出动画
        self.setWindowOpacity(0.0)
        self.fade_anim.start()

    def close_animated(self):
        """带动画关闭"""
        if self._is_closing:
            return
        self._is_closing = True

        # 通知所有工具关闭
        for tool in self.tools:
            tool.on_close()

        # 淡出动画
        self.fade_anim.setStartValue(1.0)
        self.fade_anim.setEndValue(0.0)
        self.fade_anim.finished.connect(self._do_close)
        self.fade_anim.start()

    def _do_close(self):
        self._is_closing = False
        self.closed.emit()
        self.close()

    def keyPressEvent(self, event):
        """ESC 关闭"""
        if event.key() == Qt.Key_Escape:
            self.close_animated()
        else:
            super().keyPressEvent(event)

    def paintEvent(self, event):
        """绘制阴影效果"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制窗口阴影
        shadow_color = QColor(0, 0, 0, 40)
        painter.setBrush(QBrush(shadow_color))
        painter.setPen(Qt.NoPen)

        # 阴影偏移
        offset = 6
        path = QPainterPath()
        path.addRoundedRect(
            offset, offset,
            config.TOOLBOX_WIDTH - offset * 2,
            config.TOOLBOX_HEIGHT - offset * 2,
            16, 16
        )
        painter.drawPath(path)

        super().paintEvent(event)
