# -*- coding: utf-8 -*-
from os import path, mkdir
from time import strftime, localtime, time
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

log_file_path = "log"
log_file_name = strftime("%Y-%m-%d %Hh %Mm %Ss.log", localtime(time()))
log_formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s", "%Y-%m-%d %H:%M:%S")

if not path.exists(path.join(log_file_path)):
    mkdir(log_file_path)


file = logging.FileHandler(path.join(log_file_path, log_file_name))
file.setFormatter(log_formatter)

console = logging.StreamHandler()
console.setFormatter(log_formatter)

logger.addHandler(hdlr=file)
logger.addHandler(hdlr=console)
