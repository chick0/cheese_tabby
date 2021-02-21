# -*- coding: utf-8 -*-

from redis import Redis

from conf import conf


redis = Redis.from_url(url=conf['redis']['url'])


def set_cache(image_id: str, cache):
    redis.set(image_id, cache)


def get_cache(image_id: str):
    return redis.get(image_id)
