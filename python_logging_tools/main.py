from logging import Logger, ERROR, WARNING, INFO, DEBUG, CRITICAL
import sys
import logging

logging.basicConfig(level=logging.INFO, format="[%(name)s]> %(levelname)s - %(message)s")

__all__ = ["LoggingTools",
           "ERROR", "WARNING", "INFO", "DEBUG", "CRITICAL",
           "_run_test"]


class LoggingTools:
    """
    A class that provides logging functionality.
    """
    _name: str | None
    level: int | None
    __logger: logging.Logger | None
    file_handlers: dict = {}

    def __new__(cls, name: str, level: int, *args, **kwargs):
        if name is None:
            raise KeyError(
                "Logger name cannot be None"
            )
        if level is None:
            level = logging.INFO
        object_ = super().__init__(cls, name, level, *args, **kwargs)
        return object_

    def __init__(self,
                 name: str,
                 level: int,
                 file: str | None = None,
                 filemode: str = "a",
                 log_format: str | None = "{time} [name]> level - message"):
        self._name = name
        self.level: int = level
        self.log_format = log_format
        if file is not None:
            self.to_file(file=file, mode=filemode)
        self.__logger: Logger = logging.getLogger(self._name)
        self.__logger.setLevel(self.level)

    def to_file(self, file, mode):
        if file in self.file_handlers:
            return
        self.file_handlers[file] = logging.FileHandler(filename=file, mode=mode)
        self.__logger.addHandler(self.file_handlers[file])

    def debug(self, msg, *args, **kwargs):
        self.__logger.debug(msg)

    def __log(self, msg, level, *args, **kwargs):
        self.__logger.log(msg=msg, level=level)

    def info(self, msg):
        if self.to_file is True:
            self.__logger.info(msg)
        else:
            self.__log(msg, logging.INFO)

    def warning(self, msg):
        self.warning.__doc__ = 'Logs an warning message.'
        self.__log(msg, logging.WARNING)

    def error(self, msg):
        self.error.__doc__ = 'Logs an error message.'
        self.__log(msg, logging.ERROR)

    def critical(self, msg):
        self.critical.__doc__ = 'Logs a critical message.'
        self.__log(msg, logging.CRITICAL)

    def get_logger(self) -> Logger | None:
        """Returns the logger object"""
        return self.__logger


# GitHub actions and tests
def git_path_loader():
    sys.path.append(__file__.rstrip("main.py"))


if sys.argv.count("-git") > 0:
    git_path_loader()


def _run_test() -> bool:
    try:
        print("")
        log_test = LoggingTools(name="test", level=INFO)
        log_test.debug("Test Debug")
        log_test.info("Test Info")
        log_test.warning("Test Warning")
        log_test.error("Test Error")
        log_test.critical("Test Critical")
        return True
    except Exception:
        return False
