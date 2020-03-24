import os

from common.http_client import HttpClient


class PostkunBase:

    def __init__(self):
        self.message = {}

    def set_text(self, text):
        pass

    def set_color(self, color):
        pass

    def set_attachments(self, contents):
        pass

    def post_message(self):
        try:
            url = os.environ["MESSENGER_URL"]
            headers = {"Content-type": "application/json"}
            body = HttpClient.post(url, self.message, headers)
            return body
        except KeyError as e:
            print("environment value {0} is not found.".format(e))
            return False
