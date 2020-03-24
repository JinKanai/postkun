from base import PostkunBase


class SlackHandler(PostkunBase):

    def __init__(self):
        self.message = {
                "channel": "C1H9RESGL",
                "blocks": [
                    {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Danny Torrence left the following review for your property:"
                    }
                    },
                    {
                    "type": "section",
                    "block_id": "section567",
                    "text": {
                        "type": "mrkdwn",
                        "text": "<https://google.com|Overlook Hotel> \n :star: \n Doors had too many axe holes, guest in room 237 was far too rowdy, whole place felt stuck in the 1920s."
                    },
                    "accessory": {
                        "type": "image",
                        "image_url": "https://is5-ssl.mzstatic.com/image/thumb/Purple3/v4/d3/72/5c/d3725c8f-c642-5d69-1904-aa36e4297885/source/256x256bb.jpg",
                        "alt_text": "Haunted hotel image"
                    }
                    },
                    {
                    "type": "section",
                    "block_id": "section789",
                    "fields": [
                        {
                        "type": "mrkdwn",
                        "text": "*Average Rating*\n1.0"
                        }
                    ]
                    }
                ]
            }

    def set_title(self, title):
        self.message[""]

    def set_text(self, text):
        self.message["text"] = text

    def set_color(self, color):

        self.message["color"] = color

    def set_attachments(self, contents):
        self.message["attachments"] = contents


if __name__ == "__main__":
    t = SlackHandler()
    t.set_text("test-death")
    t.set_color("danger")
    print(t.post_message())
