from base import PostkunBase


class TocaroHandler(PostkunBase):

    def __init__(self):
        self.message = {
            "text": "string",
            "color": "color //info,warning,danger,success",
            "attachments": [
                {
                    "title": "string",
                    "value": "string"
                },
                {"image_url": "URL"}

            ]
        }

    def set_text(self, text):
        self.message["text"] = text

    def set_color(self, color):

        self.message["color"] = color

    def set_attachments(self, contents):
        self.message["attachments"] = contents


if __name__ == "__main__":
    t = TocaroHandler()
    t.set_text("test-death")
    t.set_color("danger")
    print(t.post_message())
