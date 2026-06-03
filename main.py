#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
乐鱼官网 - 主程序入口
"""
import os
import sys
import json
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class Config:
    """配置管理类"""
    DEFAULT_CONFIG = {
        "version": "1.0.0",
        "debug": False,
        "log_level": "INFO",
        "output_dir": "./output",
    }

    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.data = self._load()

    def _load(self):
        """加载配置文件"""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"配置加载失败: {e}, 使用默认配置")
        return self.DEFAULT_CONFIG.copy()

    def get(self, key, default=None):
        return self.data.get(key, default)


def main():
    """主函数"""
    config = Config()
    logger.info(f"启动 {config.get('version')}")
    logger.info(f"当前时间: {datetime.now().isoformat()}")
    output_dir = config.get("output_dir", "./output")
    os.makedirs(output_dir, exist_ok=True)
    logger.info("程序运行完成")


if __name__ == "__main__":
    main()
