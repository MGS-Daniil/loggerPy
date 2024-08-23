from logging import Logger
import logging
from pylogging_tools._logger import *
from pylogging_tools._logger import _Logger

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(name)s]> %(levelname)s - %(message)s")

__all__ = ["LoggingTools"]


class LoggingTools:
    """
    A class that provides logging functionality.
    """
    _name: str | None
    __logger: logging.Logger | None
    __file_handler: logging.FileHandler | None
    level: int | None

    def __init__(self,
                 name: str,
                 level: int = INFO,
                 file: str | None = None,
                 filemode: str = "a",
                 log_format: str = "{time} [name]> level - message"):
        self._name = name
        self.level: int = level
        self.log_format = log_format
        if file is not None:
            self.to_file(file=file, mode=filemode)
        __logger: Logger = logging.getLogger(name)
        __logger.setLevel(level)
        self.__logger: _Logger = _Logger(__logger)

    def to_file(self, file, mode):
        self.__file_handler = logging.FileHandler(filename=file, mode=mode)
        self.__logger.get_logger().addHandler(self.__file_handler)

    def __getattr__(self, item):
        methods = {
            "debug": self.__logger.debug,
            "info": self.__logger.info,
            "warning": self.__logger.warning,
            "error": self.__logger.error,
            "critical": self.__logger.critical,
            "get_logger": self.__logger.get_logger
        }
        if item in methods:
            return methods[item]
        return getattr(self.__logger, item)


# GitHub actions and tests
