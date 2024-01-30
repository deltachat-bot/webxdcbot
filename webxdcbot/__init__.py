#!/usr/bin/env python3
"""Minimal bot + webxdc example."""

import json
from pathlib import Path

from deltabot_cli import BotCli, ChatType, EventType, events

from .app import get_response

cli = BotCli("webxdcbot")
XDC_PATH = str(Path(__file__).parent / "app.xdc")


@cli.on(events.RawEvent)
def on_event(bot, accid, event):
    """process webxdc status updates"""
    if event.kind == EventType.WEBXDC_STATUS_UPDATE:
        bot.logger.info(event)
        msgid = event.msg_id
        serial = event.status_update_serial - 1
        update = json.loads(bot.rpc.get_webxdc_status_updates(accid, msgid, serial))[0]
        resp = get_response(update["payload"])
        if resp:
            bot.rpc.send_webxdc_status_update(
                accid, msgid, json.dumps(resp), resp.get("info", "")
            )


@cli.on(events.NewMessage(is_info=False))
def send_app(bot, accid, event):
    """send the webxdc app on every 1:1 (private) message"""
    chatid = event.msg.chat_id
    if bot.rpc.get_basic_chat_info(accid, chatid).chat_type != ChatType.SINGLE:
        return
    bot.logger.info(f"new 1:1 message: {event.msg.text!r}")
    bot.rpc.send_msg(accid, chatid, {"file": XDC_PATH})


def main():
    cli.start()
