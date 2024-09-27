import logging


class logs():


    def logging(self):

        logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        # logger.debug("Debug log")
        # logger.info("Information log ")
        # logger.warning("Warning log")
        # logger.error("Error log")
        # logger.critical("Critical log")
        return logger