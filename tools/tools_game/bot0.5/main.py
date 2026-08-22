# -*- coding: utf-8 -*-
"""
明日香桌宠 - 主入口
运行: python main.py
"""
import sys
import os

# 将项目根目录加入 path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

import config
from pet import DesktopPet


def main():
    # 高 DPI 支持
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    app.setApplicationName("明日香桌宠")
    app.setQuitOnLastWindowClosed(False)  # 关闭工具箱不退出

    # 设置默认字体
    font = QFont("Microsoft YaHei", 10)
    app.setFont(font)

    # 创建桌宠
    pet = DesktopPet()
    pet.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
