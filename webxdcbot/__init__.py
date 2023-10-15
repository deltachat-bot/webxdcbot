#!/usr/bin/env python3
"""Minimal bot + webxdc example."""

import logging
from pathlib import Path

from deltabot_cli import BotCli, EventType, events
from deltachat_rpc_client.const import ChatType

from .app import get_response

cli = BotCli("webxdcbot")
XDC_PATH = str(Path(__file__).parent / "app.xdc")


@cli.on(events.RawEvent)
def on_event(event):
    """process webxdc status updates"""
    if event.type == EventType.WEBXDC_STATUS_UPDATE:
        logging.info(event)
        msg = event.account.get_message_by_id(event.msg_id)
        update = msg.get_webxdc_status_updates(event.status_update_serial - 1)[0]
        resp = get_response(update["payload"])
        if resp:
            msg.send_webxdc_status_update(resp, resp.get("info", ""))


@cli.on(events.NewMessage)
def send_app(event):
    """send the webxdc app on every 1:1 (private) message"""
    if event.message_snapshot.chat.get_basic_snapshot().chat_type != ChatType.SINGLE:
        return
    logging.info(f"new 1:1 message: {event.message_snapshot.text!r}")
    event.message_snapshot.chat.send_message(file=XDC_PATH)


def main():
    cli.start()
