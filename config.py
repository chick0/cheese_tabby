# -*- coding: utf-8 -*-
from os import path, listdir
from configparser import ConfigParser


config = ConfigParser()
for conf_file in listdir(path.join("conf")):
    if conf_file.endswith(".ini"):
        config.read(path.join("conf", conf_file))
