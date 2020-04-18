import sys


def main():
    t = SlackHandler()
    t.set_title("AWS 4月の利用料金")
    t.set_text("料金通知")
    t.set_color("#f8991e")
    print(t.post_message())
    return 0


if __name__ == '__main__':
    from postkun.slack import SlackHandler

    sys.exit(main())
