# -*- coding: utf-8 -*-
"""
图像处理工具 - 直接裁剪原图使用 (不抠图)
"""
import os
import json
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt

import config


def crop_pet_image(image_path):
    """
    直接裁剪原图为合适的竖版比例 (不抠图, 保留原始背景)
    :param image_path: 原图路径
    :return: QImage
    """
    img = QImage(image_path)
    if img.isNull():
        return None

    width = img.width()
    height = img.height()

    # 原图是正方形, 角色集中在上半部分, 裁掉底部多余空白
    # 保留顶部和左右全部, 底部裁掉 12% 使比例更接近竖版
    crop_bottom = int(height * 0.12)
    new_height = height - crop_bottom

    cropped = img.copy(0, 0, width, new_height)
    return cropped


def get_pet_pixmap():
    """
    获取桌宠图片 (直接裁剪原图, 不抠图)
    :return: QPixmap
    """
    # 尝试读缓存
    if os.path.exists(config.PET_IMAGE_CACHE):
        pixmap = QPixmap(config.PET_IMAGE_CACHE)
        if not pixmap.isNull():
            return pixmap

    # 裁剪原图
    img = crop_pet_image(config.PET_IMAGE)
    if img is None:
        return QPixmap()

    # 保存缓存
    os.makedirs(config.ASSETS_DIR, exist_ok=True)
    img.save(config.PET_IMAGE_CACHE, "PNG")

    return QPixmap.fromImage(img)


def scale_pixmap(pixmap, width, height):
    """按比例缩放图片，保持宽高比"""
    if pixmap.isNull():
        return pixmap
    return pixmap.scaled(
        width, height,
        Qt.KeepAspectRatio,
        Qt.SmoothTransformation
    )


# === 缩放比例持久化 ===

def load_scale():
    """读取保存的缩放比例, 不存在则返回默认值"""
    try:
        if os.path.exists(config.SCALE_CONFIG_FILE):
            with open(config.SCALE_CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            scale = float(data.get("scale", config.SCALE_DEFAULT))
            return max(config.SCALE_MIN, min(config.SCALE_MAX, scale))
    except (OSError, ValueError, json.JSONDecodeError):
        pass
    return config.SCALE_DEFAULT


def save_scale(scale):
    """保存缩放比例到文件"""
    try:
        os.makedirs(os.path.dirname(config.SCALE_CONFIG_FILE), exist_ok=True)
        with open(config.SCALE_CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump({"scale": scale}, f, ensure_ascii=False, indent=2)
    except OSError:
        pass
