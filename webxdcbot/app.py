"""Example processing of incoming webxdc status updates."""
from fortune import fortune


def get_response(payload):
    # only handle requests, ignore responses from self
    if payload.get("request"):
        text = fortune()
        response = {"response": {"name": "bot", "text": text}}

        # check https://docs.webxdc.org/spec.html#sendupdate
        update = {"payload": response, "info": text}

        return update
