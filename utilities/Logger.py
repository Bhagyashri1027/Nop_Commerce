import logging
import inspect

class LoggenClass:
    @staticmethod
    def log_generator():
        log_name = inspect.stack()[1][3]  # it shows at runtime - the file path,class name and method name
        logger = logging.getLogger(log_name) # generate log
        logfile = logging.FileHandler("D:\\Python Automation Practicals\\Pytest Practicals\\nopCommerce_Testing\\Logs\\Nop_com_Logs.log") # log file
        log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(lineno)s -%(message)s") # log format
        logfile.setFormatter(log_format) # setting the format for logs
        logger.addHandler(logfile) # adding log every time to the same file
        logger.setLevel(logging.INFO) # set log level

        return logger