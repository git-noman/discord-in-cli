import json

class Tools:
    """ General utility tools
    """

    @staticmethod
    def feed(msg: dict) -> None:
        """ Feed message to the message pool stored in message_pool.json
        """
        with open('store/message_pool.json', 'r+') as f:
            msg_pool = json.loads(f.read())
            msg_pool.append(msg)
            f.seek(0)
            f.write(json.dumps(msg_pool, indent=4, ensure_ascii=False))
            f.truncate()