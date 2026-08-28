# -*- coding: utf-8 -*-
"""
软件箱 - 软件快速启动面板
桌面式图标陈列, 双击启动, 右键管理, 末尾加号添加
"""
import os
import json
import uuid
import subprocess

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame,
    QFileDialog, QMessageBox, QMenu, QAction, QScrollArea,
    QGridLayout
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap

import config
from tools.base_tool import BaseTool

# 软件列表配置保存路径
SOFTWARE_LIST_FILE = os.path.join(config.ASSETS_DIR, "software_list.json")

# 图标尺寸
ICON_SIZE = 64
ITEM_WIDTH = 96
ITEM_HEIGHT = 100
COLS = 4  # 每行图标数量


# ============================================================
# 单个软件图标项
# ============================================================
class SoftwareItem(QFrame):
    """单个软件图标: 图标 + 名称, 支持双击启动和右键菜单"""

    launched = pyqtSignal(str)        # 请求启动 exe
    edit_requested = pyqtSignal(dict)  # 请求编辑 (更改exe/图标/删除)

    # 从 exe 提取的图标缓存 (key: exe 路径小写), 避免每次刷新网格都重复提取
    _exe_icon_cache = {}

    def __init__(self, software_data, parent=None):
        super().__init__(parent)
        self.data = software_data  # {name, exe_path, icon_path}
        self.setFixedSize(ITEM_WIDTH, ITEM_HEIGHT)
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet("""
            QFrame {
                background: transparent;
                border-radius: 8px;
            }
            QFrame:hover {
                background-color: rgba(255, 255, 255, 0.08);
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(4, 6, 4, 4)
        layout.setSpacing(4)

        # 图标
        self.icon_label = QLabel()
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.icon_label.setFixedSize(ICON_SIZE, ICON_SIZE)
        self.icon_label.setStyleSheet("background: transparent;")
        self._load_icon()
        layout.addWidget(self.icon_label, alignment=Qt.AlignCenter)

        # 名称 (紧贴图标下方)
        self.name_label = QLabel(self.data.get("name", "未知"))
        self.name_label.setAlignment(Qt.AlignCenter)
        self.name_label.setWordWrap(True)
        self.name_label.setFixedWidth(ITEM_WIDTH - 8)
        self.name_label.setStyleSheet(f"""
            QLabel {{
                color: {config.COLOR_TEXT_PRIMARY};
                font-size: 11px;
                background: transparent;
                font-family: 'Microsoft YaHei', 'Segoe UI', sans-serif;
            }}
        """)
        # 调整字体大小以适应两行
        font = self.name_label.font()
        font.setPointSize(10)
        self.name_label.setFont(font)
        layout.addWidget(self.name_label)

        # 右键菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._show_context_menu)

    def _load_icon(self):
        """加载软件图标"""
        icon_path = self.data.get("icon_path")
        exe_path = self.data.get("exe_path", "")

        pixmap = None

        # 优先用自定义图标
        if icon_path and os.path.exists(icon_path):
            pixmap = QPixmap(icon_path)

        # 否则从 exe 提取图标 (带缓存)
        if pixmap is None or pixmap.isNull():
            if exe_path and os.path.exists(exe_path):
                cache_key = exe_path.lower()
                if cache_key not in self._exe_icon_cache:
                    try:
                        from PyQt5.QtWidgets import QFileIconProvider
                        from PyQt5.QtCore import QFileInfo
                        provider = QFileIconProvider()
                        icon = provider.icon(QFileInfo(exe_path))
                        self._exe_icon_cache[cache_key] = icon.pixmap(ICON_SIZE, ICON_SIZE)
                    except Exception:
                        self._exe_icon_cache[cache_key] = QPixmap()
                pixmap = self._exe_icon_cache[cache_key]

        # 都没有就用默认图标
        if pixmap is None or pixmap.isNull():
            pixmap = QPixmap(ICON_SIZE, ICON_SIZE)
            pixmap.fill(Qt.transparent)
            # 画一个默认的电脑图标
            from PyQt5.QtGui import QPainter, QBrush, QColor
            painter = QPainter(pixmap)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setBrush(QBrush(QColor("#f4a261")))
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(12, 16, 40, 28, 4, 4)
            painter.setBrush(QBrush(QColor("#e63946")))
            painter.drawRoundedRect(20, 44, 24, 6, 2, 2)
            painter.end()

        # 缩放
        scaled = pixmap.scaled(
            ICON_SIZE, ICON_SIZE,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.icon_label.setPixmap(scaled)

    def mouseDoubleClickEvent(self, event):
        """双击启动软件"""
        if event.button() == Qt.LeftButton:
            exe_path = self.data.get("exe_path", "")
            if exe_path and os.path.exists(exe_path):
                self.launched.emit(exe_path)
            else:
                QMessageBox.warning(self, "错误", "软件路径不存在，请右键重新设置。")

    def _show_context_menu(self, pos):
        """右键菜单"""
        menu = QMenu(self)
        menu.setStyleSheet(f"""
            QMenu {{
                background-color: {config.COLOR_BG_DARK};
                color: {config.COLOR_TEXT_PRIMARY};
                border: 1px solid {config.COLOR_BORDER};
                border-radius: 8px;
                padding: 4px;
                font-size: 12px;
            }}
            QMenu::item {{
                padding: 6px 16px;
                border-radius: 4px;
            }}
            QMenu::item:selected {{
                background-color: {config.COLOR_ACCENT_RED};
                color: white;
            }}
        """)

        action_open = QAction("🚀 打开", self)
        action_open.triggered.connect(lambda: self.launched.emit(self.data.get("exe_path", "")))
        menu.addAction(action_open)

        menu.addSeparator()

        action_exe = QAction("📂 更改 exe 位置", self)
        action_exe.triggered.connect(lambda: self.edit_requested.emit({"action": "change_exe", "data": self.data}))
        menu.addAction(action_exe)

        action_icon = QAction("🖼️ 更改软件图标", self)
        action_icon.triggered.connect(lambda: self.edit_requested.emit({"action": "change_icon", "data": self.data}))
        menu.addAction(action_icon)

        menu.addSeparator()

        action_delete = QAction("🗑️ 删除", self)
        action_delete.triggered.connect(lambda: self.edit_requested.emit({"action": "delete", "data": self.data}))
        menu.addAction(action_delete)

        menu.exec_(self.mapToGlobal(pos))


# ============================================================
# 添加按钮 (加号)
# ============================================================
class AddButton(QFrame):
    """末尾的加号按钮, 点击添加新软件"""

    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(ITEM_WIDTH, ITEM_HEIGHT)
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet("""
            QFrame {
                background: transparent;
                border: 2px dashed rgba(255,255,255,0.15);
                border-radius: 8px;
            }
            QFrame:hover {
                border-color: rgba(244, 162, 97, 0.6);
                background-color: rgba(244, 162, 97, 0.05);
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(4, 6, 4, 4)
        layout.setSpacing(4)

        # 加号图标
        plus = QLabel("+")
        plus.setAlignment(Qt.AlignCenter)
        plus.setFixedSize(ICON_SIZE, ICON_SIZE)
        plus.setStyleSheet(f"""
            QLabel {{
                color: {config.COLOR_TEXT_MUTED};
                font-size: 36px;
                font-weight: bold;
                background: transparent;
            }}
        """)
        layout.addWidget(plus, alignment=Qt.AlignCenter)

        # 文字
        label = QLabel("添加软件")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(f"""
            QLabel {{
                color: {config.COLOR_TEXT_MUTED};
                font-size: 10px;
                background: transparent;
            }}
        """)
        layout.addWidget(label)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()


# ============================================================
# 主工具类
# ============================================================
class OpenSoftwareTool(BaseTool):
    """文件格式转换 - 软件快速启动面板"""

    name = "软件箱"
    icon = "📦"
    tooltip = "快速启动常用软件"
    shortcut = ""

    def get_widget(self, parent=None):
        if self._widget is not None:
            return self._widget

        self.software_list = []
        self._load_list()

        widget = QWidget(parent)
        widget.setStyleSheet(f"""
            QWidget {{
                background-color: {config.COLOR_BG_CARD};
                color: {config.COLOR_TEXT_PRIMARY};
            }}
        """)

        main_layout = QVBoxLayout(widget)
        main_layout.setContentsMargins(16, 12, 16, 12)
        main_layout.setSpacing(8)

        # 标题
        title = QLabel("📦  软件箱")
        title.setStyleSheet(f"""
            QLabel {{
                color: {config.COLOR_ACCENT_ORANGE};
                font-size: 16px;
                font-weight: bold;
                background: transparent;
            }}
        """)
        main_layout.addWidget(title)

        # 提示
        tip = QLabel("双击图标启动软件 · 右键图标管理 · 点 + 添加")
        tip.setStyleSheet(f"""
            QLabel {{
                color: {config.COLOR_TEXT_MUTED};
                font-size: 11px;
                background: transparent;
            }}
        """)
        main_layout.addWidget(tip)

        # 分隔线
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet(f"background-color: {config.COLOR_BORDER}; max-height: 1px;")
        main_layout.addWidget(line)

        # 滚动区域
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setStyleSheet(f"""
            QScrollArea {{
                background: transparent;
                border: none;
            }}
            QScrollBar:vertical {{
                background: {config.COLOR_BG_DARK};
                width: 8px;
                border-radius: 4px;
            }}
            QScrollBar::handle:vertical {{
                background: {config.COLOR_BORDER};
                border-radius: 4px;
                min-height: 20px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: {config.COLOR_ACCENT_ORANGE};
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0;
            }}
        """)

        # 图标网格容器
        self.grid_container = QWidget()
        self.grid_container.setStyleSheet("background: transparent;")
        self.grid_layout = QGridLayout(self.grid_container)
        self.grid_layout.setContentsMargins(4, 8, 4, 8)
        self.grid_layout.setSpacing(8)
        self.grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        scroll.setWidget(self.grid_container)
        main_layout.addWidget(scroll, 1)

        self._widget = widget
        self._refresh_grid()
        return widget

    def on_show(self):
        self._refresh_grid()

    # === 数据持久化 ===

    def _load_list(self):
        """加载软件列表"""
        self.software_list = []
        try:
            if os.path.exists(SOFTWARE_LIST_FILE):
                with open(SOFTWARE_LIST_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self.software_list = data.get("software_list", [])
        except (OSError, json.JSONDecodeError):
            pass

        # 兼容旧数据: 为没有 id 的记录补上唯一 id, 避免同名软件编辑/删除时误匹配
        changed = False
        for sw in self.software_list:
            if not sw.get("id"):
                sw["id"] = uuid.uuid4().hex
                changed = True
        if changed:
            self._save_list()

    def _save_list(self):
        """保存软件列表"""
        try:
            os.makedirs(config.ASSETS_DIR, exist_ok=True)
            data = {"software_list": self.software_list}
            with open(SOFTWARE_LIST_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError:
            pass

    # === 界面刷新 ===

    def _clear_grid(self):
        """清空网格"""
        while self.grid_layout.count():
            item = self.grid_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def _refresh_grid(self):
        """刷新图标网格"""
        self._clear_grid()

        row, col = 0, 0
        for sw in self.software_list:
            item = SoftwareItem(sw)
            item.launched.connect(self._launch_software)
            item.edit_requested.connect(self._handle_edit)
            self.grid_layout.addWidget(item, row, col, alignment=Qt.AlignTop | Qt.AlignLeft)
            col += 1
            if col >= COLS:
                col = 0
                row += 1

        # 末尾添加加号按钮
        add_btn = AddButton()
        add_btn.clicked.connect(self._add_software)
        self.grid_layout.addWidget(add_btn, row, col, alignment=Qt.AlignTop | Qt.AlignLeft)

    # === 操作 ===

    def _launch_software(self, exe_path):
        """启动软件"""
        if not exe_path or not os.path.exists(exe_path):
            QMessageBox.warning(self._widget, "错误", "软件路径不存在，请重新设置。")
            return
        try:
            work_dir = os.path.dirname(exe_path)
            subprocess.Popen([exe_path], cwd=work_dir, shell=False)
        except Exception as e:
            QMessageBox.critical(self._widget, "启动失败", f"无法启动软件:\n{e}")

    def _add_software(self):
        """添加新软件"""
        # 选 exe
        start_dir = os.path.expanduser("~\\Desktop")
        exe_path, _ = QFileDialog.getOpenFileName(
            self._widget, "选择软件 (.exe)", start_dir,
            "可执行文件 (*.exe);;所有文件 (*.*)"
        )
        if not exe_path:
            return
        if not exe_path.lower().endswith(".exe"):
            QMessageBox.warning(self._widget, "提示", "请选择 .exe 可执行文件。")
            return

        # 从文件名提取名称
        name = os.path.splitext(os.path.basename(exe_path))[0]

        # 询问是否自定义图标
        icon_path = None
        reply = QMessageBox.question(
            self._widget, "自定义图标",
            f"已选择: {name}\n\n要自定义软件图标吗？\n(否则自动使用 exe 自带图标)",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            icon_file, _ = QFileDialog.getOpenFileName(
                self._widget, "选择图标图片",
                os.path.expanduser("~\\Desktop"),
                "图片文件 (*.png *.jpg *.jpeg *.ico *.bmp);;所有文件 (*.*)"
            )
            if icon_file:
                icon_path = icon_file

        # 添加到列表
        self.software_list.append({
            "id": uuid.uuid4().hex,
            "name": name,
            "exe_path": exe_path,
            "icon_path": icon_path
        })
        self._save_list()
        self._refresh_grid()

    def _handle_edit(self, request):
        """处理右键编辑请求"""
        action = request.get("action")
        data = request.get("data", {})

        # 优先按唯一 id 匹配
        idx = -1
        sw_id = data.get("id")
        if sw_id:
            for i, sw in enumerate(self.software_list):
                if sw.get("id") == sw_id:
                    idx = i
                    break

        # 兼容旧数据 (无 id): 按 name + exe_path 匹配
        if idx < 0:
            exe_path = data.get("exe_path", "")
            for i, sw in enumerate(self.software_list):
                if sw.get("exe_path") == exe_path and sw.get("name") == data.get("name"):
                    idx = i
                    break

        if idx < 0:
            return

        if action == "change_exe":
            self._change_exe(idx)
        elif action == "change_icon":
            self._change_icon(idx)
        elif action == "delete":
            self._delete_software(idx)

    def _change_exe(self, idx):
        """更改 exe 位置"""
        sw = self.software_list[idx]
        start_dir = os.path.dirname(sw.get("exe_path", "")) or os.path.expanduser("~\\Desktop")
        new_exe, _ = QFileDialog.getOpenFileName(
            self._widget, "重新选择软件 (.exe)", start_dir,
            "可执行文件 (*.exe);;所有文件 (*.*)"
        )
        if not new_exe or not new_exe.lower().endswith(".exe"):
            return
        sw["exe_path"] = new_exe
        # 如果名称还是原来的默认名, 同步更新
        old_name = sw.get("name", "")
        default_old = os.path.splitext(os.path.basename(sw.get("exe_path", "")))[0]
        if old_name == default_old or not old_name:
            sw["name"] = os.path.splitext(os.path.basename(new_exe))[0]
        self._save_list()
        self._refresh_grid()

    def _change_icon(self, idx):
        """更改软件图标"""
        sw = self.software_list[idx]
        start_dir = os.path.expanduser("~\\Desktop")
        icon_file, _ = QFileDialog.getOpenFileName(
            self._widget, "选择图标图片", start_dir,
            "图片文件 (*.png *.jpg *.jpeg *.ico *.bmp);;所有文件 (*.*)"
        )
        if icon_file:
            sw["icon_path"] = icon_file
        else:
            # 用户取消, 询问是否恢复默认
            if sw.get("icon_path"):
                reply = QMessageBox.question(
                    self._widget, "恢复默认",
                    "要恢复使用 exe 自带图标吗？",
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                )
                if reply == QMessageBox.Yes:
                    sw["icon_path"] = None
                else:
                    return
            else:
                return
        self._save_list()
        self._refresh_grid()

    def _delete_software(self, idx):
        """删除软件"""
        sw = self.software_list[idx]
        reply = QMessageBox.question(
            self._widget, "确认删除",
            f"确定要删除「{sw.get('name', '未知')}」吗？",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            del self.software_list[idx]
            self._save_list()
            self._refresh_grid()
