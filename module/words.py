# -*- coding: utf-8 -*-

from os import path, listdir
from json import dump
from logging import getLogger

logger = getLogger()

words = []
queue = listdir(path.join("words"))
for file in queue:
    if file.endswith(".txt"):
        logger.info(f"Loading words from '{file}'...")
        with open(path.join("words", file), mode="r", encoding="utf-8") as fp:
            tmp = fp.read()

        tmp = tmp.replace("\n", ",").replace(" ", "").split(",")
        words.extend(tmp)

logger.info(f"Number of registered words '{len(words)}'")
dump(obj=words,
     fp=open(path.join("words", "words.json"), mode="w", encoding="utf-8"))
