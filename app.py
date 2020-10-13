import logging.handlers
import os


def log_conf():
    """日志初始化"""
    # 日志文件位置
    logpath = './Log'
    # 日志器
    logger = logging.getLogger()
    # 设置日志器的级别
    logger.setLevel(logging.INFO)
    # 处理器 -控制台
    sh = logging.StreamHandler()
    # 处理器 -文件
    trfh = logging.handlers.TimedRotatingFileHandler(filename=logpath
                                                              + os.sep + 'mini.log', when='midnight',
                                                     interval=1, backupCount=7, encoding='utf-8')
    # 格式化字符串
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    # 格式化器
    formatter = logging.Formatter(fmt)
    # 处理器添加格式化器
    sh.setFormatter(formatter)
    trfh.setFormatter(formatter)
    # 日志器添加处理器
    logger.addHandler(sh)
    logger.addHandler(trfh)


# 请求通用接口地址
base_url = "http://e.cn/api/v1"

# 微信code
code = "0718Ik200EMruK14P3200UueyP18Ik2V"

# 请求头
headers = {
    "Content-Type": "application/json",
    "token": "0725f323117fd6b302c9f651ecd86225"
}
