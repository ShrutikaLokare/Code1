import inspect
import logging


class baseClass:
    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)  # to get the filename on the report

        fileHandler = logging.FileHandler("logFile.log")  # derived from parent logging
        logger.addHandler(fileHandler)  # fileHandler object

        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # to print al the detailed info on the report
        fileHandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        return logger
