import logging
from logging import handlers
from typing import Any

name = "yflog"

class Logger(object):
    level_relations = {
        'all': logging.NOTSET,
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(self, filename, level='debug', stream_level='info', file_level='info', filemod='a', when='D', backCount=3, fmt="%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"):
        self.stream_level = stream_level
        self.file_level = file_level
        self.filemod = filemod
        self.logger = logging.getLogger()
        format_str = logging.Formatter(fmt)
        self.logger.setLevel(self.level_relations.get(level))
        
        sh = logging.StreamHandler()
        sh.setFormatter(format_str)
        th = handlers.TimedRotatingFileHandler(
            filename=filename, when=when, backupCount=backCount, encoding='utf-8')
        th.setFormatter(format_str)

        if stream_level is not None:
            sh.setLevel(self.level_relations.get(stream_level))
        if file_level is not None:
            th.setLevel(self.level_relations.get(file_level))

        self.logger.addHandler(sh)
        self.logger.addHandler(th)

    # 修改各个日志方法，添加 stacklevel=2
    def info(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self.logger.info(msg, *args, stacklevel=2, **kwargs)

    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self.logger.debug(msg, *args, stacklevel=2, **kwargs)

    def warning(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self.logger.warning(msg, *args, stacklevel=2, **kwargs)

    def error(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self.logger.error(msg, *args, stacklevel=2, **kwargs)

    def critical(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self.logger.critical(msg, *args, stacklevel=2, **kwargs)