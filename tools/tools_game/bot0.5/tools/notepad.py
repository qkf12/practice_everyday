# -*- coding: utf-8 -*-
"""
记事本工具 - 记录当下想法，自动按年月日建文件夹、时分命名txt
"""
import os
from datetime import datetime

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTextEdit,
    QPushButton, QLabel, QFrame, QMessageBox
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QColor, QPalette

import config
from tools.base_tool import BaseTool


class NotepadTool(BaseTool):
    """记事本工具"""

    name = "记事本"
    icon = "📝"
    tooltip = "记录此刻的想法"
    shortcut = "Ctrl+N"

    def get_widget(self, parent=None):
        if self._widget is not None:
            return self._widget

        widget = QWidget(parent)
        widget.setStyleSheet(f"""
            QWidget {{
                background-color: {config.COLOR_BG_CARD};
                color: {config.COLOR_TEXT_PRIMARY};
            }}
        """)

        layout = QVBoxLayout(widget)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(12)

        # === 顶部标题栏 ===
        header = QHBoxLayout()
        title_label = QLabel("📝  随想记事本")
        title_label.setStyleSheet(f"""
            QLabel {{
                color: {config.COLOR_ACCENT_ORANGE};
                font-size: 18px;
                font-weight: bold;
                background: transparent;
            }}
        """)
        header.addWidget(title_label)
        header.addStretch()

        # 时间显示
        self.time_label = QLabel()
        self.time_label.setStyleSheet(f"""
            QLabel {{
                color: {config.COLOR_TEXT_SECONDARY};
                font-size: 12px;
                background: transparent;
                font-family: 'Consolas', 'Courier New', monospace;
            }}
        """)
        header.addWidget(self.time_label)
        layout.addLayout(header)

        # 分隔线
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet(f"background-color: {config.COLOR_BORDER}; max-height: 1px;")
        layout.addWidget(line)

        # === 文本编辑区 ===
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText(config.NOTEPAD_PLACEHOLDER)
        self.text_edit.setMaximumHeight(220)
        self.text_edit.setStyleSheet(f"""
            QTextEdit {{
                background-color: {config.COLOR_INPUT_BG};
                color: {config.COLOR_TEXT_PRIMARY};
                border: 1px solid {config.COLOR_BORDER};
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
                font-family: 'Microsoft YaHei', 'Segoe UI', sans-serif;
                selection-background-color: {config.COLOR_ACCENT_RED};
            }}
            QTextEdit:focus {{
                border: 1px solid {config.COLOR_ACCENT_ORANGE};
            }}
        """)
        self.text_edit.textChanged.connect(self._update_char_count)
        layout.addWidget(self.text_edit)

        # === 底部状态栏 ===
        bottom = QHBoxLayout()

        # 保存路径提示
        self.path_label = QLabel()
        self.path_label.setStyleSheet(f"""
            QLabel {{
                color: {config.COLOR_TEXT_MUTED};
                font-size: 11px;
                background: transparent;
                font-family: 'Consolas', 'Courier New', monospace;
            }}
        """)
        self.path_label.setWordWrap(True)
        bottom.addWidget(self.path_label, 1)

        # 字数统计
        self.char_label = QLabel("0 字")
        self.char_label.setStyleSheet(f"""
            QLabel {{
                color: {config.COLOR_TEXT_SECONDARY};
                font-size: 12px;
                background: transparent;
                padding: 2px 8px;
                border-radius: 4px;
                background-color: {config.COLOR_BG_DARK};
            }}
        """)
        bottom.addWidget(self.char_label)

        layout.addLayout(bottom)

        # === 保存按钮 ===
        self.save_btn = QPushButton("💾  保存想法")
        self.save_btn.setCursor(Qt.PointingHandCursor)
        self.save_btn.setFixedHeight(40)
        self.save_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {config.COLOR_ACCENT_RED};
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
                padding: 0 20px;
            }}
            QPushButton:hover {{
                background-color: {config.COLOR_ACCENT_HOVER};
            }}
            QPushButton:pressed {{
                background-color: #c62828;
            }}
            QPushButton:disabled {{
                background-color: {config.COLOR_BORDER};
                color: {config.COLOR_TEXT_MUTED};
            }}
        """)
        self.save_btn.clicked.connect(self._save_note)
        layout.addWidget(self.save_btn)

        # 保存成功提示
        self.success_label = QLabel("")
        self.success_label.setAlignment(Qt.AlignCenter)
        self.success_label.setStyleSheet(f"""
            QLabel {{
                color: {config.COLOR_SUCCESS};
                font-size: 12px;
                background: transparent;
                font-weight: bold;
            }}
        """)
        layout.addWidget(self.success_label)

        self._widget = widget
        self._refresh_time()
        return widget

    def on_show(self):
        """显示时刷新时间和路径"""
        self._refresh_time()
        self.text_edit.setFocus()

    def _refresh_time(self):
        """刷新时间显示和保存路径"""
        now = datetime.now()
        self.time_label.setText(now.strftime("%Y-%m-%d  %H:%M:%S"))
        # 显示将保存到的路径
        rel_path = os.path.join(
            "notes",
            now.strftime("%Y"),
            now.strftime("%m"),
            now.strftime("%d"),
            now.strftime("%H_%M") + ".txt"
        )
        self.path_label.setText(f"📂 {rel_path}")

    def _update_char_count(self):
        """更新字数统计"""
        count = len(self.text_edit.toPlainText())
        self.char_label.setText(f"{count} 字")
        # 超过最大字数限制
        if count > config.NOTEPAD_MAX_CHARS:
            self.char_label.setStyleSheet(f"""
                QLabel {{
                    color: {config.COLOR_ACCENT_RED};
                    font-size: 12px;
                    background: transparent;
                    padding: 2px 8px;
                    border-radius: 4px;
                    background-color: {config.COLOR_BG_DARK};
                }}
            """)
        else:
            self.char_label.setStyleSheet(f"""
                QLabel {{
                    color: {config.COLOR_TEXT_SECONDARY};
                    font-size: 12px;
                    background: transparent;
                    padding: 2px 8px;
                    border-radius: 4px;
                    background-color: {config.COLOR_BG_DARK};
                }}
            """)

    def _save_note(self):
        """保存笔记到文件"""
        content = self.text_edit.toPlainText().strip()
        if not content:
            self._show_message("内容不能为空哦~", is_error=True)
            return

        now = datetime.now()
        # 构建目录: notes/YYYY/MM/DD/
        year_dir = os.path.join(config.NOTES_DIR, now.strftime("%Y"))
        month_dir = os.path.join(year_dir, now.strftime("%m"))
        day_dir = os.path.join(month_dir, now.strftime("%d"))

        try:
            os.makedirs(day_dir, exist_ok=True)
        except OSError as e:
            self._show_message(f"创建文件夹失败: {e}", is_error=True)
            return

        # 文件名: HH_MM.txt
        filename = now.strftime("%H_%M") + ".txt"
        filepath = os.path.join(day_dir, filename)

        # 如果同一分钟内已有文件，追加秒数区分
        if os.path.exists(filepath):
            filename = now.strftime("%H_%M_%S") + ".txt"
            filepath = os.path.join(day_dir, filename)

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                # 写入带时间头的内容
                header = f"# {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                f.write(header + content + "\n")
        except OSError as e:
            self._show_message(f"保存失败: {e}", is_error=True)
            return

        # 成功反馈
        rel_path = os.path.relpath(filepath, config.BASE_DIR)
        self._show_message(f"✅ 已保存到 {rel_path}", is_error=False)
        self.text_edit.clear()
        self._refresh_time()

    def _show_message(self, text, is_error=False):
        """显示提示消息，3秒后自动消失"""
        color = config.COLOR_ACCENT_RED if is_error else config.COLOR_SUCCESS
        self.success_label.setStyleSheet(f"""
            QLabel {{
                color: {color};
                font-size: 12px;
                background: transparent;
                font-weight: bold;
            }}
        """)
        self.success_label.setText(text)
        QTimer.singleShot(3000, lambda: self.success_label.setText(""))
