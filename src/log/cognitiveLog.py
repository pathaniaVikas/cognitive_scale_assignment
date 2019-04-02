import sys
import os
import logging

class Log():
    def __init__(self, cllog):
        self.cllog = cllog

    def fmt_args(self, fmt, args):
        if not isinstance(fmt, basestring):
            fmt = repr(fmt)
        args_list = []
        for arg in args:
            try:
                str(arg)
                args_list.append(arg)
            except Exception as fault:
                args_list.append(repr(arg))
        args = tuple(args_list)
        return fmt, args

    def error(self, fmt, *args):
        fmt, args = self.fmt_args(fmt, args)
        self.cllog.error(fmt % args)

    def info(self, fmt, *args):
        fmt, args = self.fmt_args(fmt, args)
        self.cllog.info(fmt % args)

    def debug(self, fmt, *args):
        fmt, args = self.fmt_args(fmt, args)
        self.cllog.debug(fmt % args)

    def warn(self, fmt, *args):
        fmt, args = self.fmt_args(fmt, args)
        self.cllog.warn(fmt % args)

    def traceback(self, fault):
        import traceback
        msg = "Error %s:%s. Traceback -" % (str(fault.__class__), str(fault))
        msg += "".join(traceback.format_exception(*sys.exc_info()))
        self.cllog.error("%s", msg)

def get_cllog_logger():
    """ provides a file logger for cllog """
    log_dir = 'logs'

    logger = logging.getLogger('cllog')
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(os.path.join(log_dir, "cllog.log"), mode='w')
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)-8s] %(message)s', datefmt='%d-%m-%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

if __name__ == '__main__':
    __builtins__.Cllog = Log(get_cllog_logger())
