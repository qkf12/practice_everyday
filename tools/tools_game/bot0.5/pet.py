# -*- coding: utf-8 -*-
"""
桌宠主体 - 透明窗口、可拖拽、点击反馈、空闲浮动、缩放调节
"""
import os
import math
from PyQt5.QtWidgets import (
    QWidget, QLabel, QMenu, QAction, QApplication,
    QWidgetAction, QSlider, QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import (
    Qt, QPoint, QTimer, QPropertyAnimation,
    QEasingCurve, QRect, pyqtSignal
)
from PyQt5.QtGui import QPixmap

import config
from utils.image_utils import get_pet_pixmap, scale_pixmap, load_scale, save_scale


class ScaleSliderWidget(QWidget):
    """右键菜单中的缩放滑块控件"""

    def __init__(self, current_scale, on_change, parent=None):
        super().__init__(parent)
        self.on_change = on_change

        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(4)

        # 标题行: 标签 + 百分比
        title_row = QHBoxLayout()
        title_row.setSpacing(0)
        self.title_label = QLabel("🔍  桌宠大小")
        self.title_label.setStyleSheet(f"""
            QLabel {{
                color: {config.COLOR_TEXT_PRIMARY};
                font-size: 13px;
                font-weight: bold;
                background: transparent;
            }}
        """)
        self.percent_label = QLabel(f"{int(current_scale * 100)}%")
        self.percent_label.setStyleSheet(f"""
            QLabel {{
                color: {config.COLOR_ACCENT_ORANGE};
                font-size: 13px;
                font-weight: bold;
                background: transparent;
                font-family: 'Consolas', monospace;
            }}
        """)
        title_row.addWidget(self.title_label)
        title_row.addStretch()
        title_row.addWidget(self.percent_label)
        layout.addLayout(title_row)

        # 滑块
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(self._scale_to_value(current_scale))
        self.slider.setFixedHeight(24)
        self.slider.setStyleSheet(f"""
            QSlider::groove:horizontal {{
                height: 6px;
                background: {config.COLOR_BORDER};
                border-radius: 3px;
            }}
            QSlider::handle:horizontal {{
                width: 16px;
                height: 16px;
                margin: -5px 0;
                background: {config.COLOR_ACCENT_RED};
                border-radius: 8px;
            }}
            QSlider::handle:horizontal:hover {{
                background: {config.COLOR_ACCENT_HOVER};
            }}
            QSlider::sub-page:horizontal {{
                background: {config.COLOR_ACCENT_ORANGE};
                border-radius: 3px;
            }}
        """)
        self.slider.valueChanged.connect(self._on_slider_changed)
        layout.addWidget(self.slider)

        self.setFixedWidth(220)

    def _scale_to_value(self, scale):
        """将缩放比例转为滑块值 (0-100)"""
        ratio = (scale - config.SCALE_MIN) / (config.SCALE_MAX - config.SCALE_MIN)
        return int(max(0, min(100, ratio * 100)))

    def _value_to_scale(self, value):
        """将滑块值转为缩放比例"""
        ratio = value / 100.0
        return config.SCALE_MIN + ratio * (config.SCALE_MAX - config.SCALE_MIN)

    def _on_slider_changed(self, value):
        scale = self._value_to_scale(value)
        self.percent_label.setText(f"{int(scale * 100)}%")
        if self.on_change:
            self.on_change(scale)


class DesktopPet(QWidget):
    """桌面桌宠"""

    clicked = pyqtSignal(QPoint)

    def __init__(self):
        super().__init__()
        self._drag_pos = None
        self._is_dragging = False
        self._click_pos = None
        self._float_offset = 0
        self._float_direction = 1
        self.toolbox = None
        self.scale = load_scale()  # 加载保存的缩放比例

        self._init_window()
        self._init_pet()
        self._init_animations()
        self._init_context_menu()

    def _current_width(self):
        return int(config.PET_BASE_WIDTH * self.scale)

    def _current_height(self):
        return int(config.PET_BASE_HEIGHT * self.scale)

    def _init_window(self):
        """初始化窗口属性"""
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        w, h = self._current_width(), self._current_height()
        self.setFixedSize(w, h)

        # 默认位置: 屏幕右下角
        screen = QApplication.primaryScreen()
        if screen:
            geo = screen.availableGeometry()
            self.move(
                geo.right() - w - 40,
                geo.bottom() - h - 60
            )

    def _init_pet(self):
        """初始化桌宠图片"""
        w, h = self._current_width(), self._current_height()

        self.pet_label = QLabel(self)
        self.pet_label.setAlignment(Qt.AlignCenter)
        self.pet_label.setGeometry(0, 0, w, h)
        self.pet_label.setStyleSheet("background: transparent;")

        # 加载并缩放图片 (不抠图, 直接用裁剪后的原图)
        pixmap = get_pet_pixmap()
        if not pixmap.isNull():
            scaled = scale_pixmap(pixmap, w, h)
            self.pet_label.setPixmap(scaled)

        # 对话气泡
        self.bubble = QLabel(self)
        self.bubble.setAlignment(Qt.AlignCenter)
        self.bubble.setWordWrap(True)
        self.bubble.hide()
        self.bubble.setStyleSheet(f"""
            QLabel {{
                background-color: {config.COLOR_BG_DARK};
                color: {config.COLOR_TEXT_PRIMARY};
                border: 1px solid {config.COLOR_ACCENT_ORANGE};
                border-radius: 12px;
                padding: 8px 14px;
                font-size: 13px;
                font-family: 'Microsoft YaHei', sans-serif;
            }}
        """)

    def _init_animations(self):
        """初始化动画"""
        self.bounce_anim = QPropertyAnimation(self.pet_label, b"geometry")
        self.bounce_anim.setDuration(config.ANIM_BOUNCE_DURATION)
        self.bounce_anim.setEasingCurve(QEasingCurve.OutBack)

        self.float_timer = QTimer(self)
        self.float_timer.timeout.connect(self._float_update)
        self.float_timer.start(30)

        self.bubble_timer = QTimer(self)
        self.bubble_timer.setSingleShot(True)
        self.bubble_timer.timeout.connect(self.bubble.hide)

    def _init_context_menu(self):
        """初始化右键菜单"""
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._show_context_menu)

    def set_scale(self, scale):
        """设置桌宠缩放比例, 实时更新大小"""
        scale = max(config.SCALE_MIN, min(config.SCALE_MAX, scale))
        self.scale = scale

        w, h = self._current_width(), self._current_height()
        old_pos = self.pos()

        # 保持右下角相对位置不变 (以右下角为锚点缩放)
        screen = QApplication.primaryScreen()
        if screen:
            geo = screen.availableGeometry()
            # 计算原来的右下角位置
            old_right = old_pos.x() + self.width()
            old_bottom = old_pos.y() + self.height()
            # 新位置 = 右下角 - 新尺寸
            new_x = old_right - w
            new_y = old_bottom - h
            # 确保不超出屏幕
            new_x = max(0, min(new_x, geo.right() - w))
            new_y = max(0, min(new_y, geo.bottom() - h))
            self.move(new_x, new_y)

        self.setFixedSize(w, h)
        self.pet_label.setGeometry(0, 0, w, h)

        # 更新图片
        pixmap = get_pet_pixmap()
        if not pixmap.isNull():
            scaled = scale_pixmap(pixmap, w, h)
            self.pet_label.setPixmap(scaled)

        # 保存缩放比例
        save_scale(scale)

    def _show_context_menu(self, pos):
        """显示右键菜单 (含缩放滑块)"""
        menu = QMenu(self)
        menu.setStyleSheet(f"""
            QMenu {{
                background-color: {config.COLOR_BG_DARK};
                color: {config.COLOR_TEXT_PRIMARY};
                border: 1px solid {config.COLOR_BORDER};
                border-radius: 8px;
                padding: 4px;
                font-size: 13px;
            }}
            QMenu::item {{
                padding: 6px 20px;
                border-radius: 4px;
            }}
            QMenu::item:selected {{
                background-color: {config.COLOR_ACCENT_RED};
                color: white;
            }}
        """)

        # === 缩放滑块 (通过 QWidgetAction 嵌入) ===
        slider_widget = ScaleSliderWidget(self.scale, self.set_scale)
        slider_action = QWidgetAction(self)
        slider_action.setDefaultWidget(slider_widget)
        menu.addAction(slider_action)

        menu.addSeparator()

        # 打开工具箱
        open_toolbox = QAction("📂 打开工具箱", self)
        open_toolbox.triggered.connect(self._open_toolbox)
        menu.addAction(open_toolbox)

        # 打开笔记文件夹
        open_notes = QAction("📁 打开笔记文件夹", self)
        open_notes.triggered.connect(self._open_notes_folder)
        menu.addAction(open_notes)

        # 重置大小
        reset_size = QAction("↺ 重置大小", self)
        reset_size.triggered.connect(lambda: self.set_scale(config.SCALE_DEFAULT))
        menu.addAction(reset_size)

        menu.addSeparator()

        exit_action = QAction("❌ 退出", self)
        exit_action.triggered.connect(QApplication.instance().quit)
        menu.addAction(exit_action)

        menu.exec_(self.mapToGlobal(pos))

    def _float_update(self):
        """空闲浮动动画更新"""
        if self._is_dragging:
            return

        self._float_offset += 0.05 * self._float_direction
        if abs(self._float_offset) > 1.0:
            self._float_direction *= -1

        w, h = self._current_width(), self._current_height()
        y_offset = int(math.sin(self._float_offset) * config.ANIM_FLOAT_AMPLITUDE * self.scale)
        self.pet_label.move(0, y_offset)

    def _show_bubble(self, text, duration=2000):
        """显示对话气泡"""
        self.bubble.setText(text)
        self.bubble.adjustSize()

        w = self._current_width()
        bubble_x = (w - self.bubble.width()) // 2
        bubble_y = -self.bubble.height() - 5
        self.bubble.move(bubble_x, bubble_y)
        self.bubble.show()
        self.bubble.raise_()

        self.bubble_timer.start(duration)

    def _bounce_animation(self):
        """点击弹跳动画"""
        w, h = self._current_width(), self._current_height()
        original_geo = QRect(0, 0, w, h)
        enlarged = QRect(-10, -10, w + 20, h + 20)

        self.bounce_anim.setStartValue(enlarged)
        self.bounce_anim.setEndValue(original_geo)
        self.bounce_anim.start()

    def _open_toolbox(self):
        """打开工具箱"""
        if self.toolbox is not None and self.toolbox.isVisible():
            self.toolbox.close_animated()
            self.toolbox = None
            return

        from toolbox import ToolboxPopup
        self.toolbox = ToolboxPopup()
        self.toolbox.closed.connect(self._on_toolbox_closed)
        self.toolbox.show_at(self.pos(), pet_width=self._current_width())

    def _on_toolbox_closed(self):
        self.toolbox = None

    def _open_notes_folder(self):
        os.makedirs(config.NOTES_DIR, exist_ok=True)
        try:
            os.startfile(config.NOTES_DIR)
        except Exception:
            pass

    # === 鼠标事件 ===

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._click_pos = event.globalPos()
            self._drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            self._is_dragging = False
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self._drag_pos is not None:
            new_pos = event.globalPos() - self._drag_pos
            if (event.globalPos() - self._click_pos).manhattanLength() > 5:
                self._is_dragging = True
                self.move(new_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if not self._is_dragging:
                self._bounce_animation()
                self._show_bubble("嗯？有什么想法吗？")
                self._open_toolbox()
                self.clicked.emit(self.pos())
            self._drag_pos = None
            self._is_dragging = False
            event.accept()

    def enterEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.unsetCursor()
        super().leaveEvent(event)
