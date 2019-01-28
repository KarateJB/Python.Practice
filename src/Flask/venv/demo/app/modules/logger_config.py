import sys
import os
import logging
from datetime import date


def init_logging(logger, min_logging_level):
    # Add DEBUG handler
    add_handler(logger, logging.DEBUG)
    # Add ERROR handler
    add_handler(logger, logging.ERROR)
    # Set level for this logger
    logger.setLevel(min_logging_level)


def add_handler(logger:logging.Logger, level):
    level_name = logging.getLevelName(level).lower()
    logging_format = logging.Formatter('[%(asctime)s][%(thread)s][%(levelname)s][%(module)s.%(funcName)s(%(filename)s, %(lineno)s)]%(message)s')
    logfiles_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", str(date.today()))
    create_log_dir(logfiles_path)
    handler = logging.FileHandler('{0}\\flask.{1}.log'.format(logfiles_path, level_name), encoding='UTF-8')
    handler.setLevel(level) # Set handler's log level
    handler.setFormatter(logging_format) # Set format
    logger.addHandler(handler) 

def create_log_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


