import logging
from logging import handlers
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
        # init a logger
        self.stream_level = stream_level
        self.file_level = file_level
        self.filemod=filemod
        self.logger = logging.getLogger()
        # set the format
        format_str = logging.Formatter(fmt)
        # judge the level
        self.logger.setLevel(self.level_relations.get(level))
        sh = logging.StreamHandler()  
        sh.setFormatter(format_str)
        th = handlers.TimedRotatingFileHandler(
            filename=filename, when=when, backupCount=backCount, encoding='utf-8')  #
        th.setFormatter(format_str) 
        

        if stream_level != None:
            if stream_level not in self.level_relations:
                assert "The steam level is wrong."
            sh.setLevel(self.level_relations.get(stream_level))
        if file_level != None:
            if file_level not in self.level_relations:
                assert "The steam level is wrong."
            th.setLevel(self.level_relations.get(file_level))

        self.logger.addHandler(sh) 
        self.logger.addHandler(th)

        print(self.logger)

    # begin func
    def info(self, msg, *args):
        return self.logger.info(msg, *args)

    def debug(self, msg, *args):
        return self.logger.debug(msg, *args)

    def warning(self, msg, *args):
        return self.logger.warning(msg, *args)

    def error(self, msg, *args):
        return self.logger.error(msg, *args)

    def critical(self, msg, *args):
        return self.logger.critical(msg, *args)