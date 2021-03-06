"""Available Commands : .stats

Edited by @One_m4x1m"""
from telethon import events
import asyncio
from datetime import datetime
from telethon.tl.types import User, Chat, Channel


@borg.on(events.NewMessage(pattern=r"\.stats", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    pm = 0
    grps = 0
    supergrps = 0
    chnls = 0
    bots = 0
    dialogs = await borg.get_dialogs(
        limit=None,
        ignore_migrated=True
    )
    for d in dialogs:
        currrent_entity = d.entity
        if type(currrent_entity) is User:
            if currrent_entity.bot:
                bots += 1
            else:
                pm += 1
        elif type(currrent_entity) is Chat:
            grps += 1
        elif type(currrent_entity) is Channel:
            if currrent_entity.broadcast:
                chnls += 1
            else:
                supergrps += 1
        else:
            print(d)
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit(f"**Your stats obtained in {ms} second(s).\nYou have {pm} private messages.\nYou are in {grps} groups.\nYou are in {supergrps} super groups.\nYou are in {chnls} channels.\nYou have chats with {bots} bots.**")
