import os
import sys
import logging
import functools
from datetime import datetime


# 用于记录已经初始化的 logger
logger_initialized = {}


@functools.lru_cache()
def get_logger(name="myManim", log_file=None, log_level=logging.DEBUG):
    """
    初始化并获取一个 logger。
    如果 logger 未初始化，则会为其添加一个或多个 handler；否则直接返回已初始化的 logger。
    
    Args:
        name (str): Logger 的名称。
        log_file (str | None): 日志文件的路径。如果指定，会添加一个 FileHandler。
        log_level (int): 日志级别。
    
    Returns:
        logging.Logger: 初始化后的 logger。
    """
    logger = logging.getLogger(name)
    if name in logger_initialized:
        return logger
    
    # 避免重复初始化同名 logger
    for logger_name in logger_initialized:
        if name.startswith(logger_name):
            return logger

    # 设置日志格式
    formatter = logging.Formatter(
        "[%(asctime)s] %(name)s %(levelname)s: %(message)s", 
        datefmt="%Y/%m/%d %H:%M:%S"
    )

    # 添加控制台 handler
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # 添加文件 handler（如果指定了 log_file）
    if log_file is not None:
        log_file_folder = os.path.split(log_file)[0]
        os.makedirs(log_file_folder, exist_ok=True)  # 确保日志目录存在
        
        # 显式指定文件编码为 utf-8
        file_handler = logging.FileHandler(log_file, "a", encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # 设置日志级别
    logger.setLevel(log_level)
    logger_initialized[name] = True
    logger.propagate = False  # 防止日志传递给父 logger

    return logger

def log_scene():
    """
    场景日志装饰器：用于记录场景的开始、结束和运行时间。这里写的有点乱，以后有机会再改一下。
    """
    def decorator(scene_func):
        @functools.wraps(scene_func)
        def wrapper(self, *args, **kwargs):
            # 日志文件路径
            current_dir = os.path.dirname(os.path.abspath(__file__))
            logs_dir=os.path.join(os.path.dirname(current_dir), "logs")

            log_file = os.path.join(logs_dir, f"{self.__class__.__name__}.log")
            logger = get_logger(name=self.__class__.__name__, log_file=log_file)

            # 记录开始时间
            start_time = datetime.now()
            logger.info("Start.")

            # 调用原始的 construct 方法
            try:
                result = scene_func(self, *args, **kwargs)
            except Exception as e:
                logger.error(f"{type(e).__name__}: {e}")
                raise e

            # 记录结束时间和总耗时
            end_time = datetime.now()
            logger.info("End.")
            logger.info(f"Total time taken: {end_time - start_time}")

            return result
        return wrapper
    return decorator


if __name__ == "__main__":
    pass