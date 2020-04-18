from slack import SlackHandler

t = SlackHandler()
t.set_title("AWS 4月の利用料金")
t.set_text("料金通知")
t.set_color("#f8991e")
print(t.post_message())
