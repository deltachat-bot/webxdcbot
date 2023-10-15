from fortune import fortune


def get_response(payload):
    if payload.get("request"):
        return {"payload": {"response": {"name": "bot", "text": fortune()}}}
