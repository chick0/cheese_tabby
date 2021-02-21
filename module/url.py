# -*- coding: utf-8 -*-

from conf import conf


def get_link(bot):
    return f"https://discord.com/api/oauth2/authorize" \
           f"?client_id={bot.user.id}" \
           f"&permissions={conf['bot']['invite_permission']}" \
           f"&scope=bot"
