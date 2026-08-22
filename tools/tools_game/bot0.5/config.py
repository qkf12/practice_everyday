# -*- coding: utf-8 -*-
"""
明日香桌宠 - 全局配置
"""
import os

# === 路径 ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
NOTES_DIR = os.path.join(BASE_DIR, "notes")
PET_IMAGE = os.path.join(BASE_DIR, "20191004171431_tloju.jpg")  # 原始参考图
PET_IMAGE_CACHE = os.path.join(ASSETS_DIR, "asuka_pet.png")       # 裁剪后缓存
SCALE_CONFIG_FILE = os.path.join(BASE_DIR, "assets", "scale.json") # 缩放比例保存

# === 桌宠尺寸 (基准尺寸, 实际显示 = 基准 * scale) ===
PET_BASE_WIDTH = 200
PET_BASE_HEIGHT = 240
PET_WIDTH = PET_BASE_WIDTH
PET_HEIGHT = PET_BASE_HEIGHT

# === 缩放范围 ===
SCALE_MIN = 0.5    # 最小 50%
SCALE_MAX = 2.5    # 最大 250%
SCALE_DEFAULT = 1.0
SCALE_STEP = 0.05  # 滑块步长

# === 工具箱尺寸 ===
TOOLBOX_WIDTH = 520
TOOLBOX_HEIGHT = 420
TOOLBOX_SIDEBAR_WIDTH = 72

# === 颜色主题 (明日香配色: 红+橙+深灰) ===
COLOR_BG_DARK = "#1a1a2e"
COLOR_BG_CARD = "#16213e"
COLOR_BG_SIDEBAR = "#0f0f1e"
COLOR_ACCENT_RED = "#e63946"
COLOR_ACCENT_ORANGE = "#f4a261"
COLOR_ACCENT_HOVER = "#ff6b6b"
COLOR_TEXT_PRIMARY = "#e8e8e8"
COLOR_TEXT_SECONDARY = "#a0a0b0"
COLOR_TEXT_MUTED = "#6c6c80"
COLOR_BORDER = "#2a2a40"
COLOR_INPUT_BG = "#0d0d1a"
COLOR_SUCCESS = "#2ecc71"

# === 动画 ===
ANIM_BOUNCE_DURATION = 300   # ms
ANIM_POPUP_DURATION = 250     # ms
ANIM_FLOAT_AMPLITUDE = 4      # px 浮动幅度
ANIM_FLOAT_SPEED = 1500       # ms 浮动周期

# === 记事本 ===
NOTEPAD_MAX_CHARS = 5000
NOTEPAD_PLACEHOLDER = "此刻在想什么？写下来吧…"
