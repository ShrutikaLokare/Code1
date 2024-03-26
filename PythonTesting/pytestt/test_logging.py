import logging  # manadatory import for log reports


def test_logging():
    logger = logging.getLogger(__name__)  # to get the filename on the report

    fileHandler = logging.FileHandler("logFile.log")  # derived from parent logging
    logger.addHandler(fileHandler)  # fileHandler object

    formatter = logging.Formatter(
        "%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # to print al the detailed info on the report
    fileHandler.setFormatter(formatter)

    logger.setLevel(logging.CRITICAL)
    logger.debug("A debug statement is created")

    logger.info("Information is created")

    logger.warning("Something is in warning mode")

    logger.error("error occurred")

    logger.critical("Critical issue is created")
